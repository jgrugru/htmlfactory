class TagFactory():
    """A tag object that has a tag, inner_html, and attribute dictionary."""
    def __init__(self, tag_and_class_str: str, inner_html,
                 children=(), **kwargs):
        self.list_of_tags = ("body", "document", "div", "h1", "form",
                             "input", "small", "button", "label")
        self.inner_html = inner_html
        self.attr_dict = kwargs
        self.cleanse_tag_and_class_str(tag_and_class_str)
        self.children = children

    def split_str_by_period(self, str):
        return str.split(".")

    def cleanse_tag_and_class_str(self, tag_and_class_str):
        """This function parses the tag and class string
           (ex. 'div.col-md-10.col-10')."""
        tag_and_class_list = self.split_str_by_period(tag_and_class_str)
        if tag_and_class_list[0] in self.list_of_tags:
            self.tag = tag_and_class_list[0]
        else:
            self.tag = None

        if len(tag_and_class_list) > 0:
            self.class_list = tag_and_class_list[1:]
        else:
            self.class_list = ''

    def attr_concatenater(self, *args, **kwargs):
        """This function creates a string with all of the html
           attributes concatenated together."""
        if(len(args) == 0 and len(kwargs) == 0):
            return ''
        attr_str = " class="
        for counter, klass in enumerate(args):
            if counter == 0:
                attr_str += "\'" + klass
            else:
                attr_str += ' ' + klass
        attr_str += "\'"
        for attr in kwargs:
            attr_str += ' ' + attr + '=' + "\'" + kwargs[attr] + "\'"
        return attr_str

    def concatenate_children(self):
        inside_tags_str = ""
        if(self.children):
            for tag_object in self.children:
                inside_tags_str += str(tag_object) + '\n'
        return inside_tags_str

    def __str__(self):
        """This function produces the usable html."""
        return "<" + self.tag \
               + self.attr_concatenater(*self.class_list, **self.attr_dict) \
               + ">" + self.inner_html + self.concatenate_children() \
               + "</" + self.tag + ">"


def test_ouput():
    assert(str(TagFactory("div.col-10.col-lg-9.d-inline-block",
           'inside the tags', id="target-div"))
           == "<div class='col-10 col-lg-9 d-inline-block'"
           + " id='target-div'>inside the tags</div>")


def example_html_creation():
    body_tag_object = TagFactory("body", '', (
        TagFactory("div.col-10.col-lg-9.d-inline-block",
                   'inside the tags', id="target-div"),
        TagFactory("div.col-10.col-lg-3.d-inline-block",
                   'well how about that'),
        TagFactory("form.input-handler", '', (
            TagFactory("div.form-group", '', (
                TagFactory("label", 'Email Address', foor="exampleInputEmail1"),
                TagFactory("input.form-control", '', id="exampleInputEmail1", ariadescribedby="emailHelp", placeholder="Enter email"),
                TagFactory("small.form-text.text-muted", "We'll never share your email with anyone else.", id="emailHelp"),
            )),
            TagFactory("div.form-group", '', (
                TagFactory("label", 'Password', foor="exampleInputPassword1"),
                TagFactory("input.form-control", '', id="exampleInputPassword1", placeholder="Password"),
            )),
            TagFactory("div.form-check", '', (
                TagFactory("input.form-check-input", '', id="exampleCheck1"),
                TagFactory("label.form-check-label", 'Check me out', foor="exampleCheck1"),
            )),
            TagFactory("button.btn.btn-primary", 'Submit', type="submit")
        ))
    ))
    print(body_tag_object)
    """Expected output -->
    <body>
        <div class='col-10 col-lg-9 d-inline-block' id='target-div'>inside the tags</div>
        <div class='col-10 col-lg-3 d-inline-block'>well how about that</div>
        <form class='input-handler'>
            <div class='form-group'><label class=' foor='exampleInputEmail1'>Email Address</label>
                <input class='form-control' id='exampleInputEmail1' ariadescribedby='emailHelp' placeholder='Enter email'></input>
                <small class='form-text text-muted' id='emailHelp'>We'll never share your email with anyone else.</small>
            </div>
            <div class='form-group'><label class=' foor='exampleInputPassword1'>Password</label>
                <input class='form-control' id='exampleInputPassword1' placeholder='Password'></input>
            </div>
            <div class='form-check'><input class='form-check-input' id='exampleCheck1'></input>
                <label class='form-check-label' foor='exampleCheck1'>Check me out</label>
            </div>
            <button class='btn btn-primary' type='submit'>Submit</button>
        </form>
    </body>"""


example_html_creation()
