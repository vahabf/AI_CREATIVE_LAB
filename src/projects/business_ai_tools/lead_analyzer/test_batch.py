from projects.business_ai_tools.lead_analyzer.batch import BatchLeadAnalyzer


runner = BatchLeadAnalyzer()

results = runner.run(
    "src/projects/business_ai_tools/lead_analyzer/data/leads.json"
)


print("🌌 Batch Lead Analysis")

for result in results:

    print("----------------")
    print(result)