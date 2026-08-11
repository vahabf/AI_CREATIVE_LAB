from decision.decision_runner import DecisionRunner


runner = DecisionRunner()


decision = runner.select_best()


print("🌌 Best Decision")
print("----------------")
print(decision)