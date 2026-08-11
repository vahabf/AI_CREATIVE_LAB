from decision.decision_engine import DecisionEngine
from opportunity.opportunity_store import OpportunityStore


class DecisionRunner:

    def __init__(self):

        self.engine = DecisionEngine()
        self.store = OpportunityStore()


    def select_best(self):

        opportunities = self.store.load()

        results = []

        for item in opportunities:

            result = self.engine.evaluate(item)

            results.append(result)


        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return results[0]