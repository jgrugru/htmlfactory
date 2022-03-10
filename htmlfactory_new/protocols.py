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
