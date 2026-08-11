from execution.registry import get_task
from core.logger import log
from memory.memory_store import MemoryStore


class ExecutionEngine:

    def __init__(self):
        self.memory = MemoryStore()

    def run(self, task_name):

        log(f"Executing: {task_name}")

        task = get_task(task_name)

        if not task:
            result = {
                "status": "failed",
                "error": "Task not found"
            }

        else:
            output = task()

            result = {
                "status": "completed",
                "task": task_name,
                "output": output
            }

        self.memory.save(
            task_name,
            result
        )

        return result