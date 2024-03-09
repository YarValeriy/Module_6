SELECT subjects.name, teachers.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = 2;