import sqlite3
import pandas as pd

# Path to the SQLite database file
db_path = "database/adnd_2e_monsters.db"

# Connect to the database and load the table into a DataFrame
conn = sqlite3.connect(db_path)
query = "SELECT * FROM monsters LIMIT 10"
monsters_df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the DataFrame
print(monsters_df)
