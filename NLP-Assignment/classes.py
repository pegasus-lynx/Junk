
# Classes for Interaction




class User(object):
    
    user_ids = 0

    STUDENT   = 3
    PROFESSOR = 2
    DEPARTMENT = 1
    INSTITUTE = 0    
    
    def __init__(self, name, email_id, password, role):
        
        self.uid = self.user_ids
        self.user_ids += 1
        
        self.name = name
        self.email_id = email_id
        self.password = password
        self.dob = None

        self.role = self.STUDENT

    def _verify_password(self, password):
        print("Works")
        if self.password == password:
            return True

    def get_pk(self):
        return self.uid



class Student(User):

    student_ids = 0

    def __init__(self, name, email_id, password):
        super(Student, self).__init__(name, email_id, password, self.STUDENT)
        self.sid = self.student_ids
        self.student_ids += 1

        self.dept = None
        self.classes = []

    def get_result(self, sem, database):        
        if not self.is_registered(sem, database):
            print("Missed student registration.")
        elif not self.is_course_registerd(sem, database):
            print("Missed course registration.")
        else:
            print("Result available")

    def get_courses(self, database):
        return [ database["classes"][x].course_id for x in self.classes]

    def course_registration(self):
        pass

    def register(self, database):
        pass

    def get_exam_schedule(self):
        pass

    def get_time_table(self):
        pass

    def is_registered(self, sem, database):
        pass

    def is_course_registered(self, sem, database):
        pass

    def get_pk(self):
        return self.sid


class Professor(User):

    professor_ids = 0

    def __init__(self, name, email_id, password):
        super(Professor, self).__init__(name, email_id, password, self.PROFESSOR)
        self.pid = self.professor_ids
        self.professor_ids += 1

        self.dept = None

    def update_result(self):
        pass

    def get_time_table(self):
        pass

    def get_courses(self):
        pass

    def get_classes(self):
        pass

    def get_pk(self):
        return self.pid


class Institute(User):

    _instance = False

    def __init__(self):

        if self._instance:
            print("There is already an instance. Another cannot be created.")
            return

        super(Institute, self).__init__("IIT(BHU)", "official@iitbhu.ac.in", "######", self.INSTITUTE)
        self._instance = True

    def prepare_exam_schedule(self):
        pass

    def prepare_time_table(self):
        pass

    def get_pk(self):
        return 0

class Department(User):
    
    dept_ids = 0
    
    def __init__(self, name, email, password):
        super(Department, self).__init__(name, email, password, self.DEPARTMENT)
        self.did = self.dept_ids
        self.dept_ids += 1

        self.name = ""
        self.hod  = None
        self.phone = phone

    def make_hod(self, prof_id):
        self.hod = prof_id

    def student_register(self, sid):
        pass

    def prepare_time_table(self):
        pass

    def verify_student(self, student):
        pass

    def prepare_exam_schedule(self):
        pass

    def get_pk(self):
        return self.did



class Course(object):
    
    def __init__(self, course_id, name, managed, dept_id):
        self.cid = course_id
        self.name = name

        self.offered_by = self.INSTITUTE
        self.dept = None

        if dept:
            self.offered_by = self.DEPARTMENT
            self.dept = dept_id
        
        
        self.semester = None
        self.credits  = None
        self.convenor = None

    def set_convenor(self, prof_id):
        self.convenor = prof_id
        
    def get_convenor(self, database):
        return database["professors"][self.convenor].name

    def get_students(self, database):
        pass

    def add_students(self, database, sid_list):
        pass

    def add_student(self, database, sid):
        pass

    def get_pk(self):
        return self.cid


class Classes(object):
    
    class_ids = 0

    def __init__(self, course_id, prof_id):
        self.clid = self.class_ids
        self.class_ids += 1
        
        self.course_id = course_id
        self.prof_id = prof_id
        self.timings = []
        self.strength = 0

    def set_timings(self, timings):
        self.timings = timings

    def get_timings(self):
        return self.timings

    def get_students(self, database):
        pass

    def get_prof(self, database):
        return database["professors"][self.prof_id].name

    def get_pk(self):
        return self.clid

class Hostel(object):
    
    hostel_ids = 0

    def __init__(self, hostel_name, capacity):
        self.hid  = self.hostel_ids
        self.hostel_ids += 1

        self.name = hostel_name
        self.capacity = capacity
        self.left = capacity 
        
        self.warden = None

    def set_warden(self, prof):
        self.warden = prof.pid

    def get_warden(self, database):
        return database["professors"][self.prof_id].name

    def get_students(self, database):
        return database.get_students_hostel_id(self.hid)

    def check_availability(self):        
        return True if self.left>0 else False

    def allot_room(self, sid):        
        if self.check_availability():
            database["students"][sid].hostel = self.hid
            self.left -= 1

    def get_pk(self):
        return self.hid

#  Classes for Storage

class Record(object):
    
    record_ids = 0

    def __init__(self, student_id, sem):
        self.rid = self.record_ids
        self.record_ids += 1

        self.sid  = student_id
        self.time = None
        self.sem  = sem
        self.verified = False

    def is_verified(self):
        return self.verified

    def verify(self):
        self.verified = True

    def get_pk(self):
        return self.rid

class StudentRegistration(Record):
    
    student_reg_ids = 0

    def __init__(self, student_id, sem, fees):
        super(Record, self).__init__(student_id, sem)
        self.fee_detail = fees

        self.srid = self.student_reg_ids
        self.student_reg_ids += 1

    def verify(self, database):
        pass  

    def get_pk(self):
        return self.srid
        

class CourseRegistration(Record):

    course_reg_ids = 0
    
    def __init__(self, student_id, sem, course_ids):
        super(CourseRegistration, self).__init__(student_id, sem)
        self.course_ids = course_ids

        self.crid = self.course_reg_ids
        self.course_reg_ids += 1

    def is_complete(self):
        return self.is_verified()

    def verify(self, database):
        pass

    def get_pk(self):
        return self.crid
