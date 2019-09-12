import csv
import os
import zipfile as zf
import re
import shutil as shu


rolls = []

print("Enter roll number list file : ")
rollNumberFilePath = input()

with open(rollNumberFilePath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rolls.extend(row)

print("Enter resume zip file path : ")
resumeZipName=input()

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