import sqlite3
from pathlib import Path


SCHEMA_PATH = Path("sql/01_schema.sql")
TEST_PATH = Path("sql/00_schema_tests.sql")

con = sqlite3.connect(":memory:") #memory allows sqlite to build a temporary db without interfering with actual tables
con.execute("PRAGMA foreign_keys = ON;")
con.executescript(SCHEMA_PATH.read_text("utf-8"))

#read test files one line at a time
label = ""
statement = ""

for line in TEST_PATH.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line.startswith("--"):
        label = line[2:].strip()
    elif line:
        statement = statement + " " + line      # add this line to the statement being built
        if line.endswith(";"):                  # semicolon = statement complete, run it
            try:
                con.execute(statement)
                print("ACCEPTED |", label)
            except sqlite3.IntegrityError as error:
                print("BLOCKED  |", label)
                print("           reason:", error)
            except sqlite3.OperationalError as error:
                print("SQL ERROR|", label)
                print("           problem:", error)
            statement = ""                      # empty the box for the next statement
con.close()