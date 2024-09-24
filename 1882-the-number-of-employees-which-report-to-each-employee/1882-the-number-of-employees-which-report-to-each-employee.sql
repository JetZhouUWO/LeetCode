# Write your MySQL query statement below
select reports_to as employee_id, 
(select name from Employees e2 where e1.reports_to = e2.employee_id) as name, 
count(employee_id) as reports_count, 
round(avg(age),0) as average_age
from Employees e1
where reports_to is not null
group by reports_to
having count(employee_id) > 0
order by employee_id;