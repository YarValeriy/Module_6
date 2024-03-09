import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("module6.db")
cursor = conn.cursor()

# Calculate GPA for each student
cursor.execute(
    """SELECT s.id, s.name, AVG(g.grade) AS gpa
                  FROM students s
                  LEFT JOIN grades g ON s.id = g.student_id
                  GROUP BY s.id, s.name
               """
)
student_gpa = cursor.fetchall()

# Sort students by GPA in descending order
sorted_students = sorted(student_gpa, key=lambda x: x[2], reverse=True)

# Select top 5 students with the highest GPA
top_5_students = sorted_students[:5]

# Print the results
print("Top 5 students with the highest GPA:")
for student in top_5_students:
    print(f"Student ID: {student[0]}, Name: {student[1]}, GPA: {student[2]}")

# Close connection
conn.close()
