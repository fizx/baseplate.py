"""Internal library helpers."""
import functools
import warnings

from typing import Callable
from typing import Generic
from typing import Type
from typing import TypeVar


def warn_deprecated(message: str) -> None:
    """Emit a deprecation warning from the caller.

    The stacktrace for the warning will point to the place where the function
    calling this was called, rather than in baseplate. This allows the user to
    most easily see where in _their_ code the deprecation is coming from.

    """
    warnings.warn(message, DeprecationWarning, stacklevel=3)


T = TypeVar("T")
R = TypeVar("R")


# cached_property is a renamed copy of pyramid.decorator.reify
# see COPYRIGHT for full license information
class cached_property(Generic[T, R]):
    """Like @property but the function will only be called once per instance.

    When used as a method decorator, this will act like @property but instead
    of calling the function each time the attribute is accessed, instead it
    will only call it on first access and then replace itself on the instance
    with the return value of the first call.

    """

    def __init__(self, wrapped: Callable[[T], R]):
        self.wrapped = wrapped
        functools.update_wrapper(self, wrapped)  # type: ignore

    def __get__(self, instance: T, owner: Type[T]) -> R:
        if instance is None:
            return self
        ret = self.wrapped(instance)
        setattr(instance, self.wrapped.__name__, ret)
        return ret
