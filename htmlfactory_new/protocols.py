from typing import Protocol, runtime_checkable


@runtime_checkable
class HTMLElement(Protocol):
    """An HTML element can be any python object that can be casted as a string.
    If the developer would like to create their own output, the get_html function is required."""

    # def get_html(self) -> str:
    #     """This will override __str__ dunder method if you would like to have your own return value for HTML."""
    #     ...

    def __str__(self) -> str:
        ...


# class InnerHTML(list):

#     @classmethod
#     def __get_validators__(cls) -> Generator[Callable[[str], List[HtmlElement]], None, None]:
#         # one or more validators may be yielded which will be called in the
#         # order to validate the input, each validator will receive as an input
#         # the value returned from the previous validator
#         yield cls.validate

#     @classmethod
#     def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
#         # __modify_schema__ should mutate the dict it receives in place,
#         # the returned value will be ignored
#         field_schema.update(pattern="List[HtmlElement]", type="List[HtmlElement]")

#     @classmethod
#     def validate(cls, v: Union[List[HtmlElement], HtmlElement]) -> List[HtmlElement]:
#         if not isinstance(v, List) and isinstance(v, HtmlElement):
#             return [v]
#         else:
#             return v

#     def __repr__(self) -> str:
#         return f"Tag({super().__repr__()})"
