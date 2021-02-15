# from html5print import HTMLBeautifier

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.dirname(__file__)))

from bs4 import BeautifulSoup
from InnerHtml import InnerHtml
from TagAttributeList import TagAttributeList


class TagFactory():
    """A tag object that has an html tag (ex: 'div'),
       inner_html ojbect (could be a single TagFactory ojbect
       or a list/tuple of other TagFactory objects or a string),
       and attribute list containing attribute objects."""

    def __init__(self, tag_and_class_str: str, inner_html = '',
                 **kwargs):
        self.inner_html = InnerHtml(inner_html)
        self.TagAttributeList = TagAttributeList(**kwargs)
        self.cleanse_tag_and_class_str(tag_and_class_str)

    def split_str_by_period(self, str):
        """Return the string split by periods.
        "div.col-md-10" becomes ["div", "col-md-10"]."""

        return str.split(".")

    def cleanse_tag_and_class_str(self, tag_and_class_str):
        """This function parses the tag and class string
           (example input: 'div.col-md-10.col-10')."""

        tag_and_class_list = self.split_str_by_period(tag_and_class_str)

        self.tag = tag_and_class_list[0]

        if len(tag_and_class_list) > 0:
            self.class_list = tag_and_class_list[1:]
        else:
            self.class_list = ''

    def class_concatenater(self, *args, **kwargs):
        """This function creates a string with all of the html
           classes concatenated together."""

        if(len(args) == 0):
            return ''
        return_class_str = " class="
        for counter, klass in enumerate(args):
            if counter == 0:
                return_class_str += "\'" + klass
            else:
                return_class_str += ' ' + klass
        return_class_str += "\'"
        return return_class_str

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
               + str(self.TagAttributeList) \
               + ">" + str(self.inner_html) + "</" + self.tag + ">"
        return html
        # return HTMLBeautifier.beautify(html, 2)
