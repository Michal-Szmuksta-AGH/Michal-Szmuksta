1. Ile rekordów znajduje się w tabeli nyc_streets?

  Odp.: W tabeli nyc_streets znajduje się 19019 rekordów.
Odpowiedź na to pytanie uzyskano wykonując następujące zapytanie:

- SELECT count(*) FROM "public"."nyc_streets"

2. Ile ulic w Nowym Jorku ma nazwy zaczynające się na „B”, „Q” i „M”?

  Odp.: W Nowym Jorku znajdują się 1282 ulice zaczynające się na "B", 68 ulic zaczynających się na "Q" i 752 ulice zaczynające się na "M".
Odpowiedź na to pytanie uzyskano wykonując następujące zapytania:

- SELECT count(*) FROM "public"."nyc_streets" WHERE name LIKE 'B%'
- SELECT count(*) FROM "public"."nyc_streets" WHERE name LIKE 'Q%'
- SELECT count(*) FROM "public"."nyc_streets" WHERE name LIKE 'M%'

3. Jaka jest populacja miasta Nowy Jork?

  Odp.: Populacja miasta Nowy Jork wynosi 8175032 ludzi.
Odpowiedź na to pytanie uzyskano wykonując następujące zapytanie:

- SELECT sum(popn_total) FROM "public"."nyc_census_blocks"

4. Jaka jest populacja Bronxu, Manhattanu i Queens?

  Odp.: Populacja Bronxu wynosi 1385108 ludzi, Manhattanu 1585873, a Queens 2230621.
Odpowiedź na to pytanie uzyskano wykonując następujące zapytania:

- SELECT sum(popn_total) FROM "public"."nyc_census_blocks" WHERE boroname = 'The Bronx'
- SELECT sum(popn_total) FROM "public"."nyc_census_blocks" WHERE boroname = 'Manhattan'
- SELECT sum(popn_total) FROM "public"."nyc_census_blocks" WHERE boroname = 'Queens'

5. Ile dzielnic ("neighborhoods") znajduje się w każdej gminie (borough)?

  Odp.: W gminie Queens znajduje się 30 dzielnic, w gminie Brooklyn 23, w gminie Staten Island 24, w gminie The Bronx 24, a w gminie Manhattan 28.
Odpowiedź na to pytanie uzyskano wykonując następujące zapytanie:

- SELECT boroname, count(name) FROM "public"."nyc_neighborhoods" GROUP BY boroname
