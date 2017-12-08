class View_Controller:
    def __init__(self, *VIEWS):
        self.VIEWSLIST = {}

        for view in VIEWS:
            self.VIEWSLIST[view.name()] = view

        for view in self.VIEWSLIST:
            self.VIEWSLIST[view].getViews(self.VIEWSLIST)

        for view in self.VIEWSLIST:
            try:
                self.VIEWSLIST[view].requieredActions()
                print("Completed requiered actions")
            except AttributeError:
                print("No requiered actions")

        print("Added " + str(len(self.VIEWSLIST)) + " views to controller")

        for view in self.VIEWSLIST:
            if view == "Main View":
                self.VIEWSLIST[view].loadInterface()
