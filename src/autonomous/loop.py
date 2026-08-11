from decision.decision_runner import DecisionRunner
from execution.engine import ExecutionEngine
from core.logger import log


class AutonomousLoop:

    def __init__(self):

        self.decision = DecisionRunner()
        self.execution = ExecutionEngine()


    def run(self):

        log("🌌 Autonomous Loop started")

        selected = self.decision.select_best()

        log(
            f"Selected opportunity: {selected['name']}"
        )

        if selected["decision"] != "HIGH_PRIORITY":

            return {
                "status": "stopped",
                "reason": "No high priority action"
            }


        result = self.execution.run(
            "first_test"
        )


        return {
            "decision": selected,
            "execution": result
        }