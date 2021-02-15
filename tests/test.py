
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory


def test_attributes():
    test_tag = TagFactory("div", 'I have an action and method attribute.',
                          action="/action_page.php", method="get")
    assert(str(test_tag) == '''<div action='/action_page.php' method='get'>'''
                            + '''I have an action and method attribute.</div>''')


def test_for_attribute():
    test_tag = TagFactory("div.my-class", "inside the div", four="my-form")
    assert(str(test_tag) == '''<div class='my-class\' '''
                            + '''for='my-form'>inside the div</div>''')


def test_multiple_classes():
    test_tag = TagFactory("div.col-10.col-lg-9.d-inline-block", '')
    assert(str(test_tag) == '''<div class='col-10 col-lg-9 '''
                            + '''d-inline-block'></div>''')


def test_single_tagfactory_child():
    test_tag = TagFactory('div', TagFactory('div-2', ''))
    assert(str(test_tag) == '''<div><div-2></div-2></div>''')

def test_inner_html_list():
    assert(str(TagFactory("div.my-class",
                          [TagFactory("div", "child tag")]))
           == '''<div class='my-class'><div>child tag</div></div>''')


def test_inner_html_tuple():
    assert(str(TagFactory("div.my-class",
                          (TagFactory("div", "child tag"))))
           == '''<div class='my-class'><div>child tag</div></div>''')


def test_pretty_str():
    test_tag = TagFactory('div', TagFactory('div-2', ''))
    assert(test_tag.pretty_str() == '''<div>\n <div-2>\n </div-2>\n</div>''')


def test_pretty_str_with_html_tags():
    test_tag = TagFactory('div', TagFactory('div-2', ''))
    assert(test_tag.pretty_str(add_html_tags=True) ==
           '<html>\n <head>\n </head>\n <body>\n  <div>\n'
           + '   <div-2>\n   </div-2>\n  </div>\n </body>\n</html>')



# def example_html_creation():
#     body_tag_object = TagFactory("body", (
#         TagFactory("div.col-10.col-lg-9.d-inline-block",
#                    'inside the tags', id="target-div"),
#         TagFactory("div.col-10.col-lg-3.d-inline-block",
#                    'well how about that'),
#         TagFactory("form.input-handler", (
#             TagFactory("div.form-group", (
#                 TagFactory("label", 'Email Address', foor="exampleInputEmail1"),
#                 TagFactory("input.form-control", '', id="exampleInputEmail1", ariadescribedby="emailHelp", placeholder="Enter email"),
#                 TagFactory("small.form-text.text-muted", "We'll never share your email with anyone else.", id="emailHelp"),
#             )),
#             TagFactory("div.form-group", (
#                 TagFactory("label", 'Password', foor="exampleInputPassword1"),
#                 TagFactory("input.form-control", '', id="exampleInputPassword1", placeholder="Password"),
#             )),
#             TagFactory("div.form-check", (
#                 TagFactory("input.form-check-input", '', id="exampleCheck1"),
#                 TagFactory("label.form-check-label", 'Check me out', foor="exampleCheck1"),
#             )),
#             TagFactory("button.btn.btn-primary", 'Submit', type="submit")
#         ))
#     ))
#     print(body_tag_object)
#     """Expected output -->
#         <html>
#         <head>
#         </head>
#         <body>
#             <div class="col-10 col-lg-9 d-inline-block" id="target-div">
#             inside the tags
#             </div>
#             <div class="col-10 col-lg-3 d-inline-block">
#             well how about that
#             </div>
#             <form class="input-handler">
#             <div class="form-group">
#                 <labelfoor='exampleinputemail1'>
#                 Email Address
#                 </labelfoor='exampleinputemail1'>
#                 <input ariadescribedby="emailHelp" class="form-control" id="exampleInputEmail1" placeholder="Enter email">
#                 <small class="form-text text-muted" id="emailHelp">
#                 We'll never share your email with anyone else.
#                 </small>
#             </div>
#             <div class="form-group">
#                 <labelfoor='exampleinputpassword1'>
#                 Password
#                 </labelfoor='exampleinputpassword1'>
#                 <input class="form-control" id="exampleInputPassword1" placeholder="Password">
#             </div>
#             <div class="form-check">
#                 <input class="form-check-input" id="exampleCheck1">
#                 <label class="form-check-label" foor="exampleCheck1">
#                 Check me out
#                 </label>
#             </div>
#             <butt"""

# print(TagFactory("div.parent-div", (TagFactory("div.first-child-div", (TagFactory("div.second-child-div", "It's party time."))))))
# print(TagFactory("div.tag1.tag2.tag3.tag4.tag5", 'I have a lot of classes.'))
# print(TagFactory("div", 'I have an action and method attribute.', action="/action_page.php", method="get"))
# print(TagAttributeDict(four="asdfasdf", id='asdf'))
# print(TagFactory("div.my-class", [TagFactory("div", "child tag")]))

# print(TagFactory("div.col-10.col-lg-9.d-inline-block", '', id="target-div"))"


# example_html_creation()
