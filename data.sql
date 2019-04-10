create table if not exists employee (
emp_id INTEGER auto_inrement not NULL ,
employee_name text NOT NULL,
birthdate date NOT NULL,
jobid text NOT NULL,
 salary integer not null,
 location text not null,
 dept_id integer not null,
PRIMARY KEY (emp_id)
);


 create table IF NOT EXISTS sites (
  site_id integer NOT NULL PRIMARY KEY ,
  capacity integer NOT NULL ,
  fragment_limit integer NOT NULL
 );


create table if not EXISTS arum (
  arum_id INTEGER NOT NULL PRIMARY KEY ,
  site_id INTEGER not NULL ,
  query_id integer not NULL ,
  frequency INTEGER not null,
  mod text not NULL ,
  attribute text not NULL,
  predicate INTEGER not null
);

CREATE TABLE  if NOT EXISTS dcm(

site_id INTEGER not NULL PRIMARY KEY ,
body text not NULL
);

