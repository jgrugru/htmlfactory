![Untitled-Artwork](https://user-images.githubusercontent.com/24437648/155743874-4187e556-7ac7-44eb-8d73-3420e9c58af6.png)

# htmlfactory     [![Build Status](https://travis-ci.com/jgrugru/htmlfactory.svg?branch=main)](https://travis-ci.com/jgrugru/htmlfactory)
A simple way to produce HTML with Python.
Source code can be found on [github](https://github.com/jgrugru/htmlfactory).
```Python
pip install htmlfactory
```

### basic tag example
```python
print(TagFactory("div.my-class"))
# <div class='my-class'></div>
```

To add content between tags, we can pass any object can be cast to a *str*.
```python
# pass a string
print(TagFactory("div.my-class", innerHTML='I am inside the div.'))
# <div class='my-class'>I am inside the div.</div>
```

```Python
# pass a TagFactory object
my_tag = TagFactory("div.my-class",  innerHTML=TagFactory("div", innerHTML="child tag"))
my_tag.print_html(pretty=True)

# <div class="my-class">
#   <div>
#     child tag
#   </div>
# </div>
```

### Add child element
You can add children using the *add_child* method.

```python
my_tag = TagFactory("div.class-1")
my_tag.add_child(TagFactory("div.class-2"))
print(my_tag)
# <div class='class-1'><div class='class-2'></div></div>
```

### Print Pretty HTML string
To print a TagFactory object, you can use `print(<TagFactoryObj>)` or `<TagFactoryObj>.print_html()`
If you would like to have a nicely formatted output, use the __pretty__ boolean flag with the __print_html()__ method:
```Python
my_tag = TagFactory("div", innerHTML=TagFactory("form"))
my_tag.print_html(pretty=True)

# <div>
#   <form>
#   </form>
# </div>
```

### Multiple classes example

You can add as many classes as you want to your tag object:
```Python
print(TagFactory("div.class1.class2.class3.class4.class5", innerHTML='I have a lot of classes.'))

# <div class='class1 class2 class3 class4 class5'>I have a lot of classes.</div>
```

###### adding attributes example

You can add attributes to your tab object by using keyword arguments:
```Python
TagFactory("form", innerHTML='I have an action & method attribute.', action="/action_page.php", method="get")
```

```html
<form action='/action_page.php' method='get'>I have an action and method attribute.</form>
```

### Creating tags without closing brackets example: Singletons

You can create tags without closing brackets, which may be useful if wanting to add an img or link. Use the singleton bool flag:
```Python
test_tag = TagFactory("img", singleton=True, border="0", alt="TestTag",
                      src="logo_w3s.gif", width="100",
                      height="100")
print(test_tag)

# <img border='0' alt='TestTag' src='fake_gif.gif' width='100' height='100'>
```
