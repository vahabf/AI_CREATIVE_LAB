import json

from .models import Lead
from .analyzer import LeadAnalyzer


class BatchLeadAnalyzer:

    def __init__(self):
        self.analyzer = LeadAnalyzer()


    def load_leads(self, path):

        with open(path, "r") as f:
            return json.load(f)


    def run(self, path):

        leads = self.load_leads(path)

        results = []

        for item in leads:

            lead = Lead(
                name=item["name"],
                message=item["message"],
                budget=item["budget"],
                deadline=item["deadline"]
            )

            result = self.analyzer.analyze(lead)

            results.append(result)

        return results