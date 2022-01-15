drop table if exists Customers;
drop table if exists Orders;
Create table Customers (id int, name varchar(255));
Create table Orders (id int, customerId int);
insert into Customers (id, name) values ('1', 'Joe');
insert into Customers (id, name) values ('2', 'Henry');
insert into Customers (id, name) values ('3', 'Sam');
insert into Customers (id, name) values ('4', 'Max');
Truncate table Orders;
insert into Orders (id, customerId) values ('1', '3');
insert into Orders (id, customerId) values ('2', '1');


-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.


select name as Customers from Customers c where not exists
(
    select 1 from Orders o where c.id = o.customerId
);
