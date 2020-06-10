
# Classes for object creation and storage in database

class System(object):
    
    _instance = False
    _database = None
    
    def __init__(self, database):
        if self._instance:
            print("Cannot instantiate again")
        
        self._database = database
        self._instance = True

    def add_student(self, name, email_id, password, dept_id):
        
        if not self._database.exists("department", dept_id):
            print("Department does not exist.")
            return False

        emails = [x.email_id for x in self._database._tables["user"].values()]
        if email_id in emails:
            print("Email-Id already exists.")
            return False

        student = Student(name, email_id, password, dept_id)
        user = User(name, email_id, password, User.STUDENT)
        user.uid = student.uid

        if self._database.can_add("user", user.uid) and self._database.can_add("student", student.sid):
            self._database.add("user", user)
            self._database.add("student", student)
            return True
        return False

    def add_professor(self, name, email_id, password, dept_id):

        if not self._database.exists("department", dept_id):
            print("Department does not exist.")
            return False

        emails = [x.email_id for x in self._database._tables["user"].values()]
        if email_id in emails:
            print("Email-Id already exists.")
            return False

        professor = Professor(name, email_id, password, dept_id)
        user = User(name, email_id, password, User.PROFESSOR)
        user.uid = professor.uid

        if self._database.can_add("user", user.uid) and self._database.can_add("professor", professor.pid):
            self._database.add("user", user)
            self._database.add("professor", professor)
            return True

        return False

    def add_course(self, course_id, name, term, dept_id=None, convenor=None):
        cids = list(self._database._tables["course"].keys()) 
        if course_id in cids:
            print("Course ID already exsits")
            return False

        if convenor is not None:
            if not self._database.exists("professor", convenor):
                print("No such professor")
                return False

        if dept_id is not None:
            if not self._database.exists("department", dept_id):
                print("Department does not exist.")
                return False
            
        course = Course(course_id, name, term, dept_id, convenor)
        if self._database.can_add("course", course.cid):
            self._database.add("course", course)
            return True

        return False

    def add_institute(self):

        if len(self._database._tables["institute"].keys()) > 0:
            print("Cannot instantiate Institute again.")
            return False

        emails = [x.email_id for x in self._database._tables["user"].values()]

        institute = Institute()

        if institute.email_id in emails:
            print("Email-Id already exists.")
            return False

        user = User(institute.name, institute.email_id, institute.password, User.INSTITUTE)
        user.uid = institute.uid

        if self._database.can_add("user", user.uid) and self._database.can_add("institute", institute.get_pk()):
            self._database.add("user", user)
            self._database.add("institute", institute)
            return True

        return False

    def add_department(self, name, email_id, password):

        emails = [x.email_id for x in self._database._tables["user"].values()]
        if email_id in emails:
            print("Email-Id already exists.")
            return False

        dept = Department(name, email_id, password)
        user = User(name, email_id, password, User.DEPARTMENT)
        user.uid = dept.uid

        if self._database.can_add("user", user.uid) and self._database.can_add("department", dept.did): 
            self._database.add("user", user)
            self._database.add("department", dept)
            return True

        return False

    def add_hostel(self, hostel_name, capacity, warden=None):
        
        if warden is not None:
            if not self._database.exists("professor", warden):
                print("No such professor")
                return False
        
        hostel = Hostel(hostel_name, capacity, warden)

        if self._database.can_add("hostel", hostel.get_pk()):
            self._database.add("hostel", hostel)
            return True

        return False

    def add_classes(self, course_id, prof_id, timings):

        if not self._database.exists("course", course_id):
            print("No such course exists")
            return False

        if not self._database.exists("professor", prof_id):
            print("No such professor exists")
            return False

        course = self._database.find_by_pk("course", course_id)
        prof = self._database.find_by_pk("professor", prof_id)
        
        
        ret = course.add_class(self._database, prof, timings)
        if not ret:
            print("Class can not be added. Timngs clash.")
            return False
    
        self._database.update("course", course)
        return True

class User(object):
    
    _user_ids = 0
    _table_name = "user"

    STUDENT   = 3
    PROFESSOR = 2
    DEPARTMENT = 1
    INSTITUTE = 0    
    
    def __init__(self, name, email_id, password, role):
        
        self.uid = User._user_ids
        User._user_ids += 1
        
        self.name = name
        self.email_id = email_id
        self.password = password
        self.dob = None

        self.role = self.STUDENT

    def _verify_password(self, password):
        if self.password == password:
            return True
        return False

    def change_password(self, database, old_password, new_password):
        if not self._verify_password(old_password):
            print("The old password is incorrect.")
            return False
        
        if len(new_password) < 4:
            print("Password to small. Cannot be changed.")
            return False

        ret = None
        try:
            self.password = new_password
            ret = database.update("user", self)
        except Exception as e:
            print("The operation ended abruptly.")
            self.password = old_password
            ret = False

        return ret

    
    def get_pk(self):
        return self.uid

class Student(User):

    _student_ids = 0

    def __init__(self, name, email_id, password, dept_id):
        super(Student, self).__init__(name, email_id, password, self.STUDENT)
        self.sid = Student._student_ids
        Student._student_ids += 1

        self.dept = dept_id
        self.hostel = None
        self.classes = []

    def get_result(self, database, sem=None):

        if sem is None:
            print("Please enter your sem (1-10) : ")
            raw = input()

            try:
                sem = int(raw)
            except ValueError as e:
                print(" 'sem' must be an integer between 1-10 ")
                return


        if not self.is_registered(sem, database):
            print("Missed student registration.")
        elif not self.is_course_registerd(sem, database):
            print("Missed course registration.")
        else:
            print("Result available")

    def get_courses(self, database):
        courses = set()

        for clid in self.classes:
            obj = database._tables["classes"][clid]
            courses.add(obj.course_id)

        courses = list(courses)
        names = [database._tables["course"][x].name for x in courses]

        print(names)
        return names

    def course_registration(self, database, sem, course_ids):

        flag = True
        for pk in course_ids:
            if not database.exists("course", pk):
                flag = False
                break

        if not flag:
            print("All courses not available.")
            return False

        creg = CourseRegistration(self.sid, sem, course_ids)
        ret = database.add("course_reg", creg)
        return ret


    def register(self, database, sem, fees_detail):

        if len(fees_detail) != 10 and not fees_detail.startswith("DU"):
            return False

        reg = StudentRegistration(self.sid, sem, fees_detail)
        ret = database.add("student_reg", reg)
        return ret

    def is_registered(self, database, sem):
        flag = False
        for pk, obj in database._tables["student_reg"].values:
            if obj.sem == sem and obj.sid == self.sid:
                if obj.verified == 1:
                    flag = True
        return flag

    def is_course_registered(self, database, sem):
        flag = False
        for pk, obj in database._tables["course_reg"].values():
            if obj.sem == sem and obj.sid == self.sid:
                if obj.verified == 1:
                    flag = True
        return flag  

    def get_pk(self):
        return self.sid

    def get_time_table(self, database):
        time_table = dict()
        days_list = ["Mon", "Tue", "Wed", "Thu", "Fri"]

        for day in days_list:
            time_table[day] = []

        for clid in self.classes:
            obj = database.find_by_pk("classes", clid)
            course = database.find_by_pk("course", obj.course_id)

            for i in range(len(obj.timings)):
                if obj.timings[i][0] != 0:
                    time_table[days_list[i]].append({"name":course.name, "class_id":clid, "time":obj.timings[i]})

        for day in days_list:
            print(day, " : ", time_table[day])

        return time_table

class Professor(User):

    _professor_ids = 0

    def __init__(self, name, email_id, password, dept_id):
        super(Professor, self).__init__(name, email_id, password, self.PROFESSOR)
        self.pid = Professor._professor_ids
        Professor._professor_ids += 1

        self.dept = dept_id
        self.classes = []

    def get_time_table(self, database):
        time_table = dict()
        days_list = ["Mon", "Tue", "Wed", "Thu", "Fri"]

        for day in days_list:
            time_table[day] = []

        for clid in self.classes:
            obj = database.find_by_pk("classes", clid)
            course = database.find_by_pk("course", obj.course_id)

            for i in range(len(obj.timings)):
                if obj.timings[i][0] != 0:
                    time_table[days_list[i]].append({"name":course.name, "class_id":clid, "time":obj.timings[i]})

        for day in days_list:
            print(day, " : ", time_table[day])

        return time_table

    def get_courses(self, database):
        courses = set()

        for clid in self.classes:
            obj = database._tables["classes"][clid]
            courses.add(obj.course_id)

        courses = list(courses)
        names = [database._tables["course"][x].name for x in courses]

        print(names)
        return names

    def get_classes(self, database):
        courses = []

        for clid in self.classes:
            obj = database._tables["classes"][clid]
            courses.append(obj.course_id)

        names = [database._tables["course"][x].name for x in courses]

        classes = zip(self.classes, names)

        print(classes)
        return classes

    def get_pk(self):
        return self.pid

# Course registration verification can be given to this
class Institute(User):

    _instance = False

    def __init__(self):

        if self._instance:
            print("There is already an instance. Another cannot be created.")
            return

        super(Institute, self).__init__("IIT(BHU)", "official@iitbhu.ac.in", "######", self.INSTITUTE)
        self._instance = True

    def allot_hostels(self, database):
        hostels = list(database._tables["hostel"].values())
        students = list(database._tables["student"].values())

        nh = len(hostels)
        ch = 0
        p  = 0

        assigned = [False] * len(students)


        for student in students:
            if student.hostel is None:
                while ch < nh:
                    if hostels[ch].left > 0:
                        hostels[ch].assign_room(student)
                        assigned[p] = True
                        break
                    else:
                        ch += 1
            else:
                assigned[p] = True
            
            p += 1

        database.update_batch("student", students)
        database.update_batch("hostel", hostels)        

    def verify_course_registrations(self, database):
        students = []
        courses = []
        course_regs = list(database._tables["course_reg"].values())

        regs = [x for x in course_regs if x.verifed == 0]

        for reg in regs:
            valid = True

            courses = []
            for cid in reg.course_ids:
                course = database.find_by_pk("course", cid)
                courses.append(course)
                if reg.sem % 2 != course.term:
                    valid = False

            if not valid:
                reg.verified = Record.FAILED
            else:
                reg.verified = Record.PASSED
                student = database.find_by_pk("student", reg.sid)
                for course in courses:
                    student.classes.append(course.classes[0])
                database.update("student", student)

        database.update_batch("course_reg", regs)

            

    def get_pk(self):
        return 0

# Register students left
class Department(User):
    
    _dept_ids = 0
    
    def __init__(self, name, email_id, password):
        super(Department, self).__init__(name, email_id, password, self.DEPARTMENT)
        self.did = Department._dept_ids
        Department._dept_ids += 1

        print(self.did, self._dept_ids)

        self.name = ""
        self.hod  = None
        self.phone = None

    def set_hod(self, database, prof):
        if not database.exists("professor", prof.get_pk()):
            print("Professor not in database.")
            return False

        if self.did != prof.dept:
            print("Professor is not of the same department")
            return False

        self.hod = prof.pid
        return True

    def get_hod(self, database):
        if self.hod:
            return database._tables["professor"][self.hod].name
        return None

    def verify_student_registrations(self, database):
        student_regs = list(database._tables["student_reg"].values())
        regs = [x for x in student_regs if x.verifed == 0]

        for reg in regs:
            if reg.fees is not None:
                reg.verified = Record.PASSED

        database.update_batch("student_reg", regs)


    def get_pk(self):
        return self.did


class Course(object):

    INSTITUTE = 0
    DEPARTMENT = 1
    
    def __init__(self, course_id, name, term, dept_id=None, convenor=None):
        self.cid = course_id
        self.name = name
        self.term = term

        self.offered_by = self.INSTITUTE
        self.dept = None

        if dept_id is not None:
            self.offered_by = self.DEPARTMENT
            self.dept = dept_id
                
        self.credits  = None
        self.convenor = convenor

        self.classes = []

    def add_class(self, database, prof, timings):
        cclass = Classes(self.cid, prof.pid, timings)
        database.add("classes", cclass)
        self.classes.append(cclass.clid)

    def set_convenor(self, database, prof):
        if not database.exists("professor", prof.get_pk()):
            print("Professor not in database.")
            return False


        if self.dept is not None:
            if self.dept != prof.dept:
                print("Professor is not in the same department")
                return False

        self.convenor = prof.pid
        database.update("course", self)
        return True
        
    def get_convenor(self, database):
        if self.convenor:
            return database._tables["professor"][self.convenor].name
        return None

    def get_students(self, database):
        students = []

        for clid in self.classes:
            students.extend(database._tables["classes"][clid].get_students(database))

        return students

    def get_pk(self):
        return self.cid


class Classes(object):
    
    _class_ids = 0

    def __init__(self, course_id, prof_id, timings=None):
        self.clid = Classes._class_ids
        Classes._class_ids += 1
        
        self.course_id = course_id
        self.prof = prof_id
        self.timings = []
        self.strength = 0

        if timings is not None:
            self.timings = timings

    def set_timings(self, database, timings):

        if len(timings) != 5:
            print("Must be a list of len 5")
            return False

        valid = True
        for val in timings:
            if val[0] == val[1] and val[0] != 0:
                valid = False
                break

        if not valid:
            print("For no class the tuple should be '(0,0)'")
            return False

        self.timings = timings
        return True

    def get_timings(self):
        return self.timings

    def add_student(self, database, sid):

        if not database.exists("student", sid):
            print("Student not in database")
            return False

        student = database.find_by_pk("student",sid)

        if student is None:
            print("Student {} not found".format(sid))
            return False

        self.strength += 1
        student.classes.append(self.clid)
        database.update(self, "student", student)
        return True

    def add_students(self, database, sids):
        added = []
        for sid in sids:
            added.append(self.add_student(database, sid))
        return added

    def get_students(self, database):
        students = []

        for obj in database._tables["student"].values():
            if self.clid in obj.classes:
                students.append(obj.name)

        return students

    def get_prof(self, database):
        return database._tables["professor"][self.prof].name

    def get_pk(self):
        return self.clid


class Hostel(object):
    
    _hostel_ids = 0

    def __init__(self, hostel_name, capacity, warden=None):
        self.hid  = Hostel._hostel_ids
        Hostel._hostel_ids += 1

        self.name = hostel_name
        self.capacity = capacity
        self.left = capacity 
        
        self.warden = warden

    def set_warden(self, database, prof):
        if not database.exists("professor", prof.get_pk()):
            print("Professor not in database.")
            return False

        self.warden = prof.pid
        return True

    def get_warden(self, database):
        if self.warden:
            return database._tables["professor"][self.warden].name

    def get_students(self, database):
        students = []

        for obj in database._tables["student"].values():
            if obj.hostel == self.hid:
                students.append(obj.name)

        return students

    def check_availability(self):        
        return True if self.left>0 else False

    def assign_room(self, student):        
        self.left -= 1
        student.hostel = self.hid

    def get_pk(self):
        return self.hid

#  Classes for Storage

class Record(object):
    
    _record_ids = 0

    PASSED = 1
    UNVERIFIED = 0
    FAILED = -1

    def __init__(self, student_id, sem):
        self.rid = Record._record_ids
        Record._record_ids += 1

        self.sid  = student_id
        self.time = None
        self.sem  = sem
        self.verified = self.UNVERIFIED

    def is_verified(self):
        return self.verified

    def get_pk(self):
        return self.rid

class StudentRegistration(Record):
    
    _student_reg_ids = 0

    def __init__(self, student_id, sem, fees):
        super(Record, self).__init__(student_id, sem)
        self.fee_detail = fees
        self.verified = True

        self.srid = StudentRegistration._student_reg_ids
        StudentRegistration._student_reg_ids += 1

    def get_pk(self):
        return self.srid
        

class CourseRegistration(Record):

    _course_reg_ids = 0
    
    def __init__(self, student_id, sem, course_ids):
        super(CourseRegistration, self).__init__(student_id, sem)
        self.course_ids = course_ids

        self.crid = CourseRegistration._course_reg_ids
        CourseRegistration._course_reg_ids += 1

    def is_complete(self):
        return self.is_verified()

    def get_pk(self):
        return self.crid
