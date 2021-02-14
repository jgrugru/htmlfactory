# htmlfactory
A simple way to produce HTML with Python.

Can be installed through pip:
```pip install htmlfactory```


How to Create a Tag
-------------------
```print(TagFactory("div.col-10.col-lg-9.d-inline-block", (TagFactory("div.dish-network", 'inside the last div')), id="target-div"))```
---> output
```<html>
  <head>
  </head>
  <body>
    <div class="col-10 col-lg-9 d-inline-block" id="target-div">
      <div class="dish-network">
        inside the last div
      </div>
    </div>
  </body>
</html>```

The class syntax for tags is based off of Emmet.
