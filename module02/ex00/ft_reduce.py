from collections.abc import Iterator

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function.
    """

    if not isinstance(iterable, (list, tuple, Iterator)):
        return None
    if len(iterable) == 1:
        return iterable[0]
    return function_to_apply(iterable[0], ft_reduce(function_to_apply, iterable[1:]))