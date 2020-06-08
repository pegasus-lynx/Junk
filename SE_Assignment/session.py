from database import *
from classes import *

class Session(object):

    _instance = False
    _user = None
    _database = None

    def __init__(self):
        if self._instance:
            print("Instance is already acctive. Cannot create another instance")
            return

        self._instance = True
        self._database = self.initalize_database()

    def login(self, email_id, password):

        user = self._database.find_user_by_email(email_id)
        
        if not user._verify_password(password):
            print("Wrong Password")
            return

        try:
            _user = self._database.get_user_instance(user.uid, user.role)
        except:
            print("Actual user instance was not instantiated")

    def logout(self):
        _user = None

    def initalize_database(self):
        database = Database()
        return database

    def run(self):
        pass

    def menu(self):
        pass

    def get_available_methods(self):
        pass

    def display_available_methods(self, methods):
        pass

    def save_database(self):
        pass