# htmlfactory
A simple way to produce HTML with Python.

Can be installed through pip:
```pip install htmlfactory```


How to Create a Tag
-------------------
```print(TagFactory("div.col-10.col-lg-9.d-inline-block", (TagFactory("div.dish-network", 'inside the last div')), id="target-div"))```
---> output
><html>
>  <head>
>  </head>
>  <body>
>    <div class="col-10 col-lg-9 d-inline-block" id="target-div">
>      <div class="dish-network">
>        inside the last div
>      </div>
>    </div>
>  </body>
></html>



```
    body_tag_object = TagFactory("body", (
        TagFactory("div.col-10.col-lg-9.d-inline-block",
                   'inside the tags', id="target-div"),
        TagFactory("div.col-10.col-lg-3.d-inline-block",
                   'well how about that'),
        TagFactory("form.input-handler", (
            TagFactory("div.form-group", (
                TagFactory("label", 'Email Address', foor="exampleInputEmail1"),
                TagFactory("input.form-control", '', id="exampleInputEmail1", ariadescribedby="emailHelp", placeholder="Enter email"),
                TagFactory("small.form-text.text-muted", "We'll never share your email with anyone else.", id="emailHelp"),
            )),
            TagFactory("div.form-group", (
                TagFactory("label", 'Password', foor="exampleInputPassword1"),
                TagFactory("input.form-control", '', id="exampleInputPassword1", placeholder="Password"),
            )),
            TagFactory("div.form-check", (
                TagFactory("input.form-check-input", '', id="exampleCheck1"),
                TagFactory("label.form-check-label", 'Check me out', foor="exampleCheck1"),
            )),
            TagFactory("button.btn.btn-primary", 'Submit', type="submit")
        ))
    ))
    print(body_tag_object)
    """Expected output -->
        <html>
        <head>
        </head>
        <body>
            <div class="col-10 col-lg-9 d-inline-block" id="target-div">
            inside the tags
            </div>
            <div class="col-10 col-lg-3 d-inline-block">
            well how about that
            </div>
            <form class="input-handler">
            <div class="form-group">
                <labelfoor='exampleinputemail1'>
                Email Address
                </labelfoor='exampleinputemail1'>
                <input ariadescribedby="emailHelp" class="form-control" id="exampleInputEmail1" placeholder="Enter email">
                <small class="form-text text-muted" id="emailHelp">
                We'll never share your email with anyone else.
                </small>
            </div>
            <div class="form-group">
                <labelfoor='exampleinputpassword1'>
                Password
                </labelfoor='exampleinputpassword1'>
                <input class="form-control" id="exampleInputPassword1" placeholder="Password">
            </div>
            <div class="form-check">
                <input class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" foor="exampleCheck1">
                Check me out
                </label>
            </div>
            <button class="btn btn-primary" type="submit">
                Submit
            </button>
            </form>
        </body>
        </html>"""```



The class syntax for tags is based off of Emmet.
