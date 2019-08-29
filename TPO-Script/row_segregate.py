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

marked = file('rollsMarked.csv', 'w')
unmarked = file('rollsUnmarked.csv', 'w')

mrk = csv.writer(marked)
unmrk = csv.writer(unmarked)

print("Enter the source file path : ")
sourceFilePath = input()

print("Enter the column of roll numbers (1,2,...) : ")
colRoll = int(input())-1

print("Enter the columns to be deleted (ex : 1 2 4 8 ) : ")
delCol = map(int, input().split())

for c in delCol:
    c -= 1

with open(sourceFilePath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[colRoll] in rolls:
            mrk.writerow( [ x[i] for i in range(len(row)) if i not in delCol] )
        else:
            unmrk.writerow( [ x[i] for i in range(len(row)) if i not in delCol] )
