from MyCourseParent import *


class Course(MyCourseParent):

    def __init__(self, name, obj_type, sub_type):
        MyCourseParent.__init__(self, name, obj_type, sub_type)
        self.name = name
        self.instructor = "unknown"
        self.schedule = []
        self.location = "unknown"
        self.grade = self.compute_grade()
        self.grade_categories = []
        self.add_course_data()

    def compute_grade(self):
        # todo
        return "NA"

    class GradeCategory:

        def __init__(self, name):
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
            new_item = self.Items(input("Assignment name: "))
            new_item.add_item_info()
            self.items.append(new_item)
            pass

        def compute_score(self):
            # todo
            return 0

        class Items:
            def __init__(self, name):
                self.name = name
                self.desc = ""
                self.due_date = ""
                self.status = "Not Started"
                self.weight = 1
                self.score = 0
                self.importance = 0

            def add_item_info(self):
                if self.desc == "":
                    self.desc = input("Description: ")
                if self.due_date == "":
                    self.due_date = input("Due Date: ")
                if self.weight == "":
                    self.weight = input("Category Weight: ")
                if self.importance == "":
                    self.importance = input("Importance (0-3):  ")
