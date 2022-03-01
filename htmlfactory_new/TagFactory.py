from typing import List, Protocol, runtime_checkable

# from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from htmlfactory_new.Tag import Tag

"""# class Tag(str):
#     A str that is surrounded by < and >. Example) <img> is a tag.
#     Creating a class so this can easily be incorporated with Pydantic.

#     @classmethod
#     def __get_validators__(cls) -> Generator[Callable[[str], str], None, None]:
#         # one or more validators may be yielded which will be called in the
#         # order to validate the input, each validator will receive as an input
#         # the value returned from the previous validator
#         yield cls.validate

#     @classmethod
#     def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
#         # __modify_schema__ should mutate the dict it receives in place,
#         # the returned value will be ignored
#         field_schema.update(pattern="< ..str.. >", type="float")

#     @classmethod
#     def validate(cls, v: str) -> str:
#         if not isinstance(v, str):
#             raise TypeError("str required")
#         if v[0] != "<" and v[-1] != ">":
#             raise TypeError(
#                 "Not a valid tag. The first element needs to be '<' and the last element needs to be '>'."
#             )
#         return v

#     def __repr__(self) -> str:
#         return f"Tag({super().__repr__()})"


# class Div(BaseModel):
#     prefix: Tag
#     suffix: Tag
#     contents: str

#     def get_html(self) -> str:
#         return self.prefix + self.contents + self.suffix

#     def print_html(self) -> None:
#         print(self.get_html())

# my_div = Div(prefix=Tag("<div>"), suffix=Tag("</div>"), contents="Testing this out.")
# my_div.print_html()


# class HtmlElement(Protocol):

#     def __str__(self) -> str:
#         ...

    # def has_child(self) -> None:
    #     ...

    # def add_child(self) -> None:
    #     ...

    # def get_html(self) -> str:
    #     ...

    # def print_html(self) -> None:
    #     ...


    # @classmethod
    # def __get_validators__(cls) -> Generator[Callable[[str], str], None, None]:
    #     yield cls.validate

    # @classmethod
    # def validate(cls, v: T) -> T:
    #     if issubclass(v, cls):
    #         return v
    #     else:
    #         raise TypeError(
    #             "Class does not contain str dunder method."
    #         )
"""

# T = TypeVar("T")


@runtime_checkable
class HtmlElement(Protocol):
    """An HTML element can be any python object that can be casted as a string.
    If the developer would like to create their own output, the get_html function is required."""

    # def get_html(self) -> str:
    #     """This will override __str__ dunder method if you would like to have your own return value for HTML."""
    #     ...

    def __str__(self) -> str:
        ...


@dataclass
class TagFactory:
    """
    Creates printable html.
    Ex) TagFactory("div.class1", innerHTML=[TagFactory_obj1, "I'm inside the div", TagFactory_obj2])
    """

    raw_tag: str
    innerHTML: List[HtmlElement] = field(default_factory=list)

    def get_tag(self) -> Tag:
        return Tag(self.raw_tag)

    def has_contents(self) -> bool:
        return bool(self.innerHTML is not None)

    def get_html(self, bootstrap: bool = False, jquery: bool = False) -> str:
        tag = self.get_tag()
        html_str = tag.get_prefix()

        html_str += self.concatenate_innerHTML()

        html_str += tag.get_suffix()
        return html_str

    def concatenate_innerHTML(self) -> str:
        # import pdb; pdb.set_trace()
        if not self.innerHTML:
            return ""

        html_str = ""
        for element in self.innerHTML:
            html_str += str(element)
        return html_str

    def print_html(self, pretty: bool = False) -> None:
        print(self.get_html())

    def add_child(self, child: HtmlElement) -> None:
        self.innerHTML.append(child)

    def __str__(self) -> str:
        return self.get_html()


my_div = TagFactory(
    raw_tag="div.class1.class2.class3",
    innerHTML=[
        "Testing this out.",
        "tests",
        TagFactory("div.second-class", innerHTML=["I am in the second div."]),
    ],
)
print(my_div.get_html())
# tag = Tag("div.class1.class2")
# print(tag)
