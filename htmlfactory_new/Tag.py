from typing import List, Dict
from pydantic import BaseModel, Field, PrivateAttr

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


class Tag(BaseModel):
    """This class represents the <tag> and closing </tag>.
    Is responsible for all attributes regarding a tag."""

    raw_str: str
    attributes: Dict[str, HTMLElement]
    classes: List[str] = Field(default_factory=list)
    _tag: str = PrivateAttr(default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parse_raw_str()

    class Config:
        arbitrary_types_allowed = True

    @property
    def prefix(self) -> str:
        return (
            "<" + self._tag + self.get_classes_str() + self.get_attributes_str() + ">"
        )

    @property
    def open_prefix(self) -> str:
        return "<" + self._tag + self.get_classes_str() + self.get_attributes_str()

    @property
    def suffix(self) -> str:
        return "</" + self._tag + ">"

    def parse_raw_str(self) -> None:
        """This function parses the tag and class string
        (example input: 'div.col-md-10.col-10').
        Self.tag = 'div' and
        self.class_list = ['col-md-10', 'col-10']."""

        split_str: List[str] = self.split_str_by_period(self.raw_str)

        self._tag = split_str[0]
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
        return f"_Tag({self.prefix})"
