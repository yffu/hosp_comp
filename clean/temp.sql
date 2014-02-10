select * from hgi where lower(hospitalname) like '%va%';

describe mspp;

alter table mspp change column footnote footnote varchar(150);

describe hai;

select count(*) from mspp;

select * from hai where footnote like '%Data were collected during a shorter period%';

select count(*) from hai;

select * from hgi where lower(hospitalname) like '%cheyenne va%';

select count(*) from hgi;

show tables;     
     
     
     
     
select * from name_map;