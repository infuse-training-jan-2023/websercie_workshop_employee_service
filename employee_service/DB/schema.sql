
CREATE TABLE "employee"(
    "empId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "age" NUMBER NOT NULL,
    "gender" TEXT NOT NULL,
    "status" BOOLEAN NOT NULL,
    "deptid" INTEGER,
    CONSTRAINT fk_departments
    FOREIGN KEY (deptid)
    REFERENCES department(deptId)
);

CREATE TABLE "department"(
    "deptId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "deptName" TEXT NOT NULL
);
