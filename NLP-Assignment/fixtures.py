from classes import *

def correct_instantiation(system, param=None):
    _add_institute(system)
    dept_ids = _add_departments(system)
    _add_hostels(system)
    pids = _add_professors(system, dept_ids)
    cids = _add_courses(system, dept_ids)
    _add_students(system, dept_ids)
    if param == "notimimgs":
        _add_classes(system, cids, pids, param)
    else:
        _add_classes(system, cids, pids)

def false_instantiation(system, param):
    _add_institute(system)

    if param == "students":
        _add_students(system, [-1,-1])
    else:
        pids = _add_professors(system, [-1,-1])

    dept_ids = _add_departments(system)

    if param == "students":
        _add_professors(system, dept_ids)
    else:
        _add_students(system, dept_ids)

    _add_hostels(system)
    cids = _add_courses(system, dept_ids)

def add_same_emails(system):
    _add_institute(system)
    dept_ids = _add_departments(system)
    system.add_student("a", "a@itbhu.ac.in", "asdqwer", dept_ids[0])
    system.add_student("a", "a@itbhu.ac.in", "asdqwer", dept_ids[1])





def _add_students(system, dept_ids, same=False):
    system.add_student("a", "a@itbhu.ac.in", "asdqwer", dept_ids[0])
    system.add_student("a", ("a@itbhu.ac.in" if same else "b@itbhu.ac.in"), "asdqwer", dept_ids[1])

def _add_professors(system, dept_ids):
    system.add_professor("p", "p@itbhu.ac.in", "123qwe", dept_ids[0])
    system.add_professor("q", "q@itbhu.ac.in", "qwessd", dept_ids[1])
    return list(system._database._tables["professor"].keys())


def _add_departments(system):
    system.add_department("CSE", "cse@itbhu.ac.in", "csecse")
    system.add_department("MNC", "mnc@itbhu.ac.in", "mncmnc")
    return list(system._database._tables["department"].keys())

def _add_courses(system, dept_ids):
    system.add_course(0, "Intro to C", 0, dept_ids[1])
    system.add_course(1, "Operating System", 0)
    return list(system._database._tables["course"].keys())

def _add_classes(system, cids, pids, param = None):
    timings = [(10,11), (0,0), (0,0), (11,12), (11, 12)]
    timingsw = [(11,12), (0,0), (0,0), (10,11), (10, 11)]
    
    if param == "notimings":
        system.add_classes(cids[0],pids[0])
        system.add_classes(cids[0],pids[1])
        system.add_classes(cids[1],pids[0])
    else:
        system.add_classes(cids[0],pids[0], timings)
        system.add_classes(cids[0],pids[1], timings)
        system.add_classes(cids[1],pids[0], timingsw)

def _add_institute(system):
    system.add_institute()

def _add_hostels(system):
    system.add_hostel("ASN", 350)
    system.add_hostel("DG", 400)