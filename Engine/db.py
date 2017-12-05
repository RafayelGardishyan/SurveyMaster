import sqlite3

class db:
    def __init__(self, DBNAME):
        self.DBNAME = DBNAME + ".sqlite"
        self.db = sqlite3.connect(self.DBNAME)
        self.cursor = self.db.cursor()

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

        self.cursor.execute(query)


    def selectpv(self, table, param, value):
        query = """SELECT *  FROM """ + table + """ WHERE """ + param + """=""" + value
        self.cursor.execute(query)

        return self.cursor.fetchall()

    def selectall(self, table):
        query = """SELECT *  FROM """ + table
        self.cursor.execute(query)
        
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

        self.cursor.execute(query)
