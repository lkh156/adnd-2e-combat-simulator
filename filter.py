import pandas as pd

# Load the first CSV file containing the monster names
monsters = pd.read_csv('monsters.csv')

# Load the second CSV file with full monster data
monsters_data = pd.read_csv('monsters_data.json_scraped_formatted.csv')

# Assuming 'Monster Name' is the column in both files that you want to match
# Filter 'monsters_data' to keep only rows with monster names in the 'monsters' list
filtered_data = monsters_data[monsters_data['Monster Name'].isin(monsters['Monster Name'])]

# Save the filtered data to a new CSV file
filtered_data.to_csv('filtered_monsters_data.csv', index=False)

print("Filtered data saved to 'filtered_monsters_data.csv'")
