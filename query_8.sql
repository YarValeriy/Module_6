SELECT teachers.name, subjects.name, AVG(grades.grade) AS average_score
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = 2
GROUP BY subjects.name;

