drop table if exists Employee;
create table Employee (id int, salary int);

insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '100');

insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');

-- Write an SQL query to report the second highest salary from the Employee table. 
-- If there is no second highest salary, the query should report null.

select top 1 salary as SecondHighestSalary from 
((
    select 
        salary
    from
    (
        select 
            salary
            ,rank() over(order by salary desc) as r
        from
            Employee 
    ) a
    where 
        r = 2
)
union all
(
    select null
)) a
order by salary desc