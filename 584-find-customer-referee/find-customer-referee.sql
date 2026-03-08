-- Write your PostgreSQL query statement below
Select name from customer 
where referee_id is null or referee_id != '2'
