# Reflected XSS
> Reflected Cross-site Scripting (XSS) occur when an attacker injects browser executable code within a single HTTP response. The injected attack is not stored within the application itself
>
> see [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)

## vulnerability
Home -> http://localhost/?page=media&src=nsa

1. If src parameter is echoed in HTML or Javascript code without proper sanitization, an attacker can inject malicious scripts.
2. Use Data URLs to create embed small file inline in documents `<script>alert("hi")</script>`. (see [here](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data))
3. encode it with base64.
4. Inject it. `http://localhost/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGkiKTwvc2NyaXB0Pg==`

## reference
* https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting
* https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data
