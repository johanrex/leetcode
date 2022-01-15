drop table if exists Person;
create table Person
(
    id int,
    email varchar(50)
);

insert into Person values (1, 'a@b.com');
insert into Person values (2, 'c@d.com');
insert into Person values (3, 'a@b.com');

-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.
-- The query result format is in the following example.

select
    email as Email
from
    Person
group by 
    email
having 
    count(*) > 1
