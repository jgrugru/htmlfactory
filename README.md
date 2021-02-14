# htmlfactory
A simple way to produce HTML with Python.

Can be installed through pip:
```
pip install htmlfactory
```

Htmlfactory produces HTML through the class *TagFactory*.

>A *TagFactory* object that has an html tag (ex: 'div'),
>inner_html ojbect (could be a list of other tag objects or a string),
>and an attribute list containing attribute objects(ex: id="email-input").

###### Behind the scenes
*TagFactory* is very easy to understand.
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

```
  def __init__(self, tag_and_class_str: str, inner_html, **kwargs):
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
