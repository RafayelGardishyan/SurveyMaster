class View_Controller:
    def __init__(self, *VIEWS):
        self.VIEWSLIST = {}

        for view in VIEWS:
            self.VIEWSLIST[view.name()] = view

        for view in self.VIEWSLIST:
            self.VIEWSLIST[view].getViews(self.VIEWSLIST)

        print("Added " + str(len(self.VIEWSLIST)) + " views to controller")

        for view in self.VIEWSLIST:
            if view == "Main View":
                self.VIEWSLIST[view].loadInterface()