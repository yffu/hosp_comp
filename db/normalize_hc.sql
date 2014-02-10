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

drop table newhgi;

rename table nhgi to newhgi;

show tables;

select * from newhgi;

alter table newhgi add primary key (providernumber);

select * from newhgi;

create table hospitaltype (type_id smallint primary key auto_increment, type_name varchar(30) unique);

insert into hospitaltype (type_name) select distinct hospitaltype from newhgi;

create table nhgi as select * from newhgi n, hospitaltype t where n.hospitaltype=t.type_name;

alter table newhgi add column type_id smallint after hospitaltype;

alter table newhgi add primary key(providernumber);

update newhgi set type_id=(select type_name from hospitaltype h, newhgi n where n.hospitaltype=h.type_name);

select n.*, t.type_id from nhgi n, hospitaltype t where t.type_name=n.hospitaltype;

describe newhgi;

select * from nhgi;

alter table nhgi drop column hospitaltype;

alter table nhgi drop column type_name;

alter table nhgi add constraint hosptype_type_id_fk foreign key(type_id) references hospitaltype(type_id), 
add constraint hospown_owner_id_fk foreign key(owner_id) references hospitalowner(owner_id);

drop table newhgi;

rename table nhgi to newhgi;

show tables;

select * from hacm;

create table newhacm as select providerid, measure, rateper1000discharges from hacm;

select l.* from hacm l left join newhgi r on l.providerid=r.providernumber
	where r.providernumber=null;

select count(distinct providerid) from newhacm;

select * from newhacm;

describe newhacm;

alter table newhacm change providerid providernumber decimal(6,0);

alter table newhacm add constraint hgi_providernumber_fk foreign key(providernumber) references newhgi(providernumber);

select count(distinct providerid) from hacm h, newhgi n where h.providerid=n.providernumber;

select count(*) from hacm where hacm.providerid not in (select providerid from hacm h, newhgi n where h.providerid=n.providernumber);

select * from hai;

select l.* from hai l left join newhgi r on l.providerid=r.providernumber where r.providernumber=null;

select * from hai where location!='';

create table newhai as select providerid as providernumber, measure, score, footnote from hai;

select count(*) from newhai; 

select count(*) from hai;

alter table newhai add constraint hai_hgi_pid foreign key(providernumber) references newhgi(providernumber);

select * from newhai;

-- this completes the section on hai

select * from hmvm;

create table newhmvm as select providernumber, diagnosisrelatedgroup as measure, numberofcases, footnote from hmvm;

select count(*) from newhai; 

select count(*) from hai;

alter table newhmvm add constraint hmvm_hgi_pid foreign key(providernumber) references newhgi(providernumber);

-- this completes the hmvm

select * from mspp;

select l.providerid from mspp l left join newhgi r on l.providerid=r.providernumber where r.providernumber=null;

create table newhmspp as select providerid as providernumber, measure, col12 as score, footnote from mspp;

rename table newhmspp to newmspp;

select * from newmspp;

select * from newmspp where footnote!='';

alter table newmspp add constraint mspp_hgi_pid foreign key(providernumber) references newhgi(providernumber);

-- completes mspp

select * from newsbbc;

-- entries in sbbc where the pid is not found in the hgi table

delete from newsbbc where providernumber in (select l.ProviderNumber from sbbc l left join newhgi r on l.providernumber=r.providernumber where r.providernumber is null);

select l.ProviderNumber from sbbc l left join newhgi r on l.providernumber=r.providernumber where r.providernumber is null;

create table newsbbc as
(select providernumber, period, type_id, AvgSpendingPerEpisodeHospital as aspe_hospital, AvgSpendingPerEpisodeState as aspe_state, AvgSpendingPerEpisodeNation as aspe_nation from sbbc, claimtype where sbbc.claimtype=claimtype.type_name);

select distinct claimtype from sbbc;

create table claimtype (type_id smallint primary key auto_increment, type_name varchar(40) unique);

insert into claimtype (type_name) select distinct claimtype from sbbc;

alter table newsbbc add constraint sbbc_hgi_pid foreign key(providernumber) references newhgi(providernumber);

select * from sbbc;

insert into hospitalowner(owner_id, owner_name) values (11, 'unclassified');

insert into hospitaltype(type_name) values ('unclassified');

select * from newhgi;

alter table newhgi drop foreign key hospown_owner_id_fk;

alter table newhgi drop foreign key hosptype_type_id_fk;

insert into newhgi (providernumber, hospitalname, state) select distinct l.providernumber, l.hospitalname, l.state from sbbc l left join newhgi r on l.providernumber=r.providernumber where r.providernumber is null;

select * from hospitaltype;

select * from hospitalowner order by owner_id asc;

delete from hospitalowner where owner_name='unclassified';

select * from newhgi where owner_id=4 and countyname is null;

update newhgi set owner_id=11 where owner_id=4 and countyname is null;

update newhgi set type_id=4 where type_id=11;

select * from newhgi where type_id=4;

alter table newhgi add constraint hgi_owner_fk foreign key(owner_id) references hospitalowner(owner_id);

alter table newhgi add constraint hgi_type_fk foreign key(type_id) references hospitaltype(type_id);

drop table hacm, hai, hgi, hmvm, mspp, sbbc;

alter table newsbbc add constraint sbbc_claimtype_fk foreign key (type_id) references claimtype(type_id);

alter table newsbbc add constraint sbbc_hgi_fk foreign key (providernumber) references newhgi(providernumber);

rename table newhacm to hacm;

rename table newhai to hai;

rename table newhgi to hgi;

rename table newhmvm to hmvm;

rename table newmspp to mspp;

rename table newsbbc to sbbc;





