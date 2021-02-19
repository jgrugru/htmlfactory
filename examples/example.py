import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory
from htmlfactory.TagAndClassStr import TagAndClassStr


def example_html_creation():
    body_tag_object = TagFactory("body", (
        TagFactory("div.col-10.col-lg-9.d-inline-block",
                   'inside the tags', id="target-div"),
        TagFactory("div.col-10.col-lg-3.d-inline-block",
                   'well how about that'),
        TagFactory("form.input-handler", (
            TagFactory("div.form-group", (
                TagFactory("label", 'Email Address', four="exampleInputEmail1"),
                TagFactory("input.form-control", '', id="exampleInputEmail1", ariadescribedby="emailHelp", placeholder="Enter email"),
                TagFactory("small.form-text.text-muted", "We'll never share your email with anyone else.", id="emailHelp"),
            )),
            TagFactory("div.form-group", (
                TagFactory("label", 'Password', four="exampleInputPassword1"),
                TagFactory("input.form-control", '', id="exampleInputPassword1", placeholder="Password"),
            )),
            TagFactory("div.form-check", (
                TagFactory("input.form-check-input", '', id="exampleCheck1"),
                TagFactory("label.form-check-label", 'Check me out', four="exampleCheck1"),
            )),
            TagFactory("button.btn.btn-primary", 'Submit', type="submit")
        ))
    ))
    print(body_tag_object.pretty_str())
"""
<body>
 <div class="col-10 col-lg-9 d-inline-block" id="target-div">
  inside the tags
 </div>
 <div class="col-10 col-lg-3 d-inline-block">
  well how about that
 </div>
 <form class="input-handler">
  <div class="form-group">
   <label for="exampleInputEmail1">
    Email Address
   </label>
   <input aria-describedby="emailHelp" class="form-control" id="exampleInputEmail1" placeholder="Enter email"/>
   <small class="form-text text-muted" id="emailHelp">
    We'll never share your email with anyone else.
   </small>
  </div>
  <div class="form-group">
   <label for="exampleInputPassword1">
    Password
   </label>
   <input class="form-control" id="exampleInputPassword1" placeholder="Password"/>
  </div>
  <div class="form-check">
   <input class="form-check-input" id="exampleCheck1"/>
   <label class="form-check-label" for="exampleCheck1">
    Check me out
   </label>
  </div>
  <button class="btn btn-primary" type="submit">
   Submit
  </button>
 </form>
</body>
"""

# example_html_creation()


def example_html_creation1():
    body_tag = TagFactory("body")
    body_tag.add_child_element(TagFactory("div.container", TagFactory("div.jumbotron")))
    print(body_tag.pretty_str(add_html_tags=True))

example_html_creation1()