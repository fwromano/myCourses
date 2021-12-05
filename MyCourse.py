from MyCourseParent import *
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
