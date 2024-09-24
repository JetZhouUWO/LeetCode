# Write your MySQL query statement below
select s.year as year, p.product_name as product_name, s.price as price
from Sales s left join Product p on s.product_id = p.product_id;