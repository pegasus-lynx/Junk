from classes import *
from database import *

db = Database()
st = System(db)

st.add_department("CSE", "cse@itbhu.ac.in", "csecse")
st.add_department("MNC", "mnc@itbhu.ac.in", "mncmnc")
st.add_student("a", "a@itbhu.ac.in", "asdqwer", 1)
st.add_student("a", "a@itbhu.ac.in", "asdqwer", 0)

print(len(db._tables["student"]))