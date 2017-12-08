from tkinter import *

class Create_Survey_View:
    def __init__(self, DBOBJECT):
        self.views = {}
        self.DB = DBOBJECT
        print("Indexed database")



        print("Initialized Create Survey View")

    def name(self):
        return "Create Survey View"

    def getViews(self, views):
        self.views = views

        print("Discovered views for " + self.name())

    def getNameAndAddToDB(self):
        print("Creating Survey")
        name = self.surveyname.get()
        print("Survey name: " + name)
        self.DB.createtable("Surveys", "Name")
        self.DB.insert("Surveys", "Name", vals=[name])
        print(self.DB.selectpvptg("Surveys", "Name", name, "id"))

    def loadInterface(self):
        self.mainapp = Tk()
        self.text = Label(self.mainapp, text="Create Survey")
        self.text1 = Label(self.mainapp, text="Survey name:")
        self.surveyname = Entry(self.mainapp,)
        self.button = Button(self.mainapp, text="Create", command=self.getNameAndAddToDB)

        self.text.grid(column=0, row=0)
        self.text1.grid(column=0, row=1)
        self.surveyname.grid(column=1, row=1)
        self.button.grid(column=0, row=2, columnspan=2)