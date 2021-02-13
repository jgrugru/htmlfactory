from src.InnerHtml import InnerHtml

class TagFactory():
    """A tag object that has a tag, inner_html ojbect, and attribute dictionary."""

    def __init__(self, tag_and_class_str: str, inner_html,
                 children=(), **kwargs):
        self.list_of_tags = ("body", "document", "div", "h1", "form",
                             "input", "small", "button", "label")
        self.inner_html = InnerHtml(inner_html)
        self.attr_dict = kwargs
        self.cleanse_tag_and_class_str(tag_and_class_str)

    def split_str_by_period(self, str):
        return str.split(".")

    def cleanse_tag_and_class_str(self, tag_and_class_str):
        """This function parses the tag and class string
           (ex. 'div.col-md-10.col-10')."""

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

        if(len(args) == 0 and len(kwargs) == 0):
            return ''
        attr_str = " class="
        for counter, klass in enumerate(args):
            if counter == 0:
                attr_str += "\'" + klass
            else:
                attr_str += ' ' + klass
        attr_str += "\'"
        for attr in kwargs:
            attr_str += ' ' + attr + '=' + "\'" + kwargs[attr] + "\'"
        return attr_str

    def __str__(self):
        """This function produces the usable html."""
        # breakpoint()
        return "<" + self.tag \
               + self.attr_concatenater(*self.class_list, **self.attr_dict) \
               + ">" + str(self.inner_html) + "</" + self.tag + ">"
