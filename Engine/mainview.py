from guizero import *

class Main_View:
    def __init__(self, DBOBJECT):
        self.views = {}
        self.DB = DBOBJECT
        print("Indexed database")



        print("Initialized main view")

    def name(self):
        return "Main View"

    def getViews(self, views):
        self.views = views

        print("Discovered views for " + self.name())

    def cs(self):
        for view in self.views:
            if view == "Create Survey View":
                self.views[view].loadInterface()

    def sl(self):
        for view in self.views:
            if view == "Survey List View":
                self.views[view].requieredActions()
                self.views[view].loadInterface()

    def tas(self):
        print("tas")

    def loadInterface(self):
        mainapp = App("SurveyMaster : Main Menu", width=200, height=200)
        text = Text(mainapp, "Welcome to SurveyMaster")
        but1 = PushButton(mainapp, text="Create Survey", command=self.cs)
        but2 = PushButton(mainapp, text="Surveys List", command=self.sl)
        but3 = PushButton(mainapp, text="Take a survey", command=self.tas)
        mainapp.display()