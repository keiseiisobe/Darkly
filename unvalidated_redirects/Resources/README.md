# Unvalidated Redirects
Dangerous Java code
```
response.sendRedirect(request.getParameter("url"));
```

## vulnerability
> Unvalidated redirects and forwards are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input. By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials.
>
> see https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html


## exploit
Home

```
<li>
	<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>
</li>
```

1. An attacker sent "http://trusted-site.com/index.php?page=redirect&site=malicious-site.com".
2. A user see "trusted-site.com" in the link, and trust it.
3. The user click link, and visit redirected malicious site.
4. When the user enters some credentials in the site, these information can be stolen.


## reference
* https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
