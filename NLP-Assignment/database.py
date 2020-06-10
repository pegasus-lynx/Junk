from classes import *

class Database(object):
    
    _instance = False
    _tables = None

    _table_names = ["user", "student", "professor", "department", "institute", 
                    "record", "student_reg", "course_reg",
                    "hostel", "course", "classes"]

    _table_pk_names = {
        "user": "uid", "student": "sid",
        "professor": "pid", "hostel": "hid",
        "institute": "iid", "record": "rid",
        "classes": "clid", "course": "cid",
        "student_reg": "srid",
        "course_reg": "crid",
        "department": "did"
    }

    def __init__(self):
        if self._instance:
            print("Already an instance. Another cannot be created")

        self._instance = True
        self._tables = self.create_tables()

    def create_tables(self):
        tables = dict()

        for table in self._table_names:
            tables[table] = dict()

        return tables

    def clear(self):
        for table in self._table_names:
            self._tables[table] = dict()

    def load(self, filename):
        pass

    def add(self, table, item):
        pk = item.get_pk()

        if not self.can_add(table, pk):
            print("Instance with {} : {} exists".format(
                self._table_pk_names[table], pk))
            return False

        self._tables[table][pk] = item
        return True

    def update(self, table, item):
        pk = item.get_pk()

        if not self.can_update(table, pk):
            print("Instance with the {} : {} does not exists".format(
                self._table_pk_names[table], pk))
            return False

        self._tables[table][pk] = item
        return True

    def remove(self, table, item):
        pk = item.get_pk()

        if not self.can_remove(table, pk):
            print("Instance with {} : {} does not exist".format(
                        self._table_pk_names[table], pk))
            return False

        del self._tables[table][pk]
        return True

    def add_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_add(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} exists".format(
                self._table_pk_names[table], pks[p]))
            return False

        for item in items:
            self.add(table, item)

        return True

    def update_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_update(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} does not exist".format(
                self._table_pk_names[table], pks[p]))
            return False

        for item in items:
            self.update(table, item)

        return True

    def remove_batch(self, table, items):
        pks  = [item.get_pk() for item in items]
        mask = [self.can_remove(table, pk) for pk in pks]

        if False in mask:
            p = mask.index(False)
            print("Instance with {} : {} does not exist".format(
                self._table_pk_names[table], pks[p]))
            return False

        for item in items:
            self.remove(table, item)

        return True

    def find_by_pk(self, table, pk):
        if not self.exists(table, pk):
            print("The object doesn't exist in the database.")
            return None

        return self._tables[table][pk]

    def find(self, table, params):
        pass

    def get_students_by_hostel_id(self, hostel_id):
        pass

    def can_add(self, table, pk):
        if self.exists(table, pk):
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

