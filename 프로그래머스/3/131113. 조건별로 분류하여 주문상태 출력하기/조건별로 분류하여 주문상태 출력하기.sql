select order_id, product_id, to_char(out_date, 'YYYY-MM-DD') as out_date
, case when out_date <= to_date('2022-05-01', 'YYYY-MM-DD') then '출고완료'
       when out_date is null then '출고미정'
       else '출고대기' end as "출고여부"
from food_order
order by order_id













-- SELECT ORDER_ID, PRODUCT_ID, TO_CHAR(OUT_DATE, 'YYYY-MM-DD') AS OURT_DATE
-- , CASE WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') <= '2022-05-01' THEN '출고완료'
--        WHEN TO_CHAR(OUT_DATE, 'YYYY-MM-DD') > '2022-05-01' THEN '출고대기'
--        ELSE '출고미정' END AS "출고여부"
-- FROM FOOD_ORDER 
-- ORDER BY ORDER_ID
-- ;