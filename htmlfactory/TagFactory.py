import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.dirname(__file__)))

from bs4 import BeautifulSoup
from InnerHtml import InnerHtml
from TagAttributeList import TagAttributeList
from TagAndClassStr import TagAndClassStr
# from BaseTag import BaseTag


class TagFactory(TagAndClassStr, TagAttributeList):
    """A tag object that inherits from TagAndClassStr and TagAttributeList. 
    InnerHtml holds the child html elements or string between the opening and
    closing tags. TagAndClassStr extracts the tag and classes from 
    the inputted str, such as 'div.class1.class2'. The tag can be referenced by
    self.get_tag(), which following the above example returns 'div'. The
    TagAttributeList abstracts all the tags that are inputted as keyword
    arguments. The tags can be grabbed with self.get_tag_attributes_str()."""

    def __init__(self, tag_and_class_str: str, inner_html= '',
                 **kwargs):
        self.inner_html = InnerHtml()
        self.add_child_element(inner_html)
        TagAttributeList.__init__(self, **kwargs)
        TagAndClassStr.__init__(self, tag_and_class_str)

    def add_child_element(self, *args):
        for html_element in args:
            if type(html_element) == str:
                self.inner_html.set_to_str(html_element)
            elif type(html_element) == TagFactory:
                self.inner_html.add_tag_factory_object(html_element)
            if type(html_element) == list or type(html_element) == tuple:
                self.add_child_element(*html_element)

    def pretty_str(self, add_html_tags = False):
        if add_html_tags:
            soup = BeautifulSoup(str(self), features="html5lib")
        else:
            soup = BeautifulSoup(str(self), features="html.parser")
        return soup.prettify()

    def __str__(self):
        """This function produces the usable html."""
        html = "<" + self.tag \
               + self.class_concatenater(*self.class_list) \
               + str(self.get_tag_attributes_str()) \
               + ">" + str(self.inner_html) + "</" + self.tag + ">"
        return html
