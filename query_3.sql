SELECT g.name, AVG(gr.grade) AS average_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.name = 'Ukrainian'
GROUP BY g.id, g.name;