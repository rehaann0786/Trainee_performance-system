CREATE TABLE IF NOT EXISTS trainees (
    trainee_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    attendance NUMERIC(5,2) NOT NULL,
    score NUMERIC(5,2) NOT NULL,
    assignment_status VARCHAR(20) NOT NULL,

    CONSTRAINT chk_attendance
        CHECK (attendance >= 0 AND attendance <= 100),

    CONSTRAINT chk_score
        CHECK (score >= 0 AND score <= 100),

    CONSTRAINT chk_specialization
        CHECK (specialization IN ('Data Science', 'Data Engineering')),

    CONSTRAINT chk_assignment_status
        CHECK (assignment_status IN ('Submitted', 'Pending'))
);