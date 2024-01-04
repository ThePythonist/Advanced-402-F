from persiantools.jdatetime import JalaliDate, JalaliDateTime
import jdatetime
import pytz

year = jdatetime.datetime.now().year
month = jdatetime.datetime.now().month
minute = jdatetime.datetime.now().minute
day = jdatetime.datetime.now().day
hour = jdatetime.datetime.now().hour

now = JalaliDateTime(year, month, day, 0, 0, 0, 0, pytz.utc).strftime("%A")
print(now)
