import sqlite3
from pathlib import Path
#store two location variables
DB_PATH = Path("data/fernledger.db")
SCHEMA_PATH = Path("sql/01_schema.sql")
#open database file
con = sqlite3.connect(DB_PATH)
con.execute("PRAGMA foreign_keys = ON;")
con.executescript(SCHEMA_PATH.read_text(encoding="utf-8")) #read sql script
con.commit() #save changes permanently

tables = con.execute("SELECT name FROM sqlite_master WHERE type = 'table';").fetchall()
print("Tables created:", tables)

con.close()

