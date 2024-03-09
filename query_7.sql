SELECT students.name, subjects.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group C' AND subjects.name = 'History';
