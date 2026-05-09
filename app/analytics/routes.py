from flask import jsonify, send_file
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
    analytics_buffer = get_csv_export(current_user.id)

    if analytics_buffer is None:
        return  jsonify({"status": "error", "message": "Can't generate report, data is not enough"}), 404

    return send_file(analytics_buffer, mimetype="text/csv", as_attachment=True, download_name="tasks.csv")


