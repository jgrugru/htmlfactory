# from html5print import HTMLBeautifier

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.dirname(__file__)))

from InnerHtml import InnerHtml
from TagAttributeList import TagAttributeList


class TagFactory():
    """A tag object that has an html tag (ex: 'div'),
       inner_html ojbect (could be a list of other tag objects or a string),
       and attribute list containing attribute objects."""

    def __init__(self, tag_and_class_str: str, inner_html,
                 **kwargs):
        self.list_of_tags = ("body", "document", "div", "h1", "form",
                             "input", "small", "button", "label")
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

        if(len(args) == 0):
            return ''
        attr_str = " class="
        for counter, klass in enumerate(args):
            if counter == 0:
                attr_str += "\'" + klass
            else:
                attr_str += ' ' + klass
        attr_str += "\'"
        return attr_str

    def __str__(self):
        """This function produces the usable html."""
        html = "<" + self.tag \
               + self.attr_concatenater(*self.class_list) \
               + str(self.TagAttributeList) \
               + ">" + str(self.inner_html) + "</" + self.tag + ">"
        return html
        # return HTMLBeautifier.beautify(html, 2)
