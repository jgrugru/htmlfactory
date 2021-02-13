# def tag_decorator_with_arguments(html_tag):
#     def tag_decorator(function):
#         def wrapper(innerHTML):
#             return "<" + html_tag + ">" + function(innerHTML) + "</" + html_tag + ">"
#         return wrapper
#     return tag_decorator
    
# @tag_decorator_with_arguments("div")
# def fill_html_tag(innerHTML):
#     return innerHTML

# print(fill_html_tag("test"))




def tag_function_factory(tag_list):
    tag_maker = {}
    for tag in tag_list:
        tag_maker[tag] = make_html_tag(tag)
    return tag_maker


def make_html_tag(tag):
    def make_tags(content, *args, **kwargs):
        return "<" + tag + attr_concatenater(*args, **kwargs) + ">" + content + "</" + tag + ">"
    
    return make_tags

def attr_concatenater(*args, **kwargs):
    """This function creates a string with all of the html attributes concatenated together."""
    if(len(args)==0 and len(kwargs)==0):
        return ''
    attr_str = ""
    for attr in kwargs:
        if attr == 'klass':
            attr_str += ' ' + 'class' + '=' + "\'" + kwargs[attr] + "\'"
        else:
            attr_str += ' ' + attr + '=' + "\'" + kwargs[attr] + "\'"
    return attr_str


# html_factory = tag_function_factory(list_of_tags)
# print(html_factory['div']("happy birthday", klass="container w-100", id="target-div"))


#html_factory("div.col-10.col-lg-9.d-inline-block") --> self.tag = div
#                                                       self.klass = ['col-10','col-lg-9',...]
#                                                       self.attr['id'] = target-div
#


class TagFactory():

    def __init__(self, tag_and_class_str: str, inner_html, **kwargs):
        self.list_of_tags = ("body", "document", "div", "h1")
        self.inner_html = inner_html
        self.attr_dict = kwargs
        self.cleanse_tag_and_class_str(tag_and_class_str)
        print(kwargs)

    def split_str_by_period(self, str):
        return str.split(".")

    def cleanse_tag_and_class_str(self, tag_and_class_str):
        tag_and_class_list = self.split_str_by_period(tag_and_class_str)
        if tag_and_class_list[0] in self.list_of_tags:
            self.tag = tag_and_class_list[0]
        else:
            self.tag = None
        self.class_list = tag_and_class_list[1:]


TagFactory("div.col-10.col-lg-9.d-inline-block", 'inside the tags', id="target-div")

def test_ouput():
    assert(str(TagFactory("div.col-10.col-lg-9.d-inline-block", '', id="target-div")) == "<div class='col-10 col-lg-9 d-inline-block' id='target-div'>inside the tags</div>")
