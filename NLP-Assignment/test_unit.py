import unittest
import pytest

from classes import *
from database import Database

import fixtures

class TestSystem(unittest.TestCase):
    db = Database()
    st = System(db)

    table_names = db._table_names
    table_sizes = {
        "institute" : 1, "department" : 2,
        "student" : 2, "professor" : 2,
        "course" : 2, "classes" : 3,
        "hostel" : 2, "user": 7,
        "record" : 0,
        "student_reg" : 0,
        "course_reg" : 0
    }

    def test_user_with_same_email(self):
        fixtures.add_same_emails(self.st)
        l = len(self.db._tables["student"].keys())
        self.db.clear()
        self.assertEqual(l, 1)

    def test_correct_instantiation(self):
        fixtures.correct_instantiation(self.st)

        valid = True
        for name in self.table_names:
            if len(self.db._tables[name]) != self.table_sizes[name]:
                valid = False
                break

        self.db.clear()
        self.assertTrue(valid)

    def test_create_student_before_dept(self):
        fixtures.false_instantiation(self.st, "student")

        valid = True

        for name in self.table_names:
            if len(self.db._tables[name]) != self.table_sizes[name]:
                valid = False
                break

        self.db.clear()
        self.assertFalse(valid)

    def test_create_professor_before_dept(self):
        fixtures.false_instantiation(self.st, "professor")

        valid = True

        for name in self.table_names:
            if len(self.db._tables[name]) != self.table_sizes[name]:
                valid = False
                break

        self.db.clear()
        self.assertFalse(valid)

    def test_multiple_institute(self):
        self.st.add_institute()
        self.st.add_institute()
        l = len(self.db._tables["institute"].keys())

        self.db.clear()
        self.assertEqual(l, 1)


class TestUser(unittest.TestCase):
    db = Database()
    st = System(db)

    def test_new_user_change_password_not_in_database(self):
        user = User("Johny", "johny@itbhu.ac.in", "johny123", User.STUDENT)
        test1 = user.change_password(self.db, "johny123", "johny@123")
        test2 = user._verify_password("johny123")
        self.assertFalse(test1 or not test2)


    def test_new_user_change_password_in_database(self):
        user = User("John", "john@itbhu.ac.in", "john123", User.STUDENT)
        # test1 = user.change_password(self.db, "john123", "john@123")
        # test2 = (user._verify_password("john123"))

        self.db.add("user", user)
        test3 = user.change_password(self.db, "john123", "john@123")

        self.assertTrue(test3)


class TestStudent(unittest.TestCase):
    db = Database()
    st = System(db)

    def test_course_registration_pass(self):
        fixtures.correct_instantiation(self.st)
        students = list(self.db._tables["student"].values())

        ret1 = students[0].course_registration(self.db, 2, [0,1])    

        self.db.clear()
        self.assertTrue(ret1)        

    def test_course_registration_fail(self):
        fixtures.correct_instantiation(self.st)
        students = list(self.db._tables["student"].values())

        ret2 = students[1].course_registration(self.db, 2, [0,2])    

        self.db.clear()
        self.assertFalse(ret2)        


    def test_student_registration_pass(self):
        fixtures.correct_instantiation(self.st)
        depts = list(self.db._tables["department"].values())
        students = list(self.db._tables["student"].values())

        ret1 = students[0].register(self.db, 2, "DU14012341")    
        # ret2 = students[1].register(self.db, 2, "")    

        self.assertTrue(ret1)
        
        # self.assertFalse(ret2)

    def test_student_registration_fail(self):
        fixtures.correct_instantiation(self.st)
        depts = list(self.db._tables["department"].values())
        students = list(self.db._tables["student"].values())

        # ret1 = students[0].register(self.db, 2, "DU14012341")    
        ret2 = students[1].register(self.db, 2, "")    

        # self.assertTrue(ret1)
        
        self.assertFalse(ret2)


class TestHostel(unittest.TestCase):
    db = Database()
    st = System(db)

    def setUp(self):
        fixtures.correct_instantiation(self.st)        

    def test_warden_property(self):
        hostels = list(self.db._tables["hostel"].values())
        profs = list(self.db._tables["professor"].values())
        
        self.assertTrue(hostels[0].set_warden(self.db, profs[0]))

    # def test_assign_room_method(self):
    #     hostel = self.db.find_by_pk("hostel", 0)
    #     student = self.db.find_by_pk("student", 0)
    

class TestDepartment(unittest.TestCase):
    db = Database()
    st = System(db)

    def setUp(self):
        fixtures.correct_instantiation(self.st)

    def test_set_hod_property(self):
        depts = list(self.db._tables["department"].values())
        profs = list(self.db._tables["professor"].values())
        
        self.assertTrue(depts[0].set_hod(self.db, profs[0]))

    def test_verify_student_registration_pass(self):
        depts = list(self.db._tables["department"].values())
        students = list(self.db._tables["student"].values())

        ret1 = students[0].register(self.db, 2, "DU14012341")    
        # ret2 = students[1].register(self.db, 2, "")    

        for dept in depts:
            dept.verify_student_registrations(self.db)
        
        students = list(self.db._tables["student"].values())

        self.assertTrue(students[0].is_registered(self.db, 2))
    
    def test_verify_student_registration_fail(self):
        depts = list(self.db._tables["department"].values())
        students = list(self.db._tables["student"].values())

        # ret1 = students[0].register(self.db, 2, "DU14012341")    
        ret2 = students[1].register(self.db, 2, "")    

        for dept in depts:
            dept.verify_student_registrations(self.db)
        
        students = list(self.db._tables["student"].values())

        self.assertFalse(students[1].is_registered(self.db, 2))



class TestInstitute(unittest.TestCase):
    db = Database()
    st = System(db)

    def setUp(self):
        fixtures.correct_instantiation(self.st)

    def test_allot_hostel(self):
        ins = self.db.find_by_pk("institute", 0)
        ins.allot_hostels(self.db)

        students = list(self.db._tables["student"].values())

        valid = True

        for student in students:
            if student.hostel is None:
                valid = False
                break

        self.assertTrue(valid)

    def test_verify_course_registration_pass(self):
        ins = self.db.find_by_pk("institute", 0)
        students = list(self.db._tables["student"].values())

        ret1 = students[0].course_registration(self.db, 2, [0,1])    
        # ret2 = students[1].course_registration(self.db, 2, [0,2])    

        self.assertTrue(ret1)
            
    def test_verify_course_registration_fail(self):
        ins = self.db.find_by_pk("institute", 0)
        students = list(self.db._tables["student"].values())

        # ret1 = students[0].course_registration(self.db, 2, [0,1])    
        ret2 = students[1].course_registration(self.db, 2, [0,2])    

        self.assertFalse(ret2)

    def test_verify_course_registration(self):
        ins = self.db.find_by_pk("institute", 0)
        students = list(self.db._tables["student"].values())

        ret1 = students[0].course_registration(self.db, 2, [0,1])    

        ins.verify_course_registrations(self.db)
        students = list(self.db._tables["student"].values())

        self.assertTrue(students[0].is_course_registered(self.db, 2))

class TestCourse(unittest.TestCase):
    db = Database()
    st = System(db)

    def setUp(self):
        fixtures.correct_instantiation(self.st)

    def test_set_convenor_property(self):
        courses = list(self.db._tables["course"].values())
        profs = list(self.db._tables["professor"].values())
        
        self.assertTrue(courses[0].set_convenor(self.db, profs[1]))

    def test_class_clash_for_course(self):
        pass
    
class TestClasses(unittest.TestCase):
    db = Database()
    st = System(db)

    def setUp(self):
        fixtures.correct_instantiation(self.st, "notimings")

    # def test_class_clash_for_prof(self):
    #     pass
    
    def test_set_timings_property_pass(self):
        timings = []
        timings.append( [(10,11), (0,0), (0,0), (11,12), (11, 12)] )
        timings.append( [(11,12), (1,1), (0,0), (10,11), (10, 11)] )
        timings.append( [(11,12), (0,0), (10,11), (10, 11)] )

        classes = list(self.db._tables["classes"].values())

        rets = [True, True, True]

        for i in range(3):
            rets[i] = classes[i].set_timings(self.db, timings[i])

        self.assertTrue(rets[0])

    def test_set_timings_property_fail(self):
        timings = []
        timings.append( [(10,11), (0,0), (0,0), (11,12), (11, 12)] )
        timings.append( [(11,12), (1,1), (0,0), (10,11), (10, 11)] )
        timings.append( [(11,12), (0,0), (10,11), (10, 11)] )

        classes = list(self.db._tables["classes"].values())

        rets = [True, True, True]

        for i in range(3):
            rets[i] = classes[i].set_timings(self.db, timings[i])


        self.assertFalse(rets[1] or rets[2])

    def test_add_new_student_pass(self):
        cl = list(self.db._tables["classes"].values())[0]
        student = list(self.db._tables["student"].values())[0]
        ret1 = cl.add_student(self.db, student.sid)

        self.assertTrue(ret1)

    def test_add_new_student_fail(self):
        cl = list(self.db._tables["classes"].values())[0]
        ret2 = cl.add_student(self.db, 2)

        self.assertFalse(ret2)

