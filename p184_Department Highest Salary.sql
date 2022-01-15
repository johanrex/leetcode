drop table if exists Employee;
Create table Employee (id int, name varchar(255), salary int, departmentId int);
drop table if exists Department;
Create table Department (id int, name varchar(255));

go

insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '70000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Jim', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('3', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('5', 'Max', '90000', '1');
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');


select 
    d.name as Department
    ,e.name as Employee
    ,s.salary as Salary
from 
(
    select departmentId, max(salary) as salary from Employee group by departmentId
) s
join Employee e on e.departmentId = s.departmentId and e.salary = s.salary
join Department d on e.departmentId = d.id
