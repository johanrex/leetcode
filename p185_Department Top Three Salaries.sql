drop table if exists Employee;
drop table if exists Department;

create table Employee (id int, name varchar(255), salary int, departmentId int);
create table Department (id int, name varchar(255));

insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');

insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');

-- A company's executives are interested in seeing who earns the most money in each of the company's departments. 
-- A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
-- Write an SQL query to find the employees who are high earners in each of the departments.
-- Return the result table in any order.

with 
rankedSalariesPerDepartment as
(
    select 
        salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) as r 
    from 
        Employee
),
top3RankedSalariesPerDepartment as
(
    select distinct salary, departmentId from rankedSalariesPerDepartment where r <= 3
)
select 
    d.name as Department
    ,e.name as Employee
    ,top3.salary as Salary
from 
    top3RankedSalariesPerDepartment top3
    join Employee e on top3.salary = e.salary and top3.departmentId = e.departmentId
    join Department d on d.id = top3.departmentId
;


