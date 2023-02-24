PRAGMA foreign_keys = ON;


CREATE TABLE "department"(
    "dept_id" INTEGER NOT NULL,
    "dept_name" TEXT NOT NULL PRIMARY KEY
);


CREATE TABLE "employee"(
    "emp_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "age" NUMBER NOT NULL,
    "gender" TEXT NOT NULL,
    "status" BOOLEAN NOT NULL,
    "dept_name" TEXT,
    FOREIGN KEY ("dept_name") REFERENCES department (dept_name)
);
