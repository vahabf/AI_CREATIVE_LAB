import json
from datetime import datetime
from pathlib import Path


class MemoryStore:
    def __init__(self):
        self.file_path = Path("src/memory/execution_history.json")

    def save(self, task, status, result=None):
        history = self.load()

        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "task": task,
            "status": status,
            "result": result
        }

        history.append(entry)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)

        return entry

    def load(self):
        if not self.file_path.exists():
            return []

        if self.file_path.stat().st_size == 0:
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)