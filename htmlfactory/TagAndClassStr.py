class TagAndClassStr():
    """This function takes the tag_and_class_str
    (Ex: 'div.class1.class2') and turns it into printable
    class and tag. The TagFactory class inherits this class."""

    def __init__(self, tag_and_class_str):
        self.cleanse_tag_and_class_str(tag_and_class_str)

    def get_tag(self):
        return self.tag

    def get_classes_str(self):
        return self.class_concatenater(*self.class_list)

    def split_str_by_period(self, str):
        """Return the string split by periods.
        "div.col-md-10" becomes ["div", "col-md-10"]."""

        return str.split(".")

    def cleanse_tag_and_class_str(self, tag_and_class_str):
        """This function parses the tag and class string
           (example input: 'div.col-md-10.col-10').
           Self.tag = 'div' and
           self.class_list = ['col-md-10', 'col-10']."""

        tag_and_class_list = self.split_str_by_period(tag_and_class_str)

        self.tag = tag_and_class_list[0]

        if len(tag_and_class_list) > 0:
            self.class_list = tag_and_class_list[1:]
        else:
            self.class_list = ''

    def class_concatenater(self, *args):
        """This function returns a string with all of the html
           classes concatenated together.
           self.class_list = ['col-md-10', 'col-10']
           becomes ' class='col-md-10 col-10'."""

        if(not args):
            return ''

        return_class_str = " class="
        for counter, klass in enumerate(args):
            if counter == 0:
                return_class_str += "\'" + klass
            else:
                return_class_str += ' ' + klass
        return_class_str += "\'"

        return return_class_str
