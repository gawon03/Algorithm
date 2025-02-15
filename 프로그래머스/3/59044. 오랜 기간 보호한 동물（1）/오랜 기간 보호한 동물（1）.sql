--아직 입양을 못 간 동물 중, 
--가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문
select *
from (select i.name, i.datetime
from animal_ins i 
left join animal_outs o on i.animal_id = o.animal_id
where o.animal_id is null
order by i.datetime )
where rownum <= 3