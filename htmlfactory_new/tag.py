from typing import List, Protocol, Generator, Callable, Dict, Any
from pydantic import BaseModel


class Tag(str):
    """
    A str that is surrounded by < and >. Example) <img> is a tag.
    Creating a class so this can easily be incorporated with Pydantic.
    """

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[str], str], None, None]:
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        # __modify_schema__ should mutate the dict it receives in place,
        # the returned value will be ignored
        field_schema.update(pattern="< ..str.. >", type="float")

    @classmethod
    def validate(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError("str required")
        if v[0] != "<" and v[-1] != ">":
            raise TypeError(
                "Not a valid tag. The first element needs to be '<' and the last element needs to be '>'."
            )
        return v

    def __repr__(self) -> str:
        return f"Tag({super().__repr__()})"


class Div(BaseModel):
    prefix: Tag
    suffix: Tag
    contents: str

    def get_html(self) -> str:
        return self.prefix + self.contents + self.suffix

    def print_html(self) -> None:
        print(self.get_html())


my_div = Div(prefix=Tag("<div>"), suffix=Tag("</div>"), contents="Testing this out.")
my_div.print_html()


class HTML_Element(Protocol):
    def get_html(self) -> str:
        ...

    def print_html(self) -> None:
        ...


class TagFactory(BaseModel):
    inner_html: List[HTML_Element]

    def get_html(self) -> str:
        str = ""
        for element in self.inner_html:
            str += element.get_html()
        return str

    def print_html(self) -> None:
        print(self.get_html())
