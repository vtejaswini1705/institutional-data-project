-- 1. Total enrollment by year
SELECT enrollment_year, COUNT(*) AS total_students
FROM Students
GROUP BY enrollment_year
ORDER BY enrollment_year;

-- 2. Enrollment by major
SELECT major, COUNT(*) AS total_students
FROM Students
GROUP BY major
ORDER BY total_students DESC;

-- 3. Gender distribution of students
SELECT gender, COUNT(*) AS total_students
FROM Students
GROUP BY gender;

-- 4. Average age of students by major
SELECT major, AVG(age) AS avg_age
FROM Students
GROUP BY major;

-- 5. Course enrollments (how many students per course)
SELECT c.course_name, COUNT(e.student_id) AS total_enrolled
FROM Enrollment e
JOIN Courses c ON e.course_id = c.course_id
GROUP BY c.course_name
ORDER BY total_enrolled DESC;

-- 6. Retention proxy (students enrolled for more than 1 year)
SELECT s.student_id, s.first_name, s.last_name, 
       MIN(e.course_id) AS first_course, MAX(e.course_id) AS last_course,
       (MAX(s.enrollment_year) - MIN(s.enrollment_year)) AS years_enrolled
FROM Students s
JOIN Enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING years_enrolled > 0;

-- 7. Retention rate (students who continued after their first year)
SELECT 
    s.enrollment_year,
    COUNT(DISTINCT s.student_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN e.semester LIKE '2021%' OR e.semester LIKE '2022%' THEN s.student_id END) AS retained_next_year,
    ROUND(
        COUNT(DISTINCT CASE WHEN e.semester LIKE '2021%' OR e.semester LIKE '2022%' THEN s.student_id END) * 100.0 /
        COUNT(DISTINCT s.student_id), 2
    ) AS retention_rate
FROM Students s
JOIN Enrollment e ON s.student_id = e.student_id
GROUP BY s.enrollment_year;

-- 8. Graduation rate proxy (students with 4+ years of enrollment)
SELECT 
    COUNT(DISTINCT s.student_id) AS graduated,
    COUNT(*) AS total_students,
    ROUND(
        COUNT(DISTINCT CASE WHEN (2023 - s.enrollment_year) >= 4 THEN s.student_id END) * 100.0 / 
        COUNT(DISTINCT s.student_id), 2
    ) AS graduation_rate
FROM Students s;
