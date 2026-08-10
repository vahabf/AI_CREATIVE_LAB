class DecisionEngine:

    def __init__(self):
        self.criteria = {
            "income_speed": 0.25,
            "scalability": 0.25,
            "skill_alignment": 0.25,
            "ai_resistance": 0.25
        }


    def evaluate(self, opportunity):

        score = 0

        for key, weight in self.criteria.items():
            score += opportunity.get(key, 0) * weight

        return {
            "name": opportunity["name"],
            "score": round(score, 2),
            "decision": self.classify(score)
        }


    def classify(self, score):

        if score >= 8:
            return "HIGH_PRIORITY"

        elif score >= 5:
            return "TEST_REQUIRED"

        else:
            return "LOW_PRIORITY"