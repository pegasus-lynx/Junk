from database import *
from classes import *

class Session(object):

    _instance = False
    _user = None
    _database = None
    _run = True

    _methods = dict()
    _global_methods      = {"list": Session._list , "help": Session._help, "exit": Session._exit}


    def __init__(self):
        if self._instance:
            print("Instance is already acctive. Cannot create another instance")
            return

        self._instance = True
        self._database = self.initalize_database()
        self._methods = self._get_method_dicts()

    def login(self, email_id, password):

        user = self._database.find_user_by_email(email_id)
        
        if not user._verify_password(password):
            print("Wrong Password")
            return

        try:
            self._user = self._database.get_user_instance(user.uid, user.role)
        except:
            print("Actual user instance was not instantiated")

    def logout(self):
        _user = None

    def initalize_database(self):
        database = Database()
        return database

    def run(self):
        print("Information System , IIT (BHU)")
        self._help()
        
        while self._run:
            methods = self.get_methods()
            print("> ", sep=" ")
            raw =  input()
            cmd, args = self._parse(raw)
            
            if cmd  in methods:
                self._exec(cmd, args)
            else:
                print("No command '{}' is available.".format(cmd))
            
    def _exec(self, cmd, args):
        method = self._methods[self._user.role][cmd]
        param_names = method.__code__.co_varnames
        params = [self._user]

        nreq_args = len(param_names)-(2 if "database" in param_names else 1)

        if nreq_args != len(args):
            print("Some arguments are missing")
            return

        params.extend(args)

        if "database" in param_names:
            params.append(self._database)

        try:
            method(*args)
        except Exception as e:
            print("Something is wrong with the arguments.")
            print(param_names)

    def _methods(self, include_global=True):

        methods = None

        if self._user is None:
            methods =  []
        else:
            methods = list(self._methods[self._user.role])
        
        if include_global:
            methods.extend(list(self._global_methods.keys))
        
        return methods

    def _save(self):
        pass

    def _help(self):
        print("list : Returns a list of the available methods")
        print("exit : Exits the system")
        print("help : Returns this list")

    def _list(self):
        methods = self._methods()
        print(*methods,"\n",sep="\t")

    def _exit(self):
        self._run = False

    def _parse(self, raw):
        tokens =  raw.split()
        
        cmd = tokens[0]
        args = []

        if len(tokens) > 1:
            args = tokens[1:]

        return (cmd, args)

    def _get_method_dicts(self):
        methods = dict()

        methods[User.STUDENT] = {}
        methods[User.PROFESSOR] = {}
        methods[User.DEPARTMENT] = {}
        methods[User.INSTITUTE] = {}

        return methods