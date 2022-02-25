from dataclasses import dataclass
from attr import attributes
from pydantic import BaseModel, ConstrainedStr


def add_brackets(raw_str: str, isSuffix: bool = False) -> str:
    if not isSuffix:
        return "<" + raw_str + ">"
    else:
        return "</" + raw_str + ">"


class RootTag(BaseModel):
    raw_tag: ConstrainedStr

    @property
    def prefix(self):
        return Tag(self.raw_tag)

    @property
    def suffix(self):
        return Tag(self.raw_tag, isSuffix=True)

@dataclass
class Tag:
    raw_tag: str
    isSuffix: bool = False
    classes: str = None

    def __str__(self) -> str:
        return add_brackets(self.raw_tag, isSuffix=self.isSuffix)

@dataclass
class TagAttribute:
    attribute: str
    value: str

    def __str__(self) -> str:
        return self.attribute + "=" + self.value


class Parser(BaseModel):
    raw_str: str

    def _get_raw_str(self) -> str:
        return self.raw_str

    def _strip_whitespace(self) -> str:
        return self.raw_str.strip()

    def _get_tag_type(self) -> str:
        return self.raw_str.split(".")[0]

    def get_root_tag(self) -> RootTag:
        return RootTag(raw_tag = self._get_tag_type())


###############################################################################
x = Parser(raw_str="div.class1.class2.class3")

y = x.get_root_tag()
print(y.prefix, y.suffix)










# class Tag(str):
#     """
#     A str that is surrounded by < and >. Example) <img> is a tag.
#     Creating a class so this can easily be incorporated with Pydantic.
#     """

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
#         field_schema.update(pattern="< ..str.. >", type="str")

#     @classmethod
#     def validate(cls, v: str) -> str:
#         if not isinstance(v, str):
#             raise TypeError("str required")
#         return v.strip()

#     @property
#     def starting_tag(self):
#         return f"<{self}>"

#     @property
#     def ending_tag(self):
#         return f"</{self}>"

#     def __repr__(self) -> str:
#         return f"Tag({super().__repr__()})"


# class Div(BaseModel):
#     tag: Tag
#     contents: str

#     def get_html(self) -> str:
#         return self.prefix + self.contents + self.suffix

#     def print_html(self) -> None:
#         print(self.get_html())


# my_div = Div(prefix=Tag("<div>"), suffix=Tag("</div>"), contents="Testing this out.")
# my_div.print_html()


# class HTML_Element(Protocol):
#     def get_html(self) -> str:
#         ...

#     def print_html(self) -> None:
#         ...


# class TagFactory(BaseModel):
#     inner_html: List[HTML_Element]

#     def get_html(self) -> str:
#         str = ""
#         for element in self.inner_html:
#             str += element.get_html()
#         return str

#     def print_html(self) -> None:
#         print(self.get_html())
