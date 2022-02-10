use datalab_ce02
go 
insert into icd10
(code, alt_code, descr)
values
('A00.0','A000','Cholera'),
('A01.0','A010','Typhoid'),
('A02.0','A020','Salmonella')
go
insert into patient_diagnosis
(patient_id, diag_id, diagnosis_date)
VALUES
(2,23,'2022-03-21')

select * from patientdata
select * from icd10
select * from patient_diagnosis