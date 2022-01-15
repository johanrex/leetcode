drop table if exists Employee;
create table Employee
(
    id int,
    name varchar(50),
    salary int,
    managerId int
)

insert into Employee
values
    (1, 'Joe', 70000, 3),
    (2, 'Henry', 80000, 4),
    (3, 'Sam', 60000, Null),
    (4, 'Max', 90000, Null);

-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The query result format is in the following example.

select
    e.name as Employee
from
    Employee e
    join Employee m
        on e.managerId = m.id
where 
    e.salary > m.salary

