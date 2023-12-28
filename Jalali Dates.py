import jdatetime

now = jdatetime.datetime.now()
today = jdatetime.date.today()
time = str(now).split()[1]
print(time)


# shamsi = jdatetime.date.fromgregorian(day=25, month=12, year=2023)
# print(shamsi)
