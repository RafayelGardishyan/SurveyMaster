from tkinter import *

class Survey_List_View:
    def __init__(self, DBOBJECT):
        self.views = {}
        self.DB = DBOBJECT
        print("Indexed database")


        self.surveys = {}
        print("Initialized main view")

    def name(self):
        return "Survey List View"

    def getViews(self, views):
        self.views = views

        print("Discovered views for " + self.name())

    def requieredActions(self):
        self.surveysRaw = self.DB.selectall("Surveys")

    def sortIntoDict(self):
        for item in self.surveysRaw:
            self.surveys[item[0]] = item[1]

    def deleteF(self, var):
        print(var.cget("text"))

    def runF(self, var):
        print(var.cget("text"))

    def loadInterface(self):
        self.sortIntoDict()
        self.mainwindow = Tk()
        for item in self.surveys:
            self.frame = Frame(self.mainwindow)
            self.id = Label(self.frame, text=str(item))
            self.name = Label(self.frame, text=str(self.surveys[item]))
            self.delete = Button(self.frame, text="Delete " + str(item))
            self.delete.configure( command=lambda b=self.delete: self.deleteF(b))
            self.play = Button(self.frame, text="Run " + str(item))
            self.play.configure(command=lambda b=self.play: self.runF(b))
            self.frame.pack()
            self.id.grid(row=0, column=0)
            self.name.grid(row=0, column=1)
            self.delete.grid(row=0, column=2)
            self.play.grid(row=0, column=3)
