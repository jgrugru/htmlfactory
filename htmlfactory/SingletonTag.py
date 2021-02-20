import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.dirname(__file__)))

from bs4 import BeautifulSoup
from TagAttributeList import TagAttributeList
from TagAndClassStr import TagAndClassStr

class SingletonTag(TagAndClassStr, TagAttributeList):
    """Class used for tags without a closing bracket.
    This would include tags such as <img> and <link>."""

    def __init__(self, tag_and_class_str, **kwargs):
        TagAndClassStr.__init__(self, tag_and_class_str)
        TagAttributeList.__init__(self, **kwargs)

    def __str__(self):
        html = "<" + self.tag \
               + self.get_classes_str() \
               + self.get_tag_attributes_str() \
               + ">"
        return html