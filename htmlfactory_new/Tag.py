from dataclasses import dataclass, field
from typing import List, Dict

from htmlfactory_new.protocols import HTMLElement


def attr_concatenater(attr: str, *args) -> str:
    """This function returns a string with all of the html
    attributes concatenated together.
    self.classes = ['col-md-10', 'col-10']
    becomes ' class='col-md-10 col-10'."""

    attr = f" {attr}="
    return_str = attr
    for counter, klass in enumerate(args):
        if counter == 0:
            return_str += "'" + klass
        else:
            return_str += " " + klass
    return_str += "'"

    return return_str


@dataclass
class Tag:
    """This function takes the tag_and_class_str
    (Ex: 'div.class1.class2') and turns it into printable tag."""

    raw_str: str
    attributes: Dict[str, HTMLElement]
    classes: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Populates the attributes self.tag and self.classes"""
        self.parse_raw_str(self.raw_str)

    @property
    def prefix(self) -> str:
        return "<" + self.tag + self.get_classes_str() + self.get_attributes_str() + ">"

    @property
    def open_prefix(self) -> str:
        return "<" + self.tag + self.get_classes_str() + self.get_attributes_str()

    @property
    def suffix(self) -> str:
        return "</" + self.tag + ">"

    def parse_raw_str(self, raw_str: str) -> None:
        """This function parses the tag and class string
        (example input: 'div.col-md-10.col-10').
        Self.tag = 'div' and
        self.class_list = ['col-md-10', 'col-10']."""

        split_str: List[str] = self.split_str_by_period(raw_str)

        self.tag = split_str[0]
        if len(split_str) > 0:
            self.classes = split_str[1:]

    def split_str_by_period(self, str) -> List[str]:
        """Return the string split by periods.
        "div.col-md-10" becomes ["div", "col-md-10"]."""

        return str.split(".")

    def get_classes_str(self) -> str:
        if len(self.classes) > 0:
            return attr_concatenater("class", *self.classes)
        else:
            return ""

    def get_attributes_str(self) -> str:
        return_str = ""
        for k, v in self.attributes.items():
            return_str += " " + str(k) + "='" + str(v) + "'"
        return return_str

    def __str__(self) -> str:
        return f"Tag({self.prefix})"
