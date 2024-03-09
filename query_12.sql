SELECT groups.name, subjects.name, students.name, grades.grade, grades.date
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'
AND subjects.name = 'English'
AND grades.date = 
(
SELECT MAX(date)
FROM (
SELECT grades.date
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A'
AND subjects.name = 'English')
)