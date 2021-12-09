# import MyCourse, Course, Category, Assignment

class MyCourseParent:
    relationships = {
        "MyCourse": "Course",
        "Course": "Category",
        "Category": "Assignment",
        "Assignment": "None"
    }
    obj_type = "MyCourseParent"
    sub_type = "MyCourse"

    def __init__(self, name, self_obj_type):
        self.name = name
        # self.obj_type = self_obj_type
        # self.sub_items = []
        # sub_type = MyCourseParent.relationships[self_obj_type]

    def info(self):
        for key in self.__dict__.keys():
            print(f"{key}: {self.__dict__[key]}")

    def prompt(self):
        action = input("What would you like to do with this course? (type 'help' for actions)\n")

        if action == "help":
            print("Add items\nUpdate\nInfo\nReturn\nExit")
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
        pass  # must be overriden

    #     if len(self.sub_items) == 0:
    #         print(f"No {self.sub_type}s defined. Please specify one.\n")
    #         func = self.sub_type
    #         new_item = func(input(f"{self.sub_type}:"))
    #         self.sub_items.append(new_item)
    #     else:
    #         if yes(f"Add new {self.sub_type}?"):
    #             func = self.sub_type
    #             new_item = func(input(f"{self.sub_type}:"))
    #             self.sub_items.append(new_item)
    #             # self.sub_items.append(getattr(self, self.sub_type)(input(f"{self.sub_type}:")))
    #     if self.sub_type.subtype is not None and yes(f"Add new {self.sub_type.subtype}?"):
    #         select(self.sub_type, self.sub_items, "add_items")

    def update(self):
        self.info()
        update = input("Please enter label of data being updated")
        if update not in self.__dict__.keys():
            print("Label is not valid.")
        else:
            self.__setattr__(update, input("New value for " + update + ": "))
        self.prompt()


def yes(prompt):
    return input(prompt).strip()[0].lower() == "y"


def select(item, from_list, and_do=None):
    from_list_length = len(from_list)
    if from_list_length == 0:
        print(f"No {item}s!")
        return None

    print(f"{item}s:")
    for i in range(from_list_length):
        print(f"[{i}] {from_list[i].name}")

    item_id = int(input(f"{item} ID:"))
    while item_id not in range(from_list_length):
        print(f"Invalid {item} ID.")
        item_id = int(input(f"{item} ID:"))

    if and_do:
        return getattr(from_list[item_id], and_do)()

    return from_list[item_id]
