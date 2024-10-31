import sqlite3

# Define the path to the database file
db_path = "database/adnd_2e_monsters.db"

# Connect to SQLite database (creates the database file if it doesn’t exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table schema based on the CSV headers
create_table_query = '''
CREATE TABLE IF NOT EXISTS monsters (
    id INTEGER PRIMARY KEY,
    monster_name TEXT,
    climate_terrain TEXT,
    frequency TEXT,
    organization TEXT,
    activity_cycle TEXT,
    diet TEXT,
    intelligence TEXT,
    treasure TEXT,
    alignment TEXT,
    no_appearing TEXT,
    armor_class TEXT,
    movement TEXT,
    hit_dice TEXT,
    thac0 TEXT,
    no_of_attacks TEXT,
    damage_attack TEXT,
    special_attacks TEXT,
    special_defenses TEXT,
    magic_resistance TEXT,
    size TEXT,
    morale TEXT,
    xp_value TEXT
)
'''

# Execute the command to create the table
cursor.execute(create_table_query)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
