# Robots
> In order for search engines to work, computer programs (or robots) regularly fetch data (referred to as crawling) from billions of pages on the web. These programs find web content and functionality by following links from other pages, or by looking at sitemaps. If a site uses a special file called robots.txt to list pages that it does not want search engines to fetch, then the pages listed there will be ignored.
>
> see [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage)

## vulnerability
> The robots.txt file is retrieved from the web root directory of the web server.
>
> see [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage)

1. access http://localhost/robots.txt.
2. In the /whatever dir, you can get root password.
3. apply md5 decoding.
4. access http://localhost/admin/, and login!

## reference
* https://developers.google.com/search/docs/fundamentals/how-search-works?hl=en&visit_id=638841597927998574-827997521&rd=1#indexing
* https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage
