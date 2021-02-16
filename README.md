# htmlfactory     [![Build Status](https://travis-ci.com/jgrugru/htmlfactory.svg?branch=main)](https://travis-ci.com/jgrugru/htmlfactory)
A simple way to produce HTML with Python.
Source code can be found on [github](https://github.com/jgrugru/htmlfactory).
```
pip install htmlfactory
```

**htmlfactory** makes making html easy to understand.

#### Examples:

###### basic div example
```
TagFactory("div.my-class")

# output:
<div class='my-class'></div>
```

To add content between the divs, we can pass a string or *TagFactory* objects.
```
# pass a string
TagFactory("div.my-class", 'I am inside the div.')

# output
<div class='my-class'>I am inside the div.</div>
```

```
# pass a TagFactory object
TagFactory("div.my-class",  TagFactory("div", "child tag"))

# output
<div class="my-class">
  <div>
    child tag
  </div>
</div>
```

###### children div example

pass a list of *TagFactory* objects
```
TagFactory("div.parent-div", [
      TagFactory("div.first-child-div", (
        TagFactory("div.second-child-div", "It's party time.")))])

# output:
<div class='parent-div'>
  <div class='first-child-div'>
    <div class='second-child-div'>
      It's party time.
    </div>
  </div>
</div>
```
>Note:
>Children tags can be passed through a list, tuple, or singular *TagFactory* object.

###### printing *TagFactory* objects

To output a TagFactory object, use print.
```
print(TagFactory('div', TagFactory('form')))
# output:
<div><form></form></div>
```

Use the function *pretty_str()* for an indented output.
```
print(TagFactory('div', TagFactory('form')).pretty_str())
#output:
# <div>
#   <form>
#   </form>
# </div>
```

If you would like an HTML, body, and head tag to be included, pass *add_html_tags=True*.
```
print(TagFactory('div', TagFactory('form')).pretty_str(add_html_tags=True))
# output:
# <html>
# <head>
# </head>
# <body>
#   <div>
#     <form>
#     </form>
#   </div>
# </body>
# </html>
```
###### multiple classes example

You can add as many classes as you want to your tag object:
```
TagFactory("div.class1.class2.class3.class4.class5", 'I have a lot of classes.')

# output:
<div class='class1 class2 class3 class4 class5'>I have a lot of classes.</div>
```
###### adding attributes example

You can add attributes to your tab object by using keyword arguments:
```
TagFactory("form", 'I have an action & method attribute.', action="/action_page.php", method="get")

# output:
<form action='/action_page.php' method='get'>I have an action and method attribute.</form>
```

>Note:
>'for' is a keyword so it cannot be used as a keyword argument. Instead use 'four'.
>Example: ```TagFactory("div.my-class", "inside the div", four="my-form")```

>Dashes (-) also cause a similar problem. For all html attributes that require a dash, 
>please omit the dash. The dash will be added upon creation of the object.

```
# with an omitted dash
TagFactory("div", role="application", ariadescribedby="info")

# output
<div role='application' aria-describedby='info'></div>
```