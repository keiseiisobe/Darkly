# Authorization With Cookie

## vulnerability
> Identify Application Entry Points:
> 
> Identify where new cookies are set (Set-Cookie header), modified, or added to.
> 
> see https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/06-Identify_Application_Entry_Points

## exploit
Home

1. see request header in Developer tool.
```
cookie: security=low; I_am_admin=68934a3e9455fa72420237eb05902327
```
2. apply md5 decoding to I_am_admin value, then get "false".
3. go to Developer tools -> Application -> Storage -> Cookies
4. set cookie I_am_admin=<"true" with md5 encoding>


Change the mail value to other value.

## reference
* https://owasp.org/Top10/A01_2021-Broken_Access_Control/
