import sqlite3

db_path = "database/adnd_2e_monsters.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query to retrieve the schema of the monsters table
cursor.execute("PRAGMA table_info(monsters);")
schema = cursor.fetchall()

conn.close()
print("Monsters table schema:", schema)
