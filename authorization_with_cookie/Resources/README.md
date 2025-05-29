# Cookie
<input type="hidden" ...>

## vulnerability
> Warning: While the value isn't displayed to the user in the page's content, it is visible—and can be edited—using any browser's developer tools or "View Source" functionality. Do not rely on hidden inputs as a form of security.
> 
> see https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden

## exploit
Home -> Sign In -> I forgot my password

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

Change the mail value to other value.

## reference
* https://owasp.org/Top10/A01_2021-Broken_Access_Control/
* https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden
