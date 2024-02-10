import sqlite3

con = sqlite3.connect("info.db")
cur = con.cursor()

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
users = [i[1:] for i in records]

new_record = {"name": "Bahar", "code": "40215", "job": "Civil Engineer"}

new_record = tuple(new_record.values())


def save(record):
    if record in users:
        print("Record already exists in database")
    else:
        query = f"INSERT INTO employees(name,code,job) VALUES {record}"
        cur.execute(query)
        print("Record Inserted")


# save(new_record)

con.commit()
con.close()
