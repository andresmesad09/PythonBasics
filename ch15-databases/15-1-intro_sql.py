import sqlite3
from pathlib import Path


def main():

    values = (
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29),
    )

    create_table = """
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INT
    );
    """

    insert_values = "INSERT INTO Roster VALUES(?,?,?);"

    db_path = Path().cwd() / "ch15-databases" / "Roster.db"

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        # Create table
        cursor.execute(create_table)
        # Insert values in the table
        cursor.executemany(insert_values, values)
        # Update name in table
        cursor.execute("UPDATE Roster SET Name=? WHERE Name=?", ("Ezri Dax", "Jadzia Dax"))
        # Display the name and age of everyone in the table classified as Bajoran
        cursor.execute("SELECT Name, Age FROM Roster")
        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    main()
