class InnerHtml():
    """This class allows the innerHTML attribute of a TagFactory object
       to either be a str, single TagFactory object, or a list/tuple of
       TagFactory objects"""

    def __init__(self, inner_html):
        self.inner_html = inner_html

    def is_list_or_tuple(self, an_object):
        if type(an_object) == tuple or type(an_object) == list:
            return True
        else:
            return False

    def concatenate_children(self, iterable_object):
        inside_tags_str = ""
        for tag_object in iterable_object:
            inside_tags_str += str(tag_object) + '\n'
        return inside_tags_str

    def __str__(self):
        if self.is_list_or_tuple(self.inner_html):
            return self.concatenate_children(self.inner_html)
        else:
            return str(self.inner_html)
