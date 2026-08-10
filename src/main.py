from automation.file_organizer import organize_test
from core.config import Config
from core.logger import log
from automation.task_runner import run_task


def main():
    log("🌌 AI CREATIVE LAB started")
    log(f"Project: {Config.PROJECT_NAME}")

    result = run_task("first_test")

    log(f"Automation result: {result}")

    file_report = organize_test()

    log(f"File report: {file_report}")


if __name__ == "__main__":
    main()