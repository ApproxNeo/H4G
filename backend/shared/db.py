from tinydb import TinyDB, Query

# Init database
db = TinyDB("database.json", indent=4, separators=(',', ': '))

# Use "drills" table
drills_db = db.table("drills")
cases_db = db.table("cases")
logs_db = db.table("logs", cache_size=None)