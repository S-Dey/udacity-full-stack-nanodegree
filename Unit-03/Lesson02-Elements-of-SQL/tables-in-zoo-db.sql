create table animals (  
       name text,
       species text,
       birthdate date);
create table diet (
       species text,
       food text);  
create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);