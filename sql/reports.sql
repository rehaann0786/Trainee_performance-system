-- 1. Overall batch statistics
SELECT
    COUNT(*) AS total_trainees,
    ROUND(AVG(attendance), 2) AS average_attendance,
    ROUND(AVG(score), 2) AS average_score
FROM trainees;


-- 2. Specialization-wise statistics
SELECT
    specialization,
    COUNT(*) AS total_trainees,
    ROUND(AVG(attendance), 2) AS average_attendance,
    ROUND(AVG(score), 2) AS average_score
FROM trainees
GROUP BY specialization
ORDER BY specialization;


-- 3. Assignment status statistics
SELECT
    assignment_status,
    COUNT(*) AS total_trainees
FROM trainees
GROUP BY assignment_status
ORDER BY assignment_status;