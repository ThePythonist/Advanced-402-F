import xmltodict

xml_data = open("flights.xml").read()
xml_dict = xmltodict.parse(xml_data)
root = xml_dict["flights"]
flights = root["flight"]
william_flights = []

for i in flights:
    for j in i["passengers"]["passenger"]:
        if j["name"] == "William Thompson":
            william_flights.append(i)

print(william_flights)
