# htmlfactory
A simple way to produce HTML with Python.

Can be installed through pip:
```
pip install htmlfactory
```

**htmlfactory** makes making html easy to understand. There is no need to overcomplicate the production of a tag-based file.

#### Examples:

###### basic div example
```
TagFactory("div.my-class", '')

# output:
<div class='my-class'></div>
```

To add content between the divs, we can pass *TagFactory* objects or a string.
```
TagFactory("div.my-class", 'I'm inside the div.')

# output
<div class='my-class'>I'm inside the div.</div>
```

###### children tags example

```
print(TagFactory("div.parent-div", (
      TagFactory("div.first-child-div", (
        TagFactory("div.second-child-div", "It's party time."))))))

# output:
<div class='parent-div'>
  <div class='first-child-div'>
    <div class='second-child-div'>
      It's party time.
    </div>
  </div>
</div>
```

###### multiple classes example

You can add as many classes as you want to your tag object:
```
TagFactory("div.tag1.tag2.tag3.tag4.tag5", 'I have a lot of classes.')

# output:
<div class='tag1 tag2 tag3 tag4 tag5'>I have a lot of classes.</div>
```

You can add attributes to your tab object by using keyword arguments:
```
TagFactory("form", 'I have an action and method attribute.')

# output:
<form action='/action_page.php' method='get'>I have an action and method attribute.</form>
```

#### Behind the scenes
**htmlfactory** produces HTML through the class *TagFactory*.

>A *TagFactory* object consists of an html tag (ex: 'div'),
>inner_html object (*InnerHtml* object which accepts a list/tuple of other *TagFactory* objects or a string),
>and an attribute list (*TagAttributeList* object) containing *TagAttribute* objects (ex: id="email-input").

**__init__ function header for TagFactory**
```
  def __init__(self, tag_and_class_str: str, inner_html, **kwargs):
```
- The *tag_and_class_str* accepts a string with this format "*<tag>*.class1.class2.class3". An example would be "div.form-group.col-md-10" which produces this output: class="form-group col-md-10"
- The *inner_html* parameter accepts either a list/tuple of TagFactory objects or a string. Passing TagFactory objects will make them a child tag. For example:
```
TagFactory("div", (TagFactory("div, "child div")))
```
produces
```
<div class='parent-div'>
  <div class='child-div'>
  </div>
</div>
```

How to Create a Tag
-------------------
```
print(TagFactory("div.col-10.col-lg-9.d-inline-block",
         (TagFactory("div.dish-network",
          'inside the last div')),
          id="target-div"))
```

Output:

```
<html>
  <head>
  </head>
  <body>
    <div class="col-10 col-lg-9 d-inline-block" id="target-div">
      <div class="dish-network">
        inside the last div
      </div>
    </div>
  </body>
</html>
```

The class syntax for tags is based off of Emmet.
