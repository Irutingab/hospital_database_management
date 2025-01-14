import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="irutingaboRai1@",
    database="hospital"
)
cursor = conn.cursor()

csv_file = 'C:/Users/RAISSA/Desktop/Dev/python/python-exercises/pandas/hospital_data.csv'

try:
    data = pd.read_csv(csv_file)

    print("CSV Columns:", data.columns)

    for _, row in data.iterrows():
        cursor.execute("""
            INSERT INTO hospital_data (Hospital_ID, Hospital_Name, City, Department, Rating)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row['Hospital_ID'],
            row['Hospital_Name'],
            row['City'],
            row['Department'],
            row['Rating']
        ))
    conn.commit()
    print("Data imported successfully!")

except FileNotFoundError:
    print(f"Error: The file {csv_file} was not found.")
except KeyError as e:
    print(f"Error: Column not found in the CSV: {e}")
except mysql.connector.Error as err:
    print(f"Database error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Database connection closed.")
