import json


class LeadReport:

    def generate(self, analysis):

        return {
            "title": "Lead Analysis Report",
            "client": analysis["client"],
            "service": analysis["service"],
            "score": analysis["lead_score"],
            "priority": analysis["priority"],
            "action": analysis["recommended_action"]
        }


    def save(self, report, filename="lead_report.json"):

        with open(filename, "w") as f:
            json.dump(
                report,
                f,
                indent=4
            )

        return filename