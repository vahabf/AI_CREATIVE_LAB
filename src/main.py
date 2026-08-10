from core.config import Config
from core.logger import log
from automation.task_runner import run_task


def main():
    log("🌌 AI CREATIVE LAB started")
    log(f"Project: {Config.PROJECT_NAME}")

    result = run_task("first_test")

    log(f"Automation result: {result}")


if __name__ == "__main__":
    main()