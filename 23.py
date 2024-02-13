import json

with open("states.json") as f1:
    data = json.load(f1)
    names = []

    for i in data["states"]:
        names.append(i["name"])

    f2 = open("state_names.json", "w")
    json.dump(names, f2, indent=4)
