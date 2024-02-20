import xmltodict

xml_data = open("payments.xml").read()
data_dict = xmltodict.parse(xml_data)
root = data_dict["employees"]
employees = root["employee"]

python_salaries = []

for i in employees:
    if "python" in i["job_title"].lower():
        for j in i["monthly_payment"].values():
            python_salaries.append(int(j))

# print(sum(python_salaries) / len(python_salaries))
print(len(python_salaries))
