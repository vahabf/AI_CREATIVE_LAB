import json
from pathlib import Path


class OpportunityStore:

    def __init__(self):
        self.file = Path(
            "src/opportunity/opportunities.json"
        )


    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)


    def add(self, opportunity):

        data = self.load()

        data.append(opportunity)

        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


        return opportunity