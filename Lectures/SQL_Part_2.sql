SELECT @@autocommit;

CREATE DATABASE prime;
USE prime;

CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance DECIMAL(10, 2)
);

INSERT INTO accounts (name, balance) VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

SELECT * FROM accounts;

SET autocommit = 0;

# Commit
START TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;

# Rollback
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 3;
ROLLBACK;

# Savepoint
START TRANSACTION;
UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;
UPDATE accounts SET balance = balance + 10 WHERE id = 1;
ROLLBACK TO after_wallet_topup;
COMMIT;


# JOINS
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

SELECT * FROM customers;
SELECT * FROM orders;

# Inner Join
SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
SELECT *
FROM orders o
INNER JOIN customers c
ON c.customer_id = o.customer_id;

# Left Join
SELECT *
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

# Right Join
SELECT *
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

# Outer Join
## Left Join UNION Right Join
SELECT * FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT * FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

# Cross Join
SELECT *
FROM customers
CROSS JOIN orders;

# Self Join
SELECT *
FROM customers a
JOIN customers b
ON a.customer_id = b.customer_id;



# Practice Qs
## Write SQL command to display the exclusive joins:
### Left Exclusive Join
SELECT *
FROM customers A
LEFT JOIN orders B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;

### Right Exclusive Join
SELECT *
FROM customers A
RIGHT JOIN orders B
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL;



# Sub - Queries
## With WHERE
SELECT *
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
);

## With SELECT
SELECT name,
    (
        SELECT COUNT(*)
        FROM orders o
        WHERE o.customer_id = c.customer_id
    ) as order_cnt
FROM customers c;

## With FROM
SELECT smry.customer_id, smry.avg_amnt
FROM (
    SELECT customer_id, AVG(amount) AS avg_amnt
    FROM orders
    GROUP BY customer_id
) AS smry;




# Views in SQL
CREATE VIEW v1 AS
SELECT customer_id, name FROM customers;

SELECT * FROM v1;

CREATE VIEW v2 AS
SELECT c.customer_id, c.name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

SELECT * FROM v2;



# Index in SQL
CREATE TABLE acnts (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10, 2),
    branch VARCHAR(50)
);
INSERT INTO acnts VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');

SELECT * FROM acnts;

CREATE INDEX idx_branch ON acnts(branch);
SHOW INDEX FROM acnts;

SELECT *
FROM acnts
WHERE branch = 'Mumbai';

CREATE INDEX idx2 ON acnts(branch, balance);
DROP INDEX idx2 ON acnts;



# Stored Procedures
DELIMITER $$
CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL(10, 2))
BEGIN
    SELECT balance INTO bal
    FROM acnts
    WHERE account_id = acc_id;
END $$
DELIMITER ;

DROP PROCEDURE IF EXISTS check_balance;

CALL check_balance(2);
CALL check_balance(1, @balance);
SELECT @balance;







