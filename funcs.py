from collections.abc import Iterable
import doctest


def ilen(iterable: Iterable) -> int:
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return len(list(iterable))


def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for it in iterable:
        if isinstance(it, str) or not isinstance(it, Iterable):
            yield it
        else:
            f = flatten(it)
            while True:
                try:
                    yield next(f)
                except StopIteration:
                    break


def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    s = set()
    for it in iterable:
        if it not in s:
            s.add(it)
            yield it


def groupby(key, iterable: Iterable) -> dict:
    """
    >>> users = [
    ...    {'gender': 'female', 'age': 33},
    ...    {'gender': 'male', 'age': 20},
    ...    {'gender': 'female', 'age': 21},
    ... ]
    >>> groupby('gender', users) # doctest: +NORMALIZE_WHITESPACE
    {'female': [{'gender': 'female', 'age': 33}, {'gender': 'female', 'age': 21}],
     'male': [{'gender': 'male', 'age': 20}]}
    """
    result = {}
    for it in iterable:
        group = it[key]
        if group not in result:
            result.update({group: []})
        result[group].append(it)
    return result


def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4)]
    """
    chunk = []
    for it in iterable:
        chunk.append(it)
        if len(chunk) == size:
            yield tuple(chunk, )
            chunk = []
    if chunk:
        yield tuple(chunk)


def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> print(first(range(0)))
    None
    """
    try:
        it = iter(iterable)
        return next(it)
    except StopIteration:
        return None


def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> print(last(range(0)))
    None
    """
    it = list(iterable)
    if len(it) > 0:
        return it[-1]
    return None


if __name__ == "__main__":
    doctest.testmod()
