# import psycopg2
# from psycopg2 import sql, DatabaseError
# from connect import create_connection
import sqlite3
from faker import Faker
import random
import logging
from datetime import datetime, timedelta


# Connect to PostgreSQL database - doesn't work properly, need to clarify later
# conn = psycopg2.connect(
#     dbname="module6",
#     user="postgres",
#     password="567234",
#     host="localhost",
#     port="5432",
# )


# Create a SQLite database connection instead of postgres
conn = sqlite3.connect("module6.db")
cursor = conn.cursor()

# Initialize Faker to generate random data

fake = Faker("uk-Ua")

# Create tables

cursor.execute("""drop table if exists groups""")
cursor.execute(
    """CREATE TABLE groups (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL
                )"""
)
# VARCHAR(50)

cursor.execute("""drop table if exists students""")
cursor.execute(
    """CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(150) NOT NULL,
                    group_id INTEGER REFERENCES groups (id)
                )"""
)
# VARCHAR(100)
cursor.execute("""drop table if exists teachers""")
cursor.execute(
    """CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(150) NOT NULL
                )"""
)

cursor.execute("""drop table if exists subjects""")
cursor.execute(
    """CREATE TABLE subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER REFERENCES teachers (id)
                )"""
)
cursor.execute("""drop table if exists grades""")
cursor.execute(
    """CREATE TABLE grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER REFERENCES students (id),
                    subject_id INTEGER REFERENCES subjects (id),
                    grade INTEGER CHECK (grade >=0 AND grade <= 100),
                    date DATE NOT NULL
                )"""
)

# Generate groups
groups = ["Group A", "Group B", "Group C"]
for group_name in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

# Generate teachers
teachers = [fake.name() for _ in range(5)]
for teacher_name in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

# Generate subjects and assign random teachers
subjects = [
    "Mathematics",
    "Physics",
    "Biology",
    "English",
    "Ukrainian",
    "History",
    "Geography",
]
for subject_name in subjects:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute(
        "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)",
        (subject_name, teacher_id),
    )

# Generate students and assign random groups
for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    cursor.execute(
        "INSERT INTO students (name, group_id) VALUES (?, ?)",
        (student_name, group_id),
    )

# Generate grades for each student in all subjects
for student_id in range(1, 31):
    for subject_id in range(1, 8):
        for _ in range(random.randint(1, 20)):
            grade = random.randint(2, 5)
            date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime(
                "%Y-%m-%d"
            )
            cursor.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                (student_id, subject_id, grade, date),
            )


try:
    # Save changes
    conn.commit()
except sqlite3.DatabaseError as e:
# except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Close connection
    cursor.close()
    conn.close()

print("Database populated successfully.")
