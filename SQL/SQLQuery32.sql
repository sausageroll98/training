use datalab_ce02;
go
/*
Transactions:
-insert
-update
-delete
*/
/*
inserting data:
TSQL
-insert hardcoded values
-copy/paste (inserting data from one table into another)
-merge
Data Ingestion techniques (bulk data)
-tools
ETL (Extract Transform Load) - legacy
Data Pipelines - Current 
*/
if object_id('jeevanrai.patientdata') is not null
drop table patientdata
create table patientdata
(
patient_id int identity(1,1) primary key,
nhsnumber varchar(12) not null,
fname varchar(100) null,
lname varchar(100) null,
dob date null,
registration_date date default getdate()
)
go
if object_id('jeevanrai.icd10') is not null
drop table icd10
create table icd10
(
diag_id int identity primary key,
code char(5) not null,
alt_code char(4) not null,
descr varchar(100)
)
go

if object_id('jeevanrai.patient_diagnosis') is not null
drop table patient_diagnosis
create table patient_diagnosis
(
patient_diag_id int identity primary key,
patient_id int references jeevanrai.patientdata(patient_id), -- definition of a foreign key
diag_id int references jeevanrai.icd10(diag_id),
diagnosis_date date default getdate()

)