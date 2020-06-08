from classes import *

class Database(item):
    
    _instance = False
    _tables = None

    _table_names = ["user", "student", "professor", "department", "institute", 
                    "record", "student_registration", "course_registration"
                    "hostel", "course", "classes"]

    _table_pk_names = {
        "user": "uid", "student": "sid",
        "professor": "pid", "hostel": "hid",
        "institute": "iid", "record": "rid",
        "classes": "clid", "course": "cid",
        "student_registration": "srid",
        "course_registration": "crid",
    }

    def __init__(self):
        if self._instance:
            print("Already an instance. Another cannot be created")

        self._instance = True
        self._tables = self.create_tables()

    def create_tables(self):
        tables = dict()

        for table in table_names:
            tables[table] = dict()

        return tables

    def load(self, filename):
        pass

    def add(self, table, item):
        pk = item.get_pk()

        if not self.can_add(table, pk):
            print("Instance with {} : {} exists".format(
                self._table_pk_names[table], pk))
            return

        self._tables[table][pk] = item

    def update(self, table, item):
        pk = item.get_pk()

        if not self.can_update(table, pk):
            print("Instance with the {} : {} does not exists".format(
                self._table_pk_names[table], pk))
            return

        self._tables[table][pk] = item

    def remove(self, table, item):
        pk = item.get_pk()

        if not self.can_remove(table, pk):
            print("Instance with {} : {} does not exist".format(
                        self._table_pk_names[table], pk))
            return

        del self._tables[table][pk]

    def add_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_add(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} exists".format(
                self._table_pk_names[table], pks[p]))
            return

        for item in items:
            self.add(table, item)

    def update_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_update(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} does not exist".format(
                self._table_pk_names[table], pks[p]))
            return

        for item in items:
            self.update(table, item)

    def remove_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_remove(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} does not exist".format(
                self._table_pk_names[table], pks[p]))
            return

        for item in items:
            self.remove(table, item)

    def find_by_pk(self, table, pk):
        if not self.exists(table, pk):
            print("The object doesn't exist in the database.")
            return

        return self._tables[table][pk]

    def find(self, table, params):
        pass

    def get_students_by_hostel_id(self, hostel_id):
        pass

    def can_add(self, table, pk):
        if self.exists(table):
            return False
        return True

    def can_update(self, table, pk):
        if self.exists(table, pk):
            return True
        return False

    def can_remove(self, table, pk):
        if self.exists(table, pk):
            return True
        return False

    def exists(self, table, pk):
        if pk in self._tables[table].keys():
            return True
        return False