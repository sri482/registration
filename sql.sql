CREATE DATABASE candidate_registration;
CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    dob DATE,
    resume_path VARCHAR(255)
);
