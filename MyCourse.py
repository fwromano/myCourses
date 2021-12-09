from MyCourseParent import *
from Course import *
import pickle as p


class MyCourses(MyCourseParent):

    def __init__(self, name):
        MyCourseParent.__init__(self, name, self.__class__.__name__)
        self.name = name
        self.courses = []
        self.save()

    def save(self):
        pickle = open(self.name + ".pkl", 'wb')
        p.dump(self, pickle)
        pickle.close()

    def add_items(self):
        if len(self.sub_items) == 0:
            print(f"No Courses defined. Please specify one.\n")
            new_item = Course(input(f"Course:"))
            self.sub_items.append(new_item)
        else:
            if yes(f"Add new {Course}?"):
                func = Course
                new_item = func(input(f"{Course}:"))
                self.sub_items.append(new_item)
                # self.sub_items.append(getattr(self, Course)(input(f"{Course}:")))
        if Course.subtype is not None and yes(f"Add new {Course.subtype}?"):
            select(Course, self.sub_items, "add_items")