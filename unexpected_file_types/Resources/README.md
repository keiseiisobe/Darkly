# Upload of Unexpected File Types
> Many applications’ business processes allow for the upload and manipulation of data that is submitted via files. But the business process must check the files and only allow certain “approved” file types.
>
> see [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)

## vulnerability
> The application may be expecting only certain file types to be uploaded for processing, such as .csv or .txt files. The application may not validate the uploaded file by extension (for low assurance file validation) or content (high assurance file validation). This may result in unexpected system or database results within the application/system or give attackers additional methods to exploit the application/system.

```bash
# test.php can be a malicious script.
shell % curl -X POST -F "uploaded=@test.php;type=image/jpg" -F "Upload=Upload" "http://localhost/index.php?page=upload" | grep flag
```

## reference
* https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types
