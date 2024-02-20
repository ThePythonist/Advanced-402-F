import xmltodict

# XML data to be parsed
xml_data = open("payments.xml").read()

# Parse XML data into a dictionary
data_dict = xmltodict.parse(xml_data)

# Access the parsed data
root = data_dict['employees']
employees = root['employee']

# print(root)

under_30 = []
for i in employees:
    if int(i["age"]) <= 30:
        under_30.append(i)

print(under_30)
print(len(under_30),"Employees are under 30")
