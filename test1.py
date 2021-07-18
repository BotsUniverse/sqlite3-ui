import sys
sys.path.append("./../")
from python.sqlite import Database

db = Database("test.something.sqlite3")
db.create_tabel("hello", ["id integer primary key not null", "col1", "col2 TEXT", "col3 BOOLEAN", "col4 DATETIME"])

print( db.get_all_column_names("hello") )