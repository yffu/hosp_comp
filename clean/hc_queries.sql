show tables;

select * from hacm;

describe hacm;

insert into hacm (phonenumber) values (8643665011);

alter table hacm change column phonenumber phonenumber int(11);

describe hacm;

select count(*) from hacm;

show tables;

drop table hacm, hai, hgi, hmvm, mspp, sbbc;

show tables;

select count(*) from hacm;

select count(*) from hai;

select count(*) from hgi;

select count(*) from sbbc;

select count(*) from mspp;

select count(*) from sbbc;

describe mspp;

-- change the footnotes section of mssp to be larger, for the rows that were not inserted 

alter table mspp change column footnote footnote varchar(100);

select * from mspp;

describe hai;
-- change the footnotes section of hai to be larger, for the rows that were not inserted 

alter table hai change column footnote footnote varchar(300);

select * from hai;

describe hmvm;
