drop table if exists Employee;
create table Employee (id int, salary int);

insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');

-- Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.

GO

create or alter function getNthHighestSalary(@N INT) RETURNS INT AS
begin
    declare @s int = NULL;

    select 
        @s = salary
    from
    (
        select 
            salary
            ,dense_rank() over(order by salary desc) as r
        from
            Employee 
    ) a
    where 
        r = @N
    ;

    return @s;
end

GO

select dbo.getNthHighestSalary(88)

