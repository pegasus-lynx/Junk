from classes import *
from database import *

db = Database()
st = System(db)

st.add_institute()

st.add_hostel("ASN", 350)
st.add_hostel("DG", 400)

st.add_student("a", "a@itbhu.ac.in", "asdqwer", 1)
st.add_student("a", "b@itbhu.ac.in", "asdqwer", 0)

st.add_department("CSE", "cse@itbhu.ac.in", "csecse")
st.add_department("MNC", "mnc@itbhu.ac.in", "mncmnc")

st.add_professor("p", "p@itbhu.ac.in", "123qwe", 0)
st.add_professor("q", "q@itbhu.ac.in", "qwessd", 1)

st.add_course(0, "Intro to C", 1)
st.add_course(1, "Operating System", 0, 0)

timings = [(10,11), (0,0), (0,0), (11,12), (11, 12)]
timingsw = [(11,12), (0,0), (0,0), (10,11), (10, 11)]
st.add_classes(0,0, timings)
st.add_classes(0,1, timings)
st.add_classes(1,0, timingsw)

print(len(db._tables["institute"]) == 1)
print(len(db._tables["department"]) == 2)
print(len(db._tables["hostel"]) == 2)
print(len(db._tables["professor"]) == 2)
print(len(db._tables["student"]) == 2)
print(len(db._tables["course"]) == 2)
print(len(db._tables["classes"]) == 3)