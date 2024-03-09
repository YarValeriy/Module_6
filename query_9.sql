SELECT students.name, subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN students ON grades.student_id = students.id
WHERE students.id = 1
GROUP BY subjects.name;
