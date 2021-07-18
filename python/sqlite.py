import sqlite3
import os
from typing import Tuple, Union




class Database:
    def __init__(self, database:str):
        self.raw_database:str = str(database)

        # Try creating a database to reduce
        # database not found errors.
        self.db = sqlite3.connect(self.raw_database)
        self.db.close()

        # a list of all the available 
        # tables in the database.
        self.tables = self.get_all_tabel_names()
    


    # a function to create a tabel
    def create_tabel(self, table_name:str, columns:Tuple[str]) -> bool:
        # check if the database is a sqlite3 file
        if not self.check_is_database_file():
            return "101"
        
        if table_name in self.get_all_tabel_names():
            return "102"

        # convert the cols into tuples
        # because the table's columns can should be tuples
        print(columns)
        cols = tuple(columns)

        # check id any col is not str
        for col in cols:
            if type(col) is not str:
                return "104"

        print(f"CREATE TABLE {table_name} {cols}", cols)

        # open the database and add values.
        db = sqlite3.connect(self.raw_database)
        cursor = db.cursor()
        cursor.execute(f"CREATE TABLE {table_name} {cols}")
        cursor.close()
        db.commit()
        db.close()

        return "100"



    # a function to get all the tabel names
    def get_all_tabel_names(self) -> Union[list, bool]:
        if not self.check_is_database_file():
            return "101"
        # change the database to string
        database = self.raw_database
        # a list to hold all the tables in the database
        tables = []

        db = sqlite3.connect(database)
        cursor = db.cursor()
        raw_query = cursor.execute(f"SELECT sql FROM sqlite_master where type = 'table'")
        # a loop to fill the `tables`
        for col in raw_query:
            tables.append(col[0].split(" ")[2])
            
        cursor.close()
        db.close()


        return tables



    # a function to get all the tabel names
    def get_all_column_names(self, tabel_name) -> Union[list, bool]:
        if not self.check_is_database_file():
            return "101"

        if tabel_name not in self.get_all_tabel_names():
            return "103"
        # change the database to string
        database = self.raw_database
        # a list to hold all the tables in the database
        table_name = tabel_name

        db = sqlite3.connect(database)
        cursor = db.cursor()
        raw_query = cursor.execute(f"SELECT sql FROM sqlite_master where type = 'table'")
        # a loop to fill the `tables`
        for col in raw_query:
            tb_name = col[0].split(" ")[2]
            # if the tabelname is the required tabel's name
            if tb_name == table_name:
                result = eval(col[0].replace("CREATE TABLE ", "").partition(" ")[2])

                cursor.close()
                db.close()
                
                return result
            
        # if the requested tabel was not found
        cursor.close()
        db.close()
                
        return "103"
    


    # a static method for getting all the tables
    # without passing parameters to the parent
    @staticmethod
    def get_foregin_tabel_names(database:str) -> Union[list, bool]:
        # change the database to string
        database = str(database)
        # a list to hold all the tables in the database
        tables = []

        db = sqlite3.connect(database)
        cursor = db.cursor()
        raw_query = cursor.execute(f"SELECT sql FROM sqlite_master where type = 'table'")
        # a loop to fill the `tables`
        for col in raw_query:
            tables.append(col)
        cursor.close()
        db.close()

        return tables
    


    # adds a value in the asked
    def add_values_in_column(self, tabel_name:str, columns:tuple, values:tuple) -> bool:
        # check if the file is a database or not
        if not self.check_is_database_file():
            return "101"

        # check if the tabel exists or not
        if tabel_name not in self.get_all_tabel_names():
            return "103"


        database = self.raw_database

        # check if the columns is list or tuple:
        t_c = type(columns)
        if t_c in [list, tuple]:
            columns = tuple(columns)
        else:
            columns = tuple([columns])

        # check the values also
        v_c = type(values)
        if v_c in [list, tuple]:
            values = tuple(values)
        else:
            values = tuple([values])


        # put the stuffs together to create an execution
        query = f"INSERT INTO {tabel_name} {columns} VALUES {values}"

        # the sql operation
        db = sqlite3.connect(database)
        cursor = db.cursor()
        cursor.execute(query)
        cursor.close()
        db.commit()
        db.close()

        return "100"
    


    # check if the given file is a database or not.
    def check_is_database_file(self):
        try:
            database = self.raw_database
            db = sqlite3.connect(database)
            cursor = db.cursor()
            cursor.execute("SELECT * FROM sqlite_master")
            cursor.close()
            db.close()
            return True
        except sqlite3.DatabaseError:
            return False