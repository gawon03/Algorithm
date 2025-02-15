select order_id, product_id, to_char(out_date, 'YYYY-MM-DD') as out_date
, case when out_date <= to_date('2022-05-01', 'YYYY-MM-DD') then '출고완료'
       when out_date is null then '출고미정'
       else '출고대기' end as "출고여부"
from food_order
order by order_id;