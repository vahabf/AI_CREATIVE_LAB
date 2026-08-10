from opportunity.opportunity_store import OpportunityStore


store = OpportunityStore()

items = store.load()


print("Opportunity Database")
print("--------------------")

for item in items:
    print(
        item["name"]
    )