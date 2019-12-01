import csv
import os
import zipfile as zf
import re
import shutil as shu

rolls = []
delCol = []

print("Enter roll number list file : ")
rollNumberFilePath = input()

with open(rollNumberFilePath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rolls.extend(row)

file.close()

marked = open('rollsMarked.csv', 'w')
unmarked = open('rollsUnmarked.csv', 'w')

mrk = csv.writer(marked)
unmrk = csv.writer(unmarked)

print("Enter the source file path : ")
sourceFilePath = input()

print("Enter the column of roll numbers (1,2,...) : ")
colRoll = int(input())-1

print("Enter the columns to be deleted (ex : 1 2 4 8 ) : ")
delCol = list(map(int, input().split()))

for i in range(len(delCol)):
    delCol[i] -= 1

print(delCol)

with open(sourceFilePath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[colRoll] in rolls:
            mrk.writerow( [ row[i] for i in range(len(row)) if i not in delCol] )
        else:
            unmrk.writerow( [ row[i] for i in range(len(row)) if i not in delCol] )

file.close()

marked.close()
unmarked.close()
