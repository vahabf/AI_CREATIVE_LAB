from .batch import BatchLeadAnalyzer


runner = BatchLeadAnalyzer()


results = runner.run(
    "src/projects/business_ai_tools/lead_analyzer/data/leads.json"
)


runner.save_results(
    results,
    "src/projects/business_ai_tools/lead_analyzer/data/results.json"
)


print(results)