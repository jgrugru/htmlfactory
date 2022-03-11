from typing import Protocol, runtime_checkable


@runtime_checkable
class Stringable(Protocol):
    """An HTML element can be any python object that can be casted as a string.
    If the developer would like to create their own output, the get_html function is required."""

    def __str__(self) -> str:
        ...
