import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers (name, city, phone);")

# cur.execute("INSERT INTO customers VALUES ('Mohsen','Tehran','09213378325');")
# cur.execute("INSERT INTO customers VALUES ('Yas','Shiraz','09334458378');")
# cur.execute("INSERT INTO customers VALUES ('Mohammad','Tabriz','09193378444');")
# cur.execute("INSERT INTO customers VALUES ('Mohsen','Tehran','09213370909');")

cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
for i in records:
    print(i)

# print(records)

con.commit()
con.close()
print('Done')
