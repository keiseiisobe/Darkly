# Invalid Input

## vlunerability
Home -> Servey

```
<form action="#" method="post">
					<input type="hidden" name="sujet" value="2">
					<select name="valeur" onchange="javascript:this.form.submit();">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
						<option value="10">10</option>
					</select>
				</form>
```

1. change the value of option tag.
2. trigger javascript:this.form.submit() to send the value changed.
3. If server does not validate the user input correctly, an attacker can edit the database.

## reference
