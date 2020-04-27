import csv
import os
import  nltk
import string
from nltk.corpus import remove_stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

files = []

def remove_punc(text):
    no_punc = "".join([c for c in  text if c not in string.punctuation])
    return no_punc

with open("/home/parzival/Documents/Sem6/IR/Ass2/data/docs.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader :
        for file in row:
            if file is not '':
                if file[0] == ' ':
                    files.append(file[1:])
                else:
                    files.append(file)

clean_data_path = "/home/parzival/Documents/Sem6/IR/Ass2/data/clean/"
processed_data_path = "/home/parzival/Documents/Sem6/IR/Ass2/data/processed/"

cnt=0

for file in files:
    clean_file = open(clean_data_path + file, 'r')
    processed_file = open(processed_data_path + file, 'w')

    text_list = clean_file.read().split("\n")
    no_punc_text_list = []

    for line in text_list:
        line_p = remove_punc(line)
        line_ps = remove_stopwords(line_p)



    # print(no_punc_text_list)
    # cnt=1
    # break


def preprocess(doc):
    stemmer = PorterStemmer()
    tokens = word_tokenize(doc)
    tokens = [w.lower() for w in tokens]

    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    words = [word for word in words if not word in stop_words]
    words = [stemmer.stem(word) for word in words]

    return words