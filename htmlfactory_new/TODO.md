TODO List
=======================
- Rename variables/classes to more understandable/contextual names.
- Add additional functionality so that the user can have the ability to pass classes as an argument.
- shouldn't have to have key word args
- the parsing of the string needs to be separated from HTMLElement and HTMLTag. Those are the core elements, all optional functionality should be calculated before that.
Ideas
-----------
form("Q group signup", fields=[("first name", "text"), ("last name", "text"), ("description", "textarea")])
--->
```html
<h1>Q group signup</h1>
<form action="/action_page.php">
  <label for="first_name">first name:</label><br>
  <input type="text" id="first_name" name="first_name"><br>
  <label for="last_name">last name:</label><br>
  <input type="text" id="last_name" name="last_name"><br><br>
  <h3>description:</h3>
  <textarea name="description" rows="10" cols="30">Description</textarea>
  <input type="submit" value="Submit">
</form> 
```