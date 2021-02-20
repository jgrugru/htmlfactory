import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory
from htmlfactory.SingletonTag import SingletonTag


def setup_function(function):
    print("Setting up", function)


def test_basic_tag():
    test_tag = TagFactory("div")
    assert(str(test_tag) == '<div></div>')


def test_attributes():
    test_tag = TagFactory("div", 'I have an action and method attribute.',
                          action="/action_page.php", method="get")
    assert(str(test_tag) == '''<div action='/action_page.php' method='get'>'''
                            + 'I have an action and method attribute.</div>')


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


def test_omitted_dash():
    test_tag = TagFactory("div", '', role="application",
                          ariadescribedby="info")
    assert(str(test_tag) == '''<div role='application' '''
                            + '''aria-describedby='info'></div>''')


def test_add_child_element():
    test_tag = TagFactory("footer.footer")
    test_tag.add_child_element((TagFactory("div.container")))
    assert(str(test_tag) == '''<footer class='footer'>'''
                            + '''<div class='container'></div></footer>''')


def test_add_child_element_list():
    test_tag = TagFactory("test_tag")
    child_tag = TagFactory("div")
    child_list = []
    for x in range(3):
        child_list.append(child_tag)
    test_tag.add_child_element(child_list)
    assert(str(test_tag) == '<test_tag><div></div><div>'
                            + '</div><div></div></test_tag>')


def test_add_child_element_with_child_element():
    test_tag = TagFactory("test_tag")
    test_tag.add_child_element(TagFactory("div.container", TagFactory("div1")))
    assert(str(test_tag) == '''<test_tag><div class='container'>'''
                            + '<div1></div1></div></test_tag>')


def test_add_child_element_with_multiple_child_tags():
    test_tag = TagFactory("test_tag")
    test_tag.add_child_element([
        TagFactory("div.container",
                   TagFactory("div1",
                              TagFactory("div2",
                                         TagFactory("div3",
                                                    TagFactory("div4")))))
    ])
    assert(str(test_tag) == '''<test_tag><div class='container'><div1><div2>'''
                            + '<div3><div4></div4></div3></div2>'
                            + '</div1></div></test_tag>')


def test_add_child_element_with_existing_child_element():
    test_tag = TagFactory("test_tag", TagFactory("div"))
    test_tag.add_child_element(TagFactory("child"))
    assert(str(test_tag) == '<test_tag><div></div><child></child></test_tag>')


def test_set_str_as_child_element_after_setting_child_tag():
    test_tag = TagFactory("test_tag", TagFactory("div"))
    test_tag.add_child_element("This is a test string.")
    assert(str(test_tag) == '<test_tag>This is a test string.</test_tag>')


def test_basic_singleton_tag():
    test_tag = SingletonTag("div")
    assert(str(test_tag) == '<div>')


def test_link_tag():
    test_tag = SingletonTag('link', rel="stylesheet",
                            href="https://stackpath.bootstrapcdn"
                            + ".com/bootstrap/4.3.1/css/bootstrap.min.css",
                            integrity="sha384-ggOyR0iXCbMQv3Xipma"
                            + "34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T",
                            crossorigin="anonymous")
    assert(str(test_tag) == "<link rel='stylesheet\'"
                            + " href=\'https://stackpath.bootstrapcdn.com"
                            + "/bootstrap/4.3.1/css/bootstrap.min.css\'"
                            + " integrity=\'sha384-ggOyR0iXCbMQv3Xipma3"
                            + "4MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T\'"
                            + " crossorigin=\'anonymous\'>")


def test_img_tag():
    test_tag = SingletonTag("img", border="0", alt="TestTag",
                            src="logo_w3s.gif", width="100",
                            height="100")

    assert(str(test_tag) == """<img border='0' alt='TestTag'"""
                            + """ src='logo_w3s.gif' width='100'"""
                            + """ height='100'>""")


def test_singleton_tag_as_child_element():
    a_tag = TagFactory("a", SingletonTag("img", src="logo_w3s.gif"),
                       href="www.google.com")
    assert(str(a_tag) == """<a href='www.google.com'>"""
                         + """<img src='logo_w3s.gif'></a>""")


def test_singleton_tag_with_add_child_element_function():
    img_tag = SingletonTag("img", src="logo_w3s.gif")
    a_tag = TagFactory("a", href="www.google.com")
    a_tag.add_child_element(img_tag)
    assert(str(a_tag) == """<a href='www.google.com'>"""
                         + """<img src='logo_w3s.gif'></a>""")
