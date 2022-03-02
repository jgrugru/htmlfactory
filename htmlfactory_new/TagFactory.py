from typing import Iterable, Dict, Union
from dataclasses import dataclass, field
from htmlfactory_new.Tag import Tag
from htmlfactory_new.protocols import HTMLElement
from itertools import chain


@dataclass
class TagFactory:
    """
    Python class that assists in creating printable html.
    Ex) TagFactory("div.container-fluid", innerHTML=[TagFactory("div.my-class", innerHTML=["I'm inside the div"])])
    -->
    <div class='container-fluid'><div class='my-class'>I'm inside the div</div></div>
    """

    raw_tag: str
    innerHTML: Iterable[HTMLElement] = field(default_factory=list)
    singleton: bool = False
    attributes: Dict[str, HTMLElement] = field(default_factory=dict)

    @property
    def tag(self) -> Tag:
        return Tag(self.raw_tag, attributes=self.attributes)

    def get_html(self, bootstrap: bool = False, jquery: bool = False) -> str:
        if not self.singleton:
            return self.full_tag()
        else:
            return self.singleton_tag()

    def full_tag(self) -> str:
        tag = self.tag
        html_str = tag.prefix
        html_str += self.concatenate_innerHTML()
        html_str += tag.suffix

        return html_str

    def singleton_tag(self) -> str:
        tag = self.tag
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
    def add_child(self, child: Union[Iterable[HTMLElement], HTMLElement]) -> None:
        if isinstance(child, Iterable):
            self.innerHTML = chain(self.innerHTML, child)
        else:
            self.innerHTML = chain(self.innerHTML, [child])

    def __str__(self) -> str:
        return self.get_html()


# x = TagFactory("div.container-fluid", innerHTML=[TagFactory("div.my-class", innerHTML=["I'm inside the div"])])
# print(x)
# x.add_child("DERKADFKADSFK AFDKDA F")
# print(x)
