import csv
from zipfile import ZipFile
import os
from shutil import rmtree
import re as re

file_pref = None
# file_name = None

print("Enter pref file")
file_pref=input()
# print("Enter name file")
# file_name=input()

# roll_name = {}

# with open(file_name, 'r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         roll_name[row[1]] = row[2]+" "+row[3]+" "+row[4]
 
head=0
head_list = []
pref_dict = []

with open(file_pref,'r') as file:
    reader=csv.reader(file)
    for row in reader:
        if head==0:
            head+=1
            head_list=row
            continue
        
        pref_dict.append([row[0], row[3]])
        # pref_dict[-1].append(roll_name[row[0]])

        temp = []
        for i in range(5,len(row)):
            if re.match(r'^[0-9]+ \(Yes\)$',row[i]):
                temp.append((int(row[i].split()[0]),head_list[i]))
                

        temp.sort()

        for c in temp:
            pref_dict[-1].append(c[1])

with open('pref_list.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in pref_dict:
        writer.writerow(row)

print('Done!')






# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# with ZipFile(zip_name,'r') as zipped:
#     zipped.extractall(path='temp')
 
# all_resumes = [x for x in os.listdir('temp')]
 
# with ZipFile('new_resumes.zip','w') as newzipped:
#     with ZipFile('resumes_removed.zip','w') as zipped_removed:
#         for file in all_resumes:
#             flag=0
#             for number in rolls:
#                 if re.search(f"^{number}",file):
#                     flag=1
#                     break
#             if not flag:
#                 newzipped.write('temp/'+file)
#             else:
#                 zipped_removed.write('temp/'+file)
       
# rmtree('temp')
# print("Done!")