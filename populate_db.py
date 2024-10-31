import sqlite3
import pandas as pd

# Define paths to the database and CSV file
db_path = "database/adnd_2e_monsters.db"
csv_path = "filtered_monsters_data.csv"  # Adjust path if needed

# Load the CSV data
monsters_df = pd.read_csv(csv_path)

# Insert data function
def insert_data_from_dataframe(df, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert query using columns that match the database schema
    insert_query = '''
        INSERT INTO monsters (
            monster_name, climate_terrain, frequency, organization, activity_cycle,
            diet, intelligence, treasure, alignment, no_appearing, armor_class,
            movement, hit_dice, thac0, no_of_attacks, damage_attack,
            special_attacks, special_defenses, magic_resistance, size, morale, xp_value
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Insert each row from the DataFrame
    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Monster data inserted successfully!")

# Run the insertion function to populate the database
insert_data_from_dataframe(monsters_df, db_path)
