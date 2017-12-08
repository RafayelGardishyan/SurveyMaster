import sqlite3
print("Imported sqlite3")

class db:
    def __init__(self, DBNAME):
        self.DBNAME = DBNAME + ".sqlite"
        self.db = sqlite3.connect(self.DBNAME)
        print("Connected to database")

        self.cursor = self.db.cursor()
        print("Created cursor")
        self.closeDB()


    def openDB(self):
        self.db = sqlite3.connect(self.DBNAME)
        print("Connected to database")

        self.cursor = self.db.cursor()
        print("Created cursor")

    def closeDB(self):
        self.db.commit()
        self.db.close()
        print("Closed database")

    def insert(self, table, *cols, vals):
        self.openDB()
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
                valusecomma +=", \"" + i + "\""
            else:
                valusecomma += "\"" + i + "\""

        query = """INSERT INTO """ + table + """(""" + colscomma + """) VALUES(""" + valusecomma + """)"""


        print("Inserting query: " + query)

        try:
            self.cursor.execute(query)
            print("Successfully inserted into " + table)
        except:
            print("Failed to insert")

        self.closeDB()

    def selectpv(self, table, param, value):
        self.openDB()
        query = """SELECT *  FROM """ + table + """ WHERE """ + param + """=""" + value

        print("Selecting query: " + query)

        try:
            self.cursor.execute(query)
            print("Successfully selected")
            return self.cursor.fetchall()
        except:
            print("failed to select")

        self.closeDB()

    def selectpvptg(self, table, param, value, paramtoget):
        self.openDB()
        query = """SELECT """ + paramtoget + """  FROM """ + table + """ WHERE """ + param + """=\"""" + value + "\""

        print("Selecting query: " + query)

        try:
            self.cursor.execute(query)
            print("Successfully selected")
            return self.cursor.fetchall()
        except:
            print("failed to select")

        self.closeDB()

    def selectall(self, table):
        self.openDB()
        query = """SELECT *  FROM """ + table

        print("Selecting query: " + query)

        try:
            self.cursor.execute(query)
            print("Successfully selected")
            return self.cursor.fetchall()
        except:
            print("Failed to select")
        self.closeDB()

    def createtable(self, tablename, *cols):
        self.openDB()
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
        try:
            self.cursor.execute(query)
            print("Successfully created table \"" + tablename + "\"")
        except:
            print("Table exists or failed to create")
        self.closeDB()
