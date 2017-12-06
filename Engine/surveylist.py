class Create_Survey_View:
    def __init__(self, DBOBJECT):
        self.views = {}
        self.DB = DBOBJECT
        print("Indexed database")



        print("Initialized main view")

    def name(self):
        return "Second View"

    def getViews(self, views):
        self.views = views

        print("Discovered views for " + self.name())
