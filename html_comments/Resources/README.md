# HTML Comments

## vulnerability
> HTML comments are often used by the developers to include debugging information about the application. Sometimes, they forget about the comments and they leave them in production environments. Testers should look for HTML comments which start with <!--.
>
> see [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage)

## execute
Home -> BortToSec at the bottom of page

We can see these comments.
```
<!--
You must come from : "https://www.nsa.gov/".
-->
...
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
```
shell % curl --user-agent ft_bornToSec --referer https://www.nsa.gov/ "http://localhost/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" 
```

## reference
* https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage
