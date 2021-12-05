from MyCourseParent import MyCourseParent


class Assignment(MyCourseParent):
    def __init__(self, name):
        MyCourseParent.__init__(self, name, self.__class__.__name__)
        self.name = name
        self.desc = ""
        self.due_date = ""
        self.status = "Not Started"
        self.weight = 1
        self.score = 0
        self.importance = 0

    def add_assignment_info(self):
        if self.desc == "":
            self.desc = input("Description: ")
        if self.due_date == "":
            self.due_date = input("Due Date: ")
        if self.weight == "":
            self.weight = input("Category Weight: ")
        if self.importance == "":
            self.importance = input("Importance (0-3):  ")

    def prompt(self):
        action = input("What would you like to do with this assignment? (type 'help' for actions)\n")

        if action == "help":
            print("Add assignment info\nUpdate\nInfo\nReturn\nExit")
        elif action == "Add items":
            self.add_items()
        elif action == "Update":
            self.update()
        elif action == "Info":
            self.info()
        elif action == "Exit":
            return False
        elif action == "Return":
            return  # to myCourses
        else:
            print("Sorry, that is not one of my available actions.")
        self.prompt()

    def add_items(self):
        if len(self.sub_items) == 0:
            print(f"No {self.sub_type}s defined. Please specify one.\n")
            func = self.sub_type
            new_item = func(input(f"{self.sub_type}:"))
            self.sub_items.append(new_item)
        else:
            if yes(f"Add new {self.sub_type}?"):
                func = self.sub_type
                new_item = func(input(f"{self.sub_type}:"))
                self.sub_items.append(new_item)
                # self.sub_items.append(getattr(self, self.sub_type)(input(f"{self.sub_type}:")))
        if self.sub_type.subtype is not None and yes(f"Add new {self.sub_type.subtype}?"):
            select(self.sub_type, self.sub_items, "add_items")