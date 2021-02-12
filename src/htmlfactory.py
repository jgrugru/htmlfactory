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


list_of_tags = ("body", "document", "div", "h1")


def tag_function_factory(tag_list):
    tag_maker = {}
    for tag in tag_list:
        tag_maker[tag] = make_html_tag(tag)
    return tag_maker


def make_html_tag(tag):
    def make_tags(content, *args):
        # print("inside make tags", args)
        return "<" + tag + attr_concatenater(*args) + ">" + content + "</" + tag + ">"
    
    return make_tags

def attr_concatenater(*args):
    """This function creates a string with all of the html attributes concatenated together."""
    if(not bool(len(args))):
        return ''
    class_str = " class="
    for counter, class_element in enumerate(args):
        if(counter != 0):
            class_str += " " + class_element
        else:
            class_str += class_element
    return class_str


html_factory = tag_function_factory(list_of_tags)
# html_factory['div']("happy birthday", klass="container w-100", id="target-div")


# print(html_factory['div'](''))
# html_factory("div", klass="container w-100", id="target-div")

# create an outer div with bootstrap class elements
# 