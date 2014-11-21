"""

File Name: class_scedule.py
Developer: Justin A. Shores
Date Last Modified: Thu Nov 20 16:56:17 PST 2014
Description: Design a schedule class for classes that a student (you!) 
                take during a semester.

"""
# Course class is object containing all information for single course
class Course(object):
    # initialize the course
    def __init__(self, course_name='', days='', time=0):
        self.course_name_str = course_name
        self.days_str = days
        self.time_int = time
    # update course info
    def update(self, course_name='', days='', time=0):
        if first:
            self.course_name_str = course_name
        if last:
            self.days__str = days
        if time:
            self.time_int = time  
    # print the course info
    def __str__(self):
        return "Course: {:<12} | Days: {:<12} | Time: {:<12}".\
            format(self.course_name_str, self.days_str, self.time_int)

# Schedule class creates/edits a course shedule
class Schedule(object):
    # initialize schedule
    def __init__(self, course_list = []):
        self.schedule = course_list
    # add items to schedule
    def add_course(self, course):
        self.schedule.append(course)
        self.schedule.sort(key=lambda course: course.course_name_str, 
                reverse=False)
    # remove items from schedule
    def remove_course(self, course_name):
        for course in self.schedule:
            if course_name == course.course_name_str:
                self.schedule.remove(course)
                print("\nThe Course '{}' was successfully removed " \
                     "from your schedule".format(course_name))
                return
        print("\nThe Course '{}' could not removed from your schedule, " \
                "the course does not exist".format(course_name))
        return
    # print the object
    def __str__(self):
        print("\nYour class schedule is as follows:\n")
        for course in self.schedule:
            print(course)
        return "\n"

# test getting course information
def add_course_info(schedule):
    while True:
        course = input("Enter course name: ")
        days = input("Enter days of the week the course meets: ")
        time = input("Enter the time of day the course meets: ")
        course_info = Course(course, days, time)
        schedule.add_course(course_info)
        print(schedule)
        valid_add = False
        while valid_add == False:
            add_course = input("Would you like to add another course?" \
                     " (y or n): ")
            if add_course != 'y' and add_course != 'Y' \
                    and add_course != 'n' and add_course != 'N':
                print("Invalid Entry!")
            else:
                valid_add = True
        if add_course == 'y' or add_course == 'Y':
            continue
        else:
            break

# test the removal of course info
def remove_course_info(schedule):
    while True:
        removed_course = input("Enter the name of the course to remove: ")
        schedule.remove_course(removed_course)
        print(schedule)
        valid_remove = False
        while valid_remove == False:
            remove_another = input("Remove another course? (y or n): ")
            if remove_another != 'y' and remove_another != 'Y' \
                    and remove_another != 'n' and remove_another != 'N':
                print("Invalid Entry!")
            else:
                valid_remove = True
        if remove_another == 'y' or remove_another == 'Y':
            continue
        else:
            break

# define the main to test the class
def run_test(schedule):
    # test start with empty schedule so first we need to add
    add_course_info(schedule)
    # test other functions of schedule class
    while True:
        action = input("What would you like to do now?\nEnter 1 to" \
            " remove course, \nEnter 2 to add another course, \nEnter" \
            " 3 to quit: ")
        if action == "1":
            remove_course_info(schedule)
            continue
        elif action == "2":
            add_course_info(schedule)
            continue
        elif action == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Entry")
            continue

# run test program
my_schedule = Schedule()
run_test(my_schedule)
