class Main_View:
    def __init__(self, DBOBJECT, *VIEWOBJECTS):
        self.views = {}
        self.DB = DBOBJECT
        print("Indexed database")

        for view in VIEWOBJECTS:
            self.views[VIEWOBJECTS.index(view)] = view

        print("Indexed views")

        print("Initialized main view")
