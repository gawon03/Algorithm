-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT CATEGORY, MAX(PRICE)
                            FROM FOOD_PRODUCT
                            WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
                            GROUP BY CATEGORY)
ORDER BY PRICE DESC