select distinct h.car_id
from car_rental_company_car c 
left join car_rental_company_rental_history h on h.car_id = c.car_id
where to_char(h.start_date, 'MM') = '10'
and c.car_type = '세단'
order by h.car_id desc