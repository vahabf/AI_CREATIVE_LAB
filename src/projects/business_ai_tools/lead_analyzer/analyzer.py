class LeadAnalyzer:
    def __init__(self):
        self.services = {
            "3d": "3D Design",
            "animation": "Animation",
            "video": "Video Production",
            "website": "Web Development",
            "automation": "AI Automation",
            "ai": "AI Service",
            "music": "Music Production"
        }

    def analyze(self, message):
        text = message.lower()

        detected_service = "Unknown"
        category = "General"

        for keyword, service in self.services.items():
            if keyword in text:
                detected_service = service
                break

        if detected_service in [
            "3D Design",
            "Animation",
            "Video Production",
            "Music Production"
        ]:
            category = "Creative"

        elif detected_service in [
            "AI Automation",
            "AI Service",
            "Web Development"
        ]:
            category = "Technology"

        result = {
            "message": message,
            "service": detected_service,
            "category": category,
            "priority": self.calculate_priority(text),
            "estimated_value": self.estimate_value(detected_service)
        }

        return result


    def calculate_priority(self, text):

        high_words = [
            "urgent",
            "asap",
            "quick",
            "deadline"
        ]

        for word in high_words:
            if word in text:
                return "high"

        return "medium"


    def estimate_value(self, service):

        values = {
            "AI Automation": "$500-$3000",
            "AI Service": "$200-$2000",
            "3D Design": "$100-$1000",
            "Animation": "$300-$3000",
            "Video Production": "$200-$2000",
            "Web Development": "$500-$5000",
            "Music Production": "$100-$1000",
            "Unknown": "Need evaluation"
        }

        return values.get(service, "Need evaluation")