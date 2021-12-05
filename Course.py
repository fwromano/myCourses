from MyCourseParent import *
from Assignments import *


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

