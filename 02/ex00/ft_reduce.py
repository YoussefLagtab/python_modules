def name(obj):
    try:
        return type(obj).__name__
    except Exception:
        return ''


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    error_msg = ''
    acc = None
    for cur in iterable:
        try:
            if not acc:
                acc = cur
            else:
                acc = function_to_apply(acc, cur)
        except Exception:
            if not hasattr(type(iterable), '__iter__'):
                error_msg = f'E: `{name(iterable)}` is not iterable'
            elif name(function_to_apply) != 'function':
                error_msg = f'`{name(function_to_apply)}` obj is not callable'
            else:
                return None
        if error_msg != '':
            raise Exception(error_msg)

    return acc
