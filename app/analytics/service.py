import pandas as pd
import numpy as np
from app.models import Task
from io import BytesIO

def _get_user_df(user_id) -> pd.DataFrame | None:
    """
    Private helper function.
    Fetches all tasks for a user, load into ad DataFrame

    Args:
        user_id: Parameter to select the user.

    """
    tasks = Task.query.filter_by(user_id=user_id).all()
    if not tasks:
        return None
    return pd.DataFrame([task.to_dict() for task in tasks])

def get_task_analytics(user_id) -> dict:
    """
    Compute stats using Pandas and Numpy

    Args:
        user_id: Parameter to select the user.

    Returns:
        dict: Dictionary containing task analytics
    """
    df = _get_user_df(user_id)

    if df is None:
        return {
            "total": 0,
            "completed": 0,
            "pending": 0,
            "in_progress": 0,
            "completion_percentage": 0.0,
            "by_priority": {"low":0, "medium":0, "high":0}
        }

    total_tasks = df.shape[0]
    completed_tasks = df[df["status"] == "completed"].shape[0]
    priority_counts = df["priority"].value_counts().to_dict()

    return {
        "total": total_tasks,
        "completed": completed_tasks,
        "pending": df[df["status"] == "pending"].shape[0],
        "in_progress": df[df["status"] == "in_progress"].shape[0],
        "completion_percentage": np.round((completed_tasks/total_tasks)*100,2),
        "by_priority": {"low": priority_counts.get("low",0),
                        "medium": priority_counts.get("medium",0),
                        "high": priority_counts.get("high",0)}
    }


def get_csv_export(user_id) -> BytesIO | None:
    """
    Converts DataFrame to CSV.
    &
    Makes user to download his reports analytics in .csv format.

    Args:
        user_id: Parameter to select the user.

    Returns:

         StringIO: Buffer of analytics report.

         None: When there is no tasks for user.

    """
    df = _get_user_df(user_id)
    if df is None:
        return None
    buffer = BytesIO()
    df.to_csv(buffer, index=False, encoding="utf-8")
    buffer.seek(0)
    return buffer