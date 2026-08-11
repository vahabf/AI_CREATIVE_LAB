from projects.business_ai_tools.lead_analyzer.analyzer import LeadAnalyzer
from projects.business_ai_tools.lead_analyzer.models import Lead


lead = Lead(
    name="Luxury Furniture Co",
    message="Need a 3D product animation for our furniture line",
    budget="$2000",
    deadline="3 weeks"
)


analyzer = LeadAnalyzer()


result = analyzer.analyze(lead)


print("🌌 Lead Analysis")
print("----------------")

for key, value in result.items():
    print(f"{key}: {value}")