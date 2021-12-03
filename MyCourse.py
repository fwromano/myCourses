from MyCourseParent import *
import pickle as p


class MyCourses(MyCourseParent):

    def __init__(self, name, obj_type, sub_type):
        MyCourseParent.__init__(self, name, obj_type, sub_type)
        self.name = name
        self.courses = []
        self.save()

    def save(self):
        pickle = open(self.name + ".pkl", 'wb')
        p.dump(self, pickle)
        pickle.close()
