from classes import *

def correct_instantiation(system, param=None):
    _add_institute(system)
    _add_departments(system)
    _add_hostels(system)
    _add_professors(system)
    _add_courses(system)
    _add_students(system)
    if param = "notimimgs":
        _add_classes(system, param)
    else:
        _add_classes(system)

def false_instantiation(system, param):
    _add_institute(system)

    if param == "students":
        _add_students(system)
    else:
        _add_professors(system)

    _add_departments(system)

    if param == "students":
        _add_professors(system)
    else:
        _add_students(system)

    _add_hostels(system)
    _add_courses(system)
    _add_classes(system)

def add_same_emails(system):
    _add_institute(system)
    _add_departments(system)
    _add_students(system)





def _add_students(system, same=False):
    system.add_student("a", "a@itbhu.ac.in", "asdqwer", 1)
    system.add_student("a", ("a@itbhu.ac.in" if same else "b@itbhu.ac.in"), "asdqwer", 0)

def _add_professors(system):
    system.add_professor("p", "p@itbhu.ac.in", "123qwe", 0)
    system.add_professor("q", "q@itbhu.ac.in", "qwessd", 1)

def _add_departments(system):
    system.add_department("CSE", "cse@itbhu.ac.in", "csecse")
    system.add_department("MNC", "mnc@itbhu.ac.in", "mncmnc")

def _add_courses(system):
    system.add_course(0, "Intro to C", 1)
    system.add_course(1, "Operating System", 0, 0)

def _add_classes(system, param = None):
    timings = [(10,11), (0,0), (0,0), (11,12), (11, 12)]
    timingsw = [(11,12), (0,0), (0,0), (10,11), (10, 11)]
    
    if param == "notimings":
        system.add_classes(0,0)
        system.add_classes(0,1)
        system.add_classes(1,0)
    else:
        system.add_classes(0,0, timings)
        system.add_classes(0,1, timings)
        system.add_classes(1,0, timingsw)

def _add_institute(system):
    system.add_institute()

def _add_hostels(system):
    system.add_hostel("ASN", 350)
    system.add_hostel("DG", 400)