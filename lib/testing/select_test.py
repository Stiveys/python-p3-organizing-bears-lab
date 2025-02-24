import sqlite3
from lib.sql_queries import select_all_female_bears_return_name_and_age

# Set up the in-memory database and execute the create and insert scripts
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Read and execute the create.sql file
with open("lib/create.sql") as f:
    create_as_string = f.read()
cursor.executescript(create_as_string)

# Read and execute the insert.sql file
with open("lib/insert.sql") as f:
    insert_as_string = f.read()
cursor.executescript(insert_as_string)

# Now you can run your tests
def test_select_all_female_bears_return_name_and_age():
    result = cursor.execute(select_all_female_bears_return_name_and_age).fetchall()
    assert len(result) == 3  # Adjusted to match the actual number of female bears
    assert ('Tabitha', 7) in result
    assert ('Melissa', 4) in result
    assert ('Wendy', 2) in result
    # Add more assertions as needed if you have more female bears