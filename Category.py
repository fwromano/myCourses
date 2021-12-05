from MyCourseParent import *


class Category(MyCourseParent):

    def __init__(self, name):
        MyCourseParent.__init__(self, name, self.__class__.__name__)
        self.name = name
        self.weight = 0
        self.score = self.compute_score()
        self.items = []

    def add_grade_category_data(self):
        if self.weight == 0:
            self.weight = int(input("Course weight of Category: "))
        if len(self.items) == 0:
            if input("Add Assignments? (y/n): ") == "y":
                self.add_items()

    def add_items(self):
        #     todo
        new_item = Assignment(input("Assignment name: "))
        new_item.add_assignment_info()
        self.items.append(new_item)
        pass

    def compute_score(self):
        # todo
        return 0
