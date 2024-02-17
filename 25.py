import json

f = open("payments.json")
data = json.load(f)
selected_employees = []

for i in data["employees"]:
    selected_employees.append({i["name"]: i["job_title"]})

for i in selected_employees:
    print(i)
