
# Classes for Interaction

class User(object):
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email_id = ""
        self.password = ""
        self.dob = None

class Student(User):

    student_id = 0

    def __init__(self):
        super.__init__()
        self.sid = student_id
        student_id += 1

class Professor(User):

    professor_id = 0

    def __init__(self):
        super.__init__()
        self.pid = professor_id
        professor_id += 1


class Institute(User):

    _instance = False

    def __init__(self):

        if Institute._instance:
            print("There is already an instance. Another cannot be created.")
            return

        super.__init__()
        Institute._instance = True


# Classes for Object-Oriented Design
class Department(object):
    pass

class Course(object):
    pass

class Class(object):
    pass

class Hostel(object):
    pass


#  Classes for Storage

class Record(object):
    pass

class StudentRegistration(Record):
    pass

class CourseRegistration(Record):
    pass
