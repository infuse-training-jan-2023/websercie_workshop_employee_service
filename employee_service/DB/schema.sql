
CREATE TABLE "employee"(
    "empId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "age" NUMBER NOT NULL,
    "gender" TEXT NOT NULL,
    "status" BOOLEAN NOT NULL
);

CREATE TABLE "department"(
    "deptId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "deptName" TEXT NOT NULL
);

CREATE TABLE "employee_department"(
    "empId" INTEGER NOT NULL,
    "deptId" INTEGER NOT NULL,
    CONSTRAINT fk_departments
    FOREIGN KEY (deptId)
    REFERENCES department(deptId)
    CONSTRAINT fk_employee
    FOREIGN KEY (empId)
    REFERENCES employee(empId)
);
