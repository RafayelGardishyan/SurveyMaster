import sqlite3
print("Imported sqlite3")

class db:
    def __init__(self, DBNAME):
        self.DBNAME = DBNAME + ".sqlite"
        self.db = sqlite3.connect(self.DBNAME)
        print("Connected to database")

        self.cursor = self.db.cursor()
        print("Created cursor")

    def insert(self, table, *cols, **vals):
        values = []
        columns = []
        valusecomma = ""
        colscomma = ""
        for col in cols:
            columns.append(col)

        for i in columns:
            if i != columns[0]:
                colscomma += "," + i
            else:
                colscomma += i

        for val in vals:
            values.append(val)

        for i in values:
            if i != values[0]:
                valusecomma += "," + i
            else:
                valusecomma += i

        query = """INSERT INTO """ + table + """(""" + colscomma + """) VALUES(""" + valusecomma + """)"""

        print("Inserting query: " + query)

        self.cursor.execute(query)
        print("Successfully inserted into " + table)


    def selectpv(self, table, param, value):
        query = """SELECT *  FROM """ + table + """ WHERE """ + param + """=""" + value

        print("Selecting query: " + query)

        self.cursor.execute(query)

        print("Successfully selected")

        return self.cursor.fetchall()

    def selectall(self, table):
        query = """SELECT *  FROM """ + table

        print("Selecting query: " + query)

        self.cursor.execute(query)

        print("Successfully selected")

        return self.cursor.fetchall()

    def createtable(self, tablename, *cols):
        columns = []
        colscomma = ""
        for col in cols:
            columns.append(col)

        for i in columns:
            if i != columns[0]:
                colscomma += "," + i + " text NOT NULL"
            else:
                colscomma += i

        query = """CREATE TABLE """ + tablename + """ (id integer PRIMARY KEY, """ + colscomma + """)"""

        print("Creating table with: " + query)

        self.cursor.execute(query)

        print("Successfully created table \"" + tablename + "\"")
