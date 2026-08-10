from automation.task_runner import run_task
from automation.file_organizer import organize_test


def first_test_task():
    return run_task("first_test")


TASKS = {
    "first_test": first_test_task,
    "file_scan": organize_test,
}


def get_task(name):
    return TASKS.get(name)