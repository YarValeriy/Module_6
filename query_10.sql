SELECT teachers.name AS teacher, subjects.name AS subject, students.name AS student
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN students ON grades.student_id = students.id
WHERE students.id = 1
AND teachers.id = 2
GROUP BY subjects.name;