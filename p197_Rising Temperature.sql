drop table if exists Weather;
create table Weather (id int, recordDate date, temperature int);
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');


select 
    id 
from 
(
    select 
        id
        ,recordDate
        ,temperature
        ,lag(temperature) over(order by recorddate) as temperature_prev 
        ,lag(recordDate) over(order by recorddate) as recordDate_prev
    from weather

) a
where
    temperature > temperature_prev
    and datediff(day, recordDate_prev, recordDate) = 1
;

