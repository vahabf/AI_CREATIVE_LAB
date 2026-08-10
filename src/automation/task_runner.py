from core.logger import log


def run_task(task_name):
    log(f"Running automation task: {task_name}")

    result = {
        "task": task_name,
        "status": "completed"
    }

    return result