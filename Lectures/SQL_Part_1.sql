CREATE DATABASE University;
USE University;

CREATE DATABASE xyz_company;
DROP DATABASE xyz_company;

CREATE TABLE Student (
    roll_no INT,
    name VARCHAR(30),
    age INT
);

INSERT INTO Student
VALUES
(101, "adam", 12),
(102, "bob", 14);

SELECT * FROM Student;

SHOW DATABASES;
SHOW TABLES;

CREATE DATABASE SocialMedia;
USE SocialMedia;
CREATE TABLE user(
    id INT PRIMARY KEY,
    age INT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    CONSTRAINT CHECK (age >= 13)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gmail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 305),
(4, 17, "donald", "donald@gmail.com", 200, 105);

SELECT id, name, email FROM user;
SELECT * FROM user;

SELECT id, age, name FROM user
WHERE followers >= 200 AND age <= 16;


CREATE TABLE post (
    id INT PRIMARY KEY,
    content VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

INSERT INTO post
(id, content, user_id)
VALUES
(101, "Hello World", 3),
(102, "Bye Bye", 1),
(103, "Hello Delta", 3);

SELECT * FROM post;

