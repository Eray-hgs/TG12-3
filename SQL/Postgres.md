``` 
CREATE TABLE dorf (
  dorfnr INTEGER PRIMARY KEY,
  name TEXT,
  haeuptling INTEGER
);
```
> ``` status
> CREATE TABLE
> ```

``` 
CREATE TABLE bewohner (
  bewohnernr INTEGER PRIMARY KEY,
  name TEXT,
  dorfnr INTEGER,
  geschlecht CHAR(1),
  beruf TEXT,
  gold INTEGER,
  status TEXT
);
```
> ``` status
> CREATE TABLE
> ```

``` 
CREATE TABLE gegenstand (
  gegenstand TEXT PRIMARY KEY,
  besitzer INTEGER
);
```
> ``` status
> CREATE TABLE
> ```

``` 
INSERT INTO dorf (dorfnr, name, haeuptling) VALUES
(1, 'Affenstadt', 1),
(2, 'Gurkendorf', 6),
(3, 'Zwiebelhausen', 13);
```
> ``` status
> INSERT 0 3
> ```

``` 
INSERT INTO bewohner (bewohnernr, name, dorfnr, geschlecht, beruf, gold, status) VALUES
(1, 'Paul Backmann', 1, 'm', 'Baecker', 850, 'friedlich'),
(2, 'Ernst Peng', 3, 'm', 'Waffenschmied', 280, 'friedlich'),
(3, 'Rita Ochse', 1, 'w', 'Baecker', 350, 'friedlich'),
(4, 'Carl Ochse', 1, 'm', 'Kaufmann', 250, 'friedlich'),
(5, 'Dirty Dieter', 3, 'm', 'Schmied', 650, 'boese'),
(6, 'Gerd Schlachter', 2, 'm', 'Metzger', 4850, 'boese'),
(7, 'Peter Schlachter', 3, 'm', 'Metzger', 3250, 'boese'),
(8, 'Arthur Schneiderpaule', 2, 'm', 'Pilot', 490, 'gefangen'),
(9, 'Tanja Trommler', 1, 'w', 'Baecker', 550, 'boese'),
(10, 'Peter Trommler', 1, 'm', 'Schmied', 600, 'friedlich'),
(11, 'Dirty Doerthe', 3, 'w', 'Erntehelfer', 10, 'boese'),
(12, 'Otto Armleuchter', 2, 'm', 'Haendler', 680, 'friedlich'),
(13, 'Fritz Dichter', 3, 'm', 'Hoerbuchautor', 420, 'friedlich'),
(14, 'Enrico Zimmermann', 3, 'm', 'Waffenschmied', 510, 'boese'),
(15, 'Helga Rasenkopf', 2, 'w', 'Haendler', 680, 'friedlich'),
(16, 'Irene Hutmacher', 1, 'w', 'Haendler', 770, 'boese'),
(17, 'Erich Rasenkopf', 3, 'm', 'Metzger', 990, 'friedlich'),
(18, 'Rudolf Gaul', 3, 'm', 'Hufschmied', 390, 'friedlich'),
(19, 'Anna Flysh', 2, 'w', 'Metzger', 2280, 'friedlich');
```
> ``` status
> INSERT 0 19
> ```

``` 
INSERT INTO gegenstand (gegenstand, besitzer) VALUES
('Teekanne', NULL),
('Spazierstock', 5),
('Hammer', 2),
('Ring', NULL),
('Kaffeetasse', NULL),
('Eimer', NULL),
('Seil', 17),
('Pappkarton', NULL),
('Gluehbirne', NULL);
```
> ``` status
> INSERT 0 9
> ```

``` 
SELECT * FROM Bewohner
```
| bewohnernr | name | dorfnr | geschlecht | beruf | gold | status |
|-----------:|:-----|-------:|:-----------|:------|-----:|:-------|
| 1 | Paul Backmann | 1 | m | Baecker | 850 | friedlich |
| 2 | Ernst Peng | 3 | m | Waffenschmied | 280 | friedlich |
| 3 | Rita Ochse | 1 | w | Baecker | 350 | friedlich |
| 4 | Carl Ochse | 1 | m | Kaufmann | 250 | friedlich |
| 5 | Dirty Dieter | 3 | m | Schmied | 650 | boese |
| 6 | Gerd Schlachter | 2 | m | Metzger | 4850 | boese |
| 7 | Peter Schlachter | 3 | m | Metzger | 3250 | boese |
| 8 | Arthur Schneiderpaule | 2 | m | Pilot | 490 | gefangen |
| 9 | Tanja Trommler | 1 | w | Baecker | 550 | boese |
| 10 | Peter Trommler | 1 | m | Schmied | 600 | friedlich |
| 11 | Dirty Doerthe | 3 | w | Erntehelfer | 10 | boese |
| 12 | Otto Armleuchter | 2 | m | Haendler | 680 | friedlich |
| 13 | Fritz Dichter | 3 | m | Hoerbuchautor | 420 | friedlich |
| 14 | Enrico Zimmermann | 3 | m | Waffenschmied | 510 | boese |
| 15 | Helga Rasenkopf | 2 | w | Haendler | 680 | friedlich |
| 16 | Irene Hutmacher | 1 | w | Haendler | 770 | boese |
| 17 | Erich Rasenkopf | 3 | m | Metzger | 990 | friedlich |
| 18 | Rudolf Gaul | 3 | m | Hufschmied | 390 | friedlich |
| 19 | Anna Flysh | 2 | w | Metzger | 2280 | friedlich |
> ``` status
> SELECT 19
> ```

``` 
SELECT * FROM Dorf
```
| dorfnr | name | haeuptling |
|-------:|:-----|-----------:|
| 1 | Affenstadt | 1 |
| 2 | Gurkendorf | 6 |
| 3 | Zwiebelhausen | 13 |
> ``` status
> SELECT 3
> ```

``` 
SELECT * FROM Gegenstand
```
| gegenstand | besitzer |
|:-----------|---------:|
| Teekanne | *null* |
| Spazierstock | 5 |
| Hammer | 2 |
| Ring | *null* |
| Kaffeetasse | *null* |
| Eimer | *null* |
| Seil | 17 |
| Pappkarton | *null* |
| Gluehbirne | *null* |
> ``` status
> SELECT 9
> ```

[fiddle](https://dbfiddle.uk/fDzQm6KA)
