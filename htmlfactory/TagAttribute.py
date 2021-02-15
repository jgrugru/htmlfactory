class TagAttribute():
    
    def __init__(self, attr, attr_value):
        self.attr = attr
        self.attr_value = attr_value

    def __str__(self):
        if self.attr == 'four':
            self.attr = 'for'
        elif self.attr == 'acceptcharset':
            self.attr = 'accept-charset'
        elif self.attr == 'ariadescribedby':
            self.attr = 'aria-describedby'
        return " " + self.attr + '=' + "\'" + self.attr_value + "\'"
