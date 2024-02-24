SELECT Students.st_name, Courses.cr_name
FROM Students
LEFT JOIN StudentCourses ON Students.st_id = StudentCourses.st_id
LEFT JOIN Courses ON StudentCourses.cr_id = Courses.cr_id;

