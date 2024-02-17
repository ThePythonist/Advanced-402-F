import json

f = open("states.json")
data = json.load(f)

selected_states = []
for i in data["states"]:
    if i["name"].lower() in ["alaska", "new york", "florida"]:
        selected_states.append(i)

print(selected_states)

output = {"states": selected_states}
file = open("selected_states.json", "w")
json.dump(output, file, indent=2)
