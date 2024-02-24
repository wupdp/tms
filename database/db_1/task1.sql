SELECT an_name, an_price
FROM Analysis
JOIN Orders ON Analysis.an_id = Orders.ord_an
WHERE ord_datetime >= '2020-02-05' AND ord_datetime < '2020-02-13';
