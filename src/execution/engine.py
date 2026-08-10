from memory.memory_store import MemoryStore
from core.logger import log


class ExecutionEngine:

    def __init__(self):
        self.memory = MemoryStore()

    def execute(self, task_name, action):
        log(f"Executing: {task_name}")

        result = action()

        self.memory.save(
            task=task_name,
            status="completed",
            result=result
        )

        return result