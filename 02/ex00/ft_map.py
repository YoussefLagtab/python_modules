def name(obj):
    try:
        return type(obj).__name__
    except Exception:
        return ''


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """

    error_msg = ''
    for ele in iterable:
        try:
            yield function_to_apply(ele)
        except Exception:
            if not hasattr(type(iterable), '__iter__'):
                error_msg = f'E: `{name(iterable)}` is not iterable'
            elif name(function_to_apply) != 'function':
                error_msg = f'`{name(function_to_apply)}` obj is not callable'
            else:
                return None
        if error_msg != '':
            raise Exception(error_msg)
