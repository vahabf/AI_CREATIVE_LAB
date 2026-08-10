from core.config import Config
from core.logger import log
from execution.engine import ExecutionEngine
from automation.task_runner import run_task
from automation.file_organizer import organize_test


def main():

    log("🌌 AI CREATIVE LAB started")
    log(f"Project: {Config.PROJECT_NAME}")

    engine = ExecutionEngine()

    engine.execute(
        "first_test",
        lambda: run_task("first_test")
    )

    engine.execute(
        "file_scan",
        organize_test
    )


if __name__ == "__main__":
    main()