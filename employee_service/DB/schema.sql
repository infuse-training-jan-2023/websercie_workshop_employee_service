PRAGMA foreign_keys = ON;


CREATE TABLE "department"(
    "deptId" INTEGER NOT NULL,
    "deptName" TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE "employee"(
    "empId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "age" NUMBER NOT NULL,
    "gender" TEXT NOT NULL,
    "status" BOOLEAN NOT NULL,
    "deptName" TEXT,
    FOREIGN KEY ("deptName") REFERENCES department (deptName)
);



CREATE TABLE "employee_department"(
    "empId" INTEGER NOT NULL ,
    "deptId" INTEGER NOT NULL ,
    CONSTRAINT fk_departments
    FOREIGN KEY (deptId)
    REFERENCES "department"(deptId)
    CONSTRAINT fk_employee
    FOREIGN KEY (empId)
    REFERENCES "employee"(empId)
);
