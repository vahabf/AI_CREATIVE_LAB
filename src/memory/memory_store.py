import json
import os
from datetime import datetime


class MemoryStore:

    def __init__(self):
        self.file = "src/memory/execution_history.json"


    def save(self, task_name, result):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                history = json.load(f)

        else:
            history = []


        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "task": task_name,
            "status": result.get("status"),
            "result": result.get("output")
        }


        history.append(entry)


        with open(self.file, "w") as f:
            json.dump(
                history,
                f,
                indent=4
            )