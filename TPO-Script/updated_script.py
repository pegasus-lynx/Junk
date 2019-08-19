import csv
from zipfile import ZipFile
import os
from shutil import rmtree
import re
rolls = None
output_file="result.csv"
file_name=None
col=None
new_rows=[]
zip_name = None
print("Enter roll numbers")
rolls = list(map(int, input().split()))
print("Enter file name")
file_name=input()
print("Which column number has roll numbers")
col = int(input())
print("Enter zip file name")
zip_name=input()

with open(file_name,'r') as file:
    reader=csv.reader(file)
    for row in reader:
        if int(row[col-1]) not in rolls:
            new_rows.append(row)


with open(output_file,'w') as file:
    writer=csv.writer(file)
    writer.writerows(new_rows)

with ZipFile(zip_name,'r') as zipped:
    zipped.extractall(path='temp')

with ZipFile('new_resumes.zip','w') as newzipped:
    for file in os.listdir('temp'):
        flag=0
        for number in rolls:
            if re.search(f"^{number}",file):
                flag=1
                break
        if not flag:
            newzipped.write(file)

        
rmtree('temp')
print("Done!")
