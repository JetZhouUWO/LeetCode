# Write your MySQL query statement below
select *
from Patients
where LOCATE("DIAB1", conditions) = 1
or LOCATE(" DIAB1", conditions) != 0;