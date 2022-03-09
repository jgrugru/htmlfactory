from typing import Dict, Union, List, Tuple, Any

# from dataclasses import dataclass, field

from pydantic import BaseModel, Field

# from pydantic import BaseModel, validator, Field
from htmlfactory_new.Tag import Tag
from htmlfactory_new.protocols import HTMLElement

# from itertools import chain


class TagFactory(BaseModel):
    """
    Python class that assists in creating printable html.
    Ex) TagFactory("div.container-fluid", innerHTML=[TagFactory("div.my-class", innerHTML=["I'm inside the div"])])
    -->
    <div class='container-fluid'><div class='my-class'>I'm inside the div</div></div>
    """

    raw_tag: str
    innerHTML: List[Any] = Field(default_factory=list)
    singleton: bool = False
    attributes: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    @property
    def tag(self) -> Tag:
        new_tag = Tag(raw_str=self.raw_tag, attributes=self.attributes)
        new_tag.parse_raw_str()
        return new_tag

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

    def add_child(self, child: HTMLElement) -> None:
        self.innerHTML.append(child)

    def __str__(self) -> str:
        return self.get_html()

    # def __enter__(self):
    #     return self

    # def __exit__(self, type, value, traceback):
    #     pass


# with TagFactory("div.container-fluid", innerHTML=[TagFactory("div.my-class", innerHTML=["I'm inside the div"])]) as obj:
#     obj.add_child("Asfadfdffads")
#     print(obj)


def convert_to_list(innerHTML) -> List[HTMLElement]:
    if isinstance(innerHTML, tuple):
        return list(innerHTML)
    elif isinstance(innerHTML, List):
        return innerHTML
    else:
        return [innerHTML]


def Tagged(
    raw_tag: str,
    innerHTML: Union[List[HTMLElement], Tuple[HTMLElement], HTMLElement] = [],
    singleton: bool = False,
    **kwargs
) -> TagFactory:
    return TagFactory(
        raw_tag=raw_tag,
        innerHTML=convert_to_list(innerHTML),
        singleton=singleton,
        attributes=kwargs,
    )
