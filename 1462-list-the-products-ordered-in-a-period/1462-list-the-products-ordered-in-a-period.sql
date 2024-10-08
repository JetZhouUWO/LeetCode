# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products p right join Orders o on o.product_id = p.product_id
where order_date between "2020-02-01" and "2020-02-29"
group by product_name 
having unit >= 100