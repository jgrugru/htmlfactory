from typing import Iterable
from dataclasses import dataclass, field
from htmlfactory_new.Tag import Tag
from htmlfactory_new.InnerHtml import HTMLElement


@dataclass
class TagFactory:
    """
    Creates printable html.
    Ex) TagFactory("div.class1", innerHTML=[TagFactory_obj1, "I'm inside the div", TagFactory_obj2])
    """

    raw_tag: str
    innerHTML: Iterable[HTMLElement] = field(default_factory=list)
    singleton: bool = False

    def get_tag(self) -> Tag:
        return Tag(self.raw_tag)

    def get_html(self, bootstrap: bool = False, jquery: bool = False) -> str:
        if not self.singleton:
            return self.full_tag()
        else:
            return self.singleton_tag()

    def full_tag(self) -> str:
        tag = self.get_tag()
        html_str = tag.prefix
        html_str += self.concatenate_innerHTML()
        html_str += tag.suffix

        return html_str

    def singleton_tag(self) -> str:
        tag = self.get_tag()
        html_str = tag.open_prefix
        html_str += ">"
        html_str += self.concatenate_innerHTML()

        return html_str

    def concatenate_innerHTML(self) -> str:
        html_str = ""
        for element in self.innerHTML:
            html_str += str(element)
        return html_str

    def print_html(self, pretty: bool = False) -> None:
        print(self.get_html())

    # TODO: How to add child when innerHTML is generic Iterable?
    # def add_child(self, child: HTMLElement) -> None:
    #     self.innerHTML.extend(child)

    def __str__(self) -> str:
        return self.get_html()
