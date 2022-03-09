from htmlfactory_new.TagFactory import TagFactory, Tagged


def test_basic_tag_factory():
    test_tag = Tagged(raw_tag="div.testing")
    assert str(test_tag) == """<div class='testing'></div>"""


def test_tag_factory_inner_html():
    test_tag = Tagged(raw_tag="div.testing", innerHTML=TagFactory(raw_tag="div.test"))
    assert str(test_tag) == """<div class='testing'><div class='test'></div></div>"""


def test_tagged():
    test_tag = Tagged(
        "div.my-class", innerHTML=Tagged("form.bootstrap", target="/action.php")
    )
    assert (
        str(test_tag)
        == """<div class='my-class'><form class='bootstrap' target='/action.php'></form></div>"""
    )


def test_basic_tag():
    test_tag = Tagged(raw_tag="div")
    assert str(test_tag) == "<div></div>"


def test_multiple_classes():
    test_tag = Tagged(raw_tag="div.col-10.col-lg-9.d-inline-block")
    assert (
        str(test_tag)
        == """<div class='col-10 col-lg-9 """ + """d-inline-block'></div>"""
    )


def test_single_child():
    test_tag = Tagged(raw_tag="div", innerHTML=[Tagged(raw_tag="div-2")])
    assert str(test_tag) == """<div><div-2></div-2></div>"""


def test_inner_html_list():
    assert (
        str(
            Tagged(
                raw_tag="div.my-class",
                innerHTML=[Tagged(raw_tag="div", innerHTML=["child tag"])],
            )
        )
        == """<div class='my-class'><div>child tag</div></div>"""
    )


def test_inner_html_tuple():
    assert (
        str(
            Tagged(
                raw_tag="div.my-class",
                innerHTML=[Tagged(raw_tag="div", innerHTML="child tag")],
            )
        )
        == """<div class='my-class'><div>child tag</div></div>"""
    )


def test_basic_singleton_tag():
    test_tag = Tagged(raw_tag="div", singleton=True)
    assert str(test_tag) == "<div>"


def test_basic_singleton_tag_with_classes():
    test_tag = Tagged(raw_tag="div.test1.test2.test3.test4", singleton=True)
    assert str(test_tag) == "<div class='test1 test2 test3 test4'>"


def test_basic_singleton_tag_with_innerHTML():
    test_tag = Tagged(
        raw_tag="img.1.2.3.4",
        innerHTML=[Tagged(raw_tag="div.1", innerHTML=[Tagged(raw_tag="div.2")])],
        singleton=True,
    )
    print(test_tag)
    assert (
        str(test_tag)
        == "<img class='1 2 3 4'><div class='1'><div class='2'></div></div>"
    )


def test_attributes():
    test_tag = Tagged(
        raw_tag="div",
        innerHTML="I have an action and method attribute.",
        action="/action_page.php",
        method="get",
    )
    assert (
        str(test_tag)
        == """<div action='/action_page.php' method='get'>"""
        + "I have an action and method attribute.</div>"
    )


def test_link_tag():
    test_tag = Tagged(
        raw_tag="link",
        singleton=True,
        rel="stylesheet",
        href="https://stackpath.bootstrapcdn"
        + ".com/bootstrap/4.3.1/css/bootstrap.min.css",
        integrity="sha384-ggOyR0iXCbMQv3Xipma"
        + "34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T",
        crossorigin="anonymous",
    )
    assert (
        str(test_tag)
        == "<link rel='stylesheet'"
        + " href='https://stackpath.bootstrapcdn.com"
        + "/bootstrap/4.3.1/css/bootstrap.min.css'"
        + " integrity='sha384-ggOyR0iXCbMQv3Xipma3"
        + "4MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'"
        + " crossorigin='anonymous'>"
    )


def test_img_tag():
    test_tag = Tagged(
        raw_tag="img",
        singleton=True,
        border="0",
        alt="TestTag",
        src="logo_w3s.gif",
        width="100",
        height="100",
    )

    assert (
        str(test_tag)
        == """<img border='0' alt='TestTag'"""
        + """ src='logo_w3s.gif' width='100'"""
        + """ height='100'>"""
    )


def test_add_child_element():
    test_tag = Tagged(raw_tag="footer.footer")
    test_tag.add_child((Tagged(raw_tag="div.container")))
    assert (
        str(test_tag)
        == """<footer class='footer'>""" + """<div class='container'></div></footer>"""
    )


"""
def test_add_child_element_list():
    test_tag = Tagged(raw_tag="test_tag")
    child_tag = Tagged(raw_tag="div")
    child_list = []
    for x in range(3):
        child_list.append(child_tag)
    test_tag.add_child_element(child_list)
    assert (
        str(test_tag) == "<test_tag><div></div><div>" + "</div><div></div></test_tag>"
    )"""


def test_add_child_element_with_child_element():
    test_tag = Tagged(raw_tag="test_tag")
    test_tag.add_child(
        Tagged(raw_tag="div.container", innerHTML=[Tagged(raw_tag="div1")])
    )
    assert (
        str(test_tag)
        == """<test_tag><div class='container'>""" + "<div1></div1></div></test_tag>"
    )


def test_singleton_tag_add_with_child_element_list():
    body = Tagged(raw_tag="body")
    body.add_child(
        [Tagged(raw_tag="img", singleton=True), Tagged(raw_tag="img1", singleton=True)]
    )
    assert str(body) == "<body><img><img1></body>"


def test_singleton_tag_as_child_element():
    a_tag = Tagged(
        raw_tag="a",
        innerHTML=[
            Tagged(raw_tag="img", singleton=True, attributes={"src": "logo_w3s.gif"})
        ],
        attributes={"href": "www.google.com"},
    )
    assert (
        str(a_tag)
        == """<a href='www.google.com'>""" + """<img src='logo_w3s.gif'></a>"""
    )


def test_singleton_tag_with_add_child_element_function():
    img_tag = Tagged(raw_tag="img", singleton=True, attributes={"src": "logo_w3s.gif"})
    a_tag = Tagged(raw_tag="a", attributes={"href": "www.google.com"})
    a_tag.add_child(img_tag)
    assert (
        str(a_tag)
        == """<a href='www.google.com'>""" + """<img src='logo_w3s.gif'></a>"""
    )


def test_pretty_str():
    test_tag = Tagged(raw_tag="div", innerHTML=[Tagged(raw_tag="div-2")])
    assert test_tag.pretty_str() == """<div>\n <div-2>\n </div-2>\n</div>"""


def test_pretty_str_with_html_tags():
    test_tag = Tagged(raw_tag="div", innerHTML=[Tagged(raw_tag="div-2")])
    assert (
        test_tag.pretty_str(add_html_tags=True)
        == "<html>\n <head>\n </head>\n <body>\n  <div>\n"
        + "   <div-2>\n   </div-2>\n  </div>\n </body>\n</html>"
    )
