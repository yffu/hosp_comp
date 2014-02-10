select * from newhgi;

alter table newhgi drop column address2, drop column address3;

select * from newhgi where location1 != '';

alter table newhgi drop column location1;

select * from newhgi;

select distinct hospitaltype from newhgi;

select distinct h.HospitalOwner from newhgi h;

-- normalize the hospital general infromation table

create table hospitalowner (owner_id smallint primary key auto_increment, owner_name varchar(30) unique);

alter table hospitalowner change column owner_name owner_name varchar(50);

describe hospitalowner;

select * from hospitalowner order by owner_id asc;

insert into hospitalowner (owner_name) select distinct h.hospitalowner from newhgi h;

alter table nhgi add constraint nghi_hospitalowner_fk foreign key (owner_id) references hospitalowner(owner_id);

create table nhgi as select h.*, o.owner_id from newhgi h, hospitalowner o where h.hospitalowner=o.owner_name;

drop table nhgi;

select * from nhgi;

alter table nhgi drop column hospitalowner;

