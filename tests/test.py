import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory


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
    assert(str(test_tag) == '''<footer class='footer'><div class='container'></div></footer>''')


def test_add_child_element_list():
    test_tag = TagFactory("test_tag")
    child_tag = TagFactory("div")
    child_list = []
    for x in range(3):
        child_list.append(child_tag)
    test_tag.add_child_element(child_list)
    assert(str(test_tag) == '''<test_tag><div></div><div></div><div></div></test_tag>''')

def test_add_child_element_with_child_element():
    test_tag = TagFactory("test_tag")
    test_tag.add_child_element([
      TagFactory("div.container", TagFactory("div1"))
    ])
    assert(str(test_tag) == '''<test_tag><div class='container'><div1></div1></div></test_tag>''')

def test_add_child_element_recursion():
    test_tag = TagFactory("test_tag")
    test_tag.add_child_element([
      TagFactory("div.container",
        TagFactory("div1",
          TagFactory("div2",
            TagFactory("div3",
              TagFactory("div4")))))
    ])
    assert(str(test_tag) == '''<test_tag><div class='container'><div1><div2><div3><div4></div4></div3></div2></div1></div></test_tag>''')
