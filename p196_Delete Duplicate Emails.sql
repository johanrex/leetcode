
drop table If Exists Person;
create table Person
(
    Id int,
    Email varchar(255)
)

go

insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.
-- Return the result table in any order.
-- The query result format is in the following example.


with
cte as
(
    select
        *, row_number() over(partition by email order by id) as rn
    from
        Person
)
delete from Person where exists( select 'a' from cte where Person.id = cte.id and cte.rn > 1);

select * from person;
