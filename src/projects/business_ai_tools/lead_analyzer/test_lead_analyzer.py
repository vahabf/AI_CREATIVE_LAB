from analyzer import LeadAnalyzer


analyzer = LeadAnalyzer()


test_message = """
I need a 3D product animation
for my furniture company.
Deadline is next month.
"""


result = analyzer.analyze(test_message)


print("Lead Analysis")
print("----------------")

for key, value in result.items():
    print(f"{key}: {value}")