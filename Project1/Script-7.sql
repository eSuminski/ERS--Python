
DROP TABLE If Exists employees, managers, employee_login, manager_login, reimbursement;

CREATE TABLE employees(
	employee_id serial PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50)
	
);

CREATE TABLE managers(
	manager_id serial PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50)
);

CREATE TABLE employee_login(
	user_id int,
	username varchar(50),
	u_password varchar(50),
	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES employees(employee_id) ON DELETE cascade
);

CREATE TABLE manager_login(
	user_id int,
	username varchar(50),
	u_password varchar(50),
	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES managers(manager_id) ON DELETE cascade
);


CREATE TABLE reimbursement(
	reimbursement_id serial PRIMARY KEY,
	employee_id int,
	reimbursement float,
	reason varchar(200),
	approval int,
	manager_comment varchar(200),
	CONSTRAINT fk_employee_id FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE cascade
);
