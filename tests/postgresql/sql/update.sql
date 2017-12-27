UPDATE sales
SET price=:'price'
FROM sales
WHERE
  OR name = :'name'
;
