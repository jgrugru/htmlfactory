from pydantic import BaseModel, Field, validate_arguments
from bs4 import BeautifulSoup
from typing import Dict, Union, List, Tuple
from htmlfactory_new.HTMLTag import HTMLTag
from htmlfactory_new.protocols import Stringable


class HTMLElement(BaseModel):
    """
    The core class to creating an HTML element. "<div class="test">Inside the div</div>" is considered an HTML element.
    HTMLElement contains a HTMLTag property which is responsible for the actual tags -- the html between <> brackets. EX) <div>.
    Ex) HTMLElement(raw_tag="div.container", innerHTML=HTMLElement("div.my-class", innerHTML="I'm inside the div"))
    -->
    <div class='container'><div class='my-class'>I'm inside the div</div></div>
    """

    raw_tag: str
    innerHTML: List[Stringable] = Field(default_factory=list)
    singleton: bool = False
    attributes: Dict[str, Stringable] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    @property
    def tag(self) -> HTMLTag:
        new_tag = HTMLTag(raw_str=self.raw_tag, attributes=self.attributes)
        return new_tag

    def get_html(self, bootstrap: bool = False, jquery: bool = False) -> str:
        """Grabs all the html for selected HTMLElement object,
        concatenates all children objects."""
        if not self.singleton:
            return self.full_tag()
        else:
            return self.singleton_tag()

    def full_tag(self) -> str:
        """The str output if singleton == False"""
        tag = self.tag
        html_str = tag.prefix
        html_str += self.concatenate_innerHTML()
        html_str += tag.suffix

        return html_str

    def singleton_tag(self) -> str:
        """The str output if singleton == True"""
        tag = self.tag
        html_str = tag.singleton
        html_str += self.concatenate_innerHTML()

        return html_str

    def concatenate_innerHTML(self) -> str:
        """Recursively grabs all children objects html
        and concatenates them"""
        html_str = ""
        for element in self.innerHTML:
            html_str += str(element)
        return html_str

    def print_html(self, pretty: bool = False) -> None:
        if pretty:
            print(self.get_pretty_str())
        else:
            print(self.get_html())

    def get_pretty_str(self) -> str:
        soup = BeautifulSoup(self.get_html(), features="html.parser")
        return soup.prettify()

    def add_child(self, child: Stringable) -> None:
        self.innerHTML.append(child)

    def __str__(self) -> str:
        return self.get_html()


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def convert_to_list(
    innerHTML: Union[List[Stringable], Tuple[Stringable], Stringable]
) -> List[Stringable]:
    """Utility function to convert any of the allowed types to a list"""
    if isinstance(innerHTML, tuple):
        return list(innerHTML)
    elif isinstance(innerHTML, List):
        return innerHTML
    else:
        return [innerHTML]


# TO DO: Maybe call it tag instead of raw_tag?
@validate_arguments(config=dict(arbitrary_types_allowed=True))
def Tag(
    raw_tag: str,
    innerHTML: Union[List[Stringable], Tuple[Stringable], Stringable] = [],
    singleton: bool = False,
    **kwargs
) -> HTMLElement:
    return HTMLElement(
        raw_tag=raw_tag,
        innerHTML=convert_to_list(innerHTML),
        singleton=singleton,
        attributes=kwargs,
    )
