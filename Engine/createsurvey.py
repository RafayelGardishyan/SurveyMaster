from guizero import *

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


    def loadInterface(self):
        self.mainapp = App("SurveyMaster : Main Menu", width=200, height=200)
        self.text = Text(self.mainapp, "Create survey")
        self.text = Text(self.mainapp, "Name of your survey:")
        self.textbox = TextBox(self.mainapp, width=200)
        self.button = PushButton(self.mainapp)

        self.mainapp.display()
