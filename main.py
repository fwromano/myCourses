# import Course as c
# import pickle as p
from MyCourse import *


# class MyCourses:
#
#     def __init__(self, me):
#         self.me = me
#         self.courses = []
#         self.save()
#
#     def add_course(self):
#         new_course = self.Course(input("Course Name:"))
#         self.courses.append(new_course)
#         self.save()
#         print("Course added!")
#
#     # def course_info(self):
#     # if len(self.courses) == 0:
#     #     print("No courses!")
#     #     return
#     #
#     # print("Courses:")
#     # for course in self.courses:
#     #     print("---("+course.course_id+"): "+course.course_name)
#     #
#     # course_name = input("Course ID:")
#     # for course_id, course in self.courses:
#     #     if course_name == course.course_name:
#     #         course.info()
#     #         return course.prompt()
#     #
#     # print("No course of that name.")
#
#     def save(self):
#         pickle = open(self.me + ".pkl", 'wb')
#         p.dump(self, pickle)
#         pickle.close()
#
#     class Course:
#
#         def __init__(self, name):
#             self.name = name
#             self.instructor = "unknown"
#             self.schedule = []
#             self.location = "unknown"
#             self.grade = self.compute_grade()
#             self.grade_categories = []
#             self.add_course_data()
#
#         def info(self):
#             print(self.name + "\n---Grade: " + self.grade + "\n---Instructor: " + self.instructor)
#
#         def prompt(self):
#             action = input("What would you like to do with this course? (type 'help' for actions)\n")
#
#             if action == "help":
#                 print("Add course data\nUpdate course info\nReturn to myCourses")
#                 self.prompt()
#             elif action == "Add course data":
#                 self.add_course_data()
#             elif action == "Update course info":
#                 self.update_course_info()
#             elif action == "Exit":
#                 return False
#             elif action == "Return to myCourses":
#                 return  # to myCourses
#             else:
#                 print("Sorry, that is not one of my available actions.")
#                 self.prompt()
#
#         def add_course_data(self):
#             if len(self.grade_categories) == 0:
#                 print("No grading categories defined. Please specify one.\n")
#                 self.grade_categories.append(self.GradeCategory(input("Category:")))
#             else:
#                 if boolean_input("Add new grading category?"):
#                     self.grade_categories.append(self.GradeCategory(input("Category:")))
#             if boolean_input("Add new assignments?"):
#                 select("Category", self.grade_categories, "add_items")
#
#         def update_course_info(self):
#             self.info()
#             update = input("Please enter label of data being updated")
#             if update not in self.__dict__.keys():
#                 print("Label is not valid.")
#             else:
#                 self.__setattr__(update, input("New value for " + update + ": "))
#             self.prompt()
#
#         def compute_grade(self):
#             # todo
#             return "NA"
#
#         class GradeCategory:
#
#             def __init__(self, name):
#                 self.name = name
#                 self.weight = 0
#                 self.score = self.compute_score()
#                 self.items = []
#
#             def add_grade_category_data(self):
#                 if self.weight == 0:
#                     self.weight = int(input("Course weight of Category: "))
#                 if len(self.items) == 0:
#                     if input("Add Assignments? (y/n): ") == "y":
#                         self.add_items()
#
#             def add_items(self):
#                 #     todo
#                 new_item = self.Items(input("Assignment name: "))
#                 new_item.add_item_info()
#                 self.items.append(new_item)
#                 pass
#
#             def compute_score(self):
#                 # todo
#                 return 0
#
#             class Items:
#                 def __init__(self, name):
#                     self.name = name
#                     self.desc = ""
#                     self.due_date = ""
#                     self.status = "Not Started"
#                     self.weight = 1
#                     self.score = 0
#                     self.importance = 0
#
#                 def add_item_info(self):
#                     if self.desc == "":
#                         self.desc = input("Description: ")
#                     if self.due_date == "":
#                         self.due_date = input("Due Date: ")
#                     if self.weight == "":
#                         self.weight = input("Category Weight: ")
#                     if self.importance == "":
#                         self.importance = input("Importance (0-3):  ")


def action_prompt():
    myCourse.save()
    action = input("How may I assist you? (type 'help' for actions)\n")

    if action == "help":
        print("Add course\nSelect Course\nExit")
    elif action == "Add course":
        myCourse.add_items()
    elif action == "Select course":
        if not select("Course", myCourse.courses, "prompt"):
            return True
    elif action == "Exit":
        myCourse.save()
        print("See you next time!")
        return False
    else:
        print("Sorry, that is not one of my available actions.")
    return True

#
# def boolean_input(prompt):
#     return input(prompt).strip()[0].lower() == "y"
#
#
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


if __name__ == '__main__':
    # print("Hello! Welcome to myCourses. I am here to help you manage and stay on top of all your course work!")
    # name = input("What is your name?\n")
    name = "Franky0"

    try:
        myCourseFile = open(name + ".pkl", "rb")
        myCourse = p.load(myCourseFile)
        myCourseFile.close()
        print("Welcome Back " + name + "!")

    except (OSError, IOError) as e:
        print("Nice to meet you " + name + "\n")
        myCourse = MyCourses(name, "MyCourse", "Course")

    # Daily Report
    # weekly Report

    while True:
        if not myCourse.prompt():
            break
