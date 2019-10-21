import sys
import openpyxl as onyx
import datetime as dt
        
def load(filepath):
    try:
        wb = onyx.load_workbook(filepath)
    except FileNotFoundError as err:
        raise FileNotFoundError

    return wb

def currentWB():
    pass

def currentWS():
    pass

def switchWS():
    pass

def add():
    pass

def delete():
    pass

def update():
    pass

def append():
    pass

def addColumn():
    pass

def printRange():
    pass

def eraseRange():
    pass

def save():
    pass

def saveAs():
    pass