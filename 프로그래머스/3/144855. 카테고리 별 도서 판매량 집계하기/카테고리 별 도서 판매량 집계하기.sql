select b.category
, nvl(sum(case when to_char(sales_date, 'YYYY-MM') = '2022-01' then s.sales
               else null end), 0) as total_sales
from book b 
left join book_sales s on b.book_id = s.book_id
group by b.category
order by b.category