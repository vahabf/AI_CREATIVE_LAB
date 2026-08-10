from memory.memory_store import MemoryStore


memory = MemoryStore()

result = memory.save(
    task="memory_test",
    status="completed",
    result={"message": "first memory entry"}
)

print("Memory saved:")
print(result)

print("\nHistory:")
print(memory.load())