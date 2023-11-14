-- Script that creates a table second_table and adds multiple rows.
CREATE TABLE IF NOT EXISTS  hbtn_0c_0.second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES
	(1, 'john', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George'. 8);
