from core.config import Config
from core.logger import log

from execution.engine import ExecutionEngine


def main():

    log("🌌 AI CREATIVE LAB started")
    log(f"Project: {Config.PROJECT_NAME}")

    engine = ExecutionEngine()

    result = engine.run("first_test")

    log(f"Engine result: {result}")


if __name__ == "__main__":
    main()