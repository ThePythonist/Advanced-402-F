import jdatetime

today = str(jdatetime.datetime.now()).split()
day = today[0].split("-")[2]
month = today[0].split("-")[1]
print(f"Month : {month} \nDay : {day}")
