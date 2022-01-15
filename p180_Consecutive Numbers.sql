drop table if exists Logs;
create table Logs (id int, num int);
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');


select distinct num as ConsecutiveNums from 
(
    select 
        num
        ,lag(num, 1) over(order by id) as lag1
        ,lag(num, 2) over(order by id) as lag2
    from 
        logs 
) a
where 
    num = lag1 
    and num = lag2
