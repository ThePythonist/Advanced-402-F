import sqlite3

def create_table(table_name):
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    columns = tuple(input("Columns (seperated by comma) :").split(","))
    query = f"CREATE TABLE IF NOT EXISTS {table_name} {columns};"
    cur.execute(query)

def select(table):
    pass


def insert(table):
    pass


def main():
    operation = input("""
1 : Create Table
2 : Insert Record Into Table
3 : Select Record From Table
: """)

    if operation == "1":
        table_name = input("Enter table name : ")
        create_table(table_name)
    elif operation == "2":
        table_name = input("Enter table name : ")
        insert(table_name)
    elif operation == "3":
        table_name = input("Enter table name : ")
        select(table_name)


main()
