from decision.decision_engine import DecisionEngine


engine = DecisionEngine()


opportunity = {
    "name": "AI Creative Automation Service",
    "income_speed": 8,
    "scalability": 9,
    "skill_alignment": 9,
    "ai_resistance": 7
}


result = engine.evaluate(opportunity)


print(result)