from collections.abc import Iterator

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            An iterable.
            None if the iterable can not be used by the function.
    """

# ... Your code here ...    
    if not isinstance(iterable, (list, tuple, Iterator)):
        return None
    return [function_to_apply(i) for i in iterable]

    def __str__(self):
        return print(self)
