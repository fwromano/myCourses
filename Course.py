from MyCourseParent import *
from Category import *


class Course(MyCourseParent):

    def __init__(self, name):
        MyCourseParent.__init__(self, name, self.__class__.__name__)
        self.name = name
        self.instructor = "unknown"
        self.schedule = []
        self.location = "unknown"
        self.grade = self.compute_grade()
        self.grade_categories = []
        self.add_items()

    def compute_grade(self):
        # todo
        return "NA"

    def add_items(self):
            if len(self.sub_items) == 0:
                print(f"No Categories defined. Please specify one.\n")

                new_item = Category(input(f"{self.sub_type}:"))
                self.sub_items.append(new_item)
            else:
                if yes(f"Add new Category?"):

                    new_item = Category(input(f"{self.sub_type}:"))
                    self.sub_items.append(new_item)
                    # self.sub_items.append(getattr(self, self.sub_type)(input(f"{self.sub_type}:")))
            if Category.sub_type is not None and yes(f"Add new {Category.sub_type}?"):
                select(self.sub_type, self.sub_items, "add_items")
