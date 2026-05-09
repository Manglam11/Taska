from flask import request, jsonify
from flask_login import login_required, current_user
from flask_socketio import emit
from app.tasks import tasks_bp
from app import db
from app.models import Task

VALID_STATUSES = ["pending", "in_progress", "completed"]
VALID_PRIORITIES = ["low", "medium", "high"]

@tasks_bp.route("/tasks", methods=["POST"])
@login_required
def create_task():
    data = request.get_json()

    user_id = current_user.id
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()
    status = data.get("status", "").strip()
    priority = data.get("priority", "").strip()

    if status not in VALID_STATUSES:
        return jsonify({"status": "error", "message": "Status must be pending, in_progress or completed"}), 400
    if priority not in VALID_PRIORITIES:
        return jsonify({"status": "error", "message": "Priority must be low, medium or high"}), 400

    if not title or not priority:
        return jsonify({"status": "error","message": "Invalid inputs. Try again."}), 400

    new_task = Task(user_id = user_id, title=title, priority=priority, description=description, status=status)
    db.session.add(new_task)
    db.session.commit()
    from app import socketio
    socketio.emit("task_updated", {"action": "created", "task": new_task.to_dict()})
    return jsonify({"status": "success","data": new_task.to_dict(), "message": "Task created successfully."}), 201


@tasks_bp.route("/tasks", methods=["GET"])
@login_required
def get_task():
    tasks = current_user.tasks

    task_list = [task.to_dict() for task in tasks]

    return jsonify({"status": "success", "data": task_list, "message": "Tasks fetched successfully."}), 200


@tasks_bp.route("/tasks/<int:id>", methods=["PUT"])
@login_required
def update_task(id):
    task = db.session.get(Task, id)

    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404

    if task.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Task doesn't belong to current user"}), 403

    data = request.get_json()

    if "title" in data:
        task.title = data["title"]
    if "priority" in data:
        task.priority = data["priority"]
    if "status" in data:
        task.status = data["status"]
    if "description" in data:
        task.description = data["description"]

    db.session.commit()
    from app import socketio
    socketio.emit("task_updated", {"action": "updated", "task": task.to_dict()})
    return jsonify({"status":"success", "data": task.to_dict(), "message": "Task updated successfully"}), 200

@tasks_bp.route("/tasks/<int:id>", methods=["DELETE"])
@login_required
def delete_task(id):
    task = db.session.get(Task, id)

    if not task:
        return jsonify({"status": "error", "message": "Task not found"}), 404

    if task.user_id != current_user.id:
        return jsonify({"status": "error", "message": "Task doesn't belong to current user"}), 403

    db.session.delete(task)
    db.session.commit()
    from app import socketio
    socketio.emit("task_updated", {"action": "deleted", "task_id": id})
    return jsonify({"status":"success", "message": "Task deleted successfully"}), 200

