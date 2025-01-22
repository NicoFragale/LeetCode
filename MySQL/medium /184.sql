'''
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.


'''

with cte as (
    select d.name, max(e.salary) as salary, e.departmentId as did
    from Department d 
    join Employee e on e.departmentId = d.id
    group by d.name
)
select e.name as Department, e1.name as Employee, e.salary as Salary
from cte e 
join Employee e1 on e.did = e1.departmentId
where e1.salary = e.salary