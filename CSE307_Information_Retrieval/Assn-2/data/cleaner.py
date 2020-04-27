import csv
import os

files = []

with open("/home/parzival/Documents/Sem6/IR/Ass2/data/docs.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader :
        for file in row:
            if file is not '':
                if file[0] == ' ':
                    files.append(file[1:])
                else:
                    files.append(file)

raw_data_path = "/home/parzival/Documents/Sem6/IR/Ass2/data/raw/"
clean_data_path = "/home/parzival/Documents/Sem6/IR/Ass2/data/clean/"

files[0] = ' ' + files[0]

for file in files:

    print(file)
    
    if file in ['', ' 101596']:
        continue

    if file[0] == ' ':
        doc = file[1:]
    else:
        doc = file

    raw_file = open(raw_data_path + doc, 'r')
    clean_file = open(clean_data_path + doc, 'w')

    text_list = raw_file.readlines()
    flag=False
    for text in text_list:
        if not flag:
            if text == "\n":
                flag = True
            else:
                continue
        else:
            clean_file.write(text)

    raw_file.close()
    clean_file.close()        

        