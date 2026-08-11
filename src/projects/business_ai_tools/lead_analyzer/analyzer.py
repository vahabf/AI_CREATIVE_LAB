from .models import Lead
from .report import LeadReport


class LeadAnalyzer:

    def analyze(self, lead: Lead):

        service = self.detect_service(lead.message)

        score = self.calculate_score(
            lead.budget,
            lead.deadline,
            service
        )

        analysis = {
            "client": lead.name,
            "service": service,
            "lead_score": score,
            "priority": self.priority(score),
            "recommended_action": self.action(score)
        }

        report = LeadReport()

        generated_report = report.generate(analysis)

        report.save(generated_report)

        return analysis


    def detect_service(self, message):

        text = message.lower()

        services = {
            "3d": "3D Design",
            "animation": "3D Animation",
            "video": "Video Production",
            "automation": "AI Automation",
            "website": "Web Development",
            "music": "Music Production"
        }

        for key, value in services.items():

            if key in text:
                return value

        return "Unknown"


    def calculate_score(self, budget, deadline, service):

        score = 50

        if "$" in budget:
            score += 20

        if "week" in deadline.lower():
            score += 15

        if service != "Unknown":
            score += 15

        return min(score, 100)


    def priority(self, score):

        if score >= 80:
            return "High"

        if score >= 60:
            return "Medium"

        return "Low"


    def action(self, score):

        if score >= 80:
            return "Send proposal immediately"

        return "Review manually"