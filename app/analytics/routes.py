from flask import jsonify, make_response
from flask_login import login_required, current_user
from app.analytics import analytics_bp
from app.analytics.service import get_task_analytics, get_csv_export

@analytics_bp.route("/analytics", methods=["GET"])
@login_required
def get_analytics():
    analytics = get_task_analytics(current_user.id)
    return jsonify({"status": "success", "data": analytics, "message": "Analytics generated successfully"}), 200

@analytics_bp.route("/analytics/export", methods=["GET"])
@login_required
def get_analytics_report():
    csv_data = get_csv_export(current_user.id)

    if csv_data is None:
        return jsonify({"status": "error", "message": "No tasks to export"}), 404

    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=tasks.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    return response

