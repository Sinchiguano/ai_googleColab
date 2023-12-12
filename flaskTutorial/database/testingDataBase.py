import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect("user_auth.db")
#
# Create a Pandas DataFrame by querying data from the database
query = 'SELECT * FROM User'
df = pd.read_sql_query(query, connection)

# Close the database connection
# connection.close()
print("----------")
# Display the DataFrame
print(df.shape)
print(df.head(5))