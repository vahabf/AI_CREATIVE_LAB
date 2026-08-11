from .batch import BatchLeadAnalyzer
from memory.memory_store import MemoryStore


runner = BatchLeadAnalyzer()

results = runner.run(
    "src/projects/business_ai_tools/lead_analyzer/data/leads.json"
)


memory = MemoryStore()


for index, result in enumerate(results):

    memory.save(
        f"lead_batch_{index+1}",
        {
            "status": "completed",
            "output": result
        }
    )


runner.save_results(
    results,
    "src/projects/business_ai_tools/lead_analyzer/data/results.json"
)


print("🌌 Batch completed")

for result in results:
    print(result)