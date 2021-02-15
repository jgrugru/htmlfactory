import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory


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


example_html_creation()