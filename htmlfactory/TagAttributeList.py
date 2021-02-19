from TagAttribute import TagAttribute


class TagAttributeList:

    def __init__(self, **kwargs):
        self.attr_list = []
        if kwargs:
            for attr in kwargs:
                self.attr_list.append(TagAttribute(attr, kwargs[attr]))

    def get_tag_attributes_str(self):
        return_str = ""
        for tag_attribute in self.attr_list:
            return_str += str(tag_attribute)
        return return_str
