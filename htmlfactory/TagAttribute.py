class TagAttribute():

    def __init__(self, attr, attr_value):
        self.attr = self.check_for_keywords_or_dashes(attr)
        self.attr_value = attr_value

    def check_for_keywords_or_dashes(self, attr):
        return_attr = attr
        if attr == 'four':
            return_attr = 'for'
        elif attr == 'acceptcharset':
            return_attr = 'accept-charset'
        elif attr == 'ariadescribedby':
            return_attr = 'aria-describedby'
        return return_attr

    def __str__(self):
        return " " + self.attr + '=' + "\'" + self.attr_value + "\'"
