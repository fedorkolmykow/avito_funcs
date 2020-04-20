import pytest
import funcs
import MyIteration


@pytest.mark.parametrize('s,exp', [
    (MyIteration.SimpleIterator(3), 3),
    (MyIteration.SomeIterable([]), 0)
])
def test_ilen(s, exp):
    length = funcs.ilen(s)
    assert exp == length


@pytest.mark.parametrize('s', [
    MyIteration.NotIterable([]),
])
def test_ilen_error(s):
    with pytest.raises(TypeError):
        funcs.ilen(s)


@pytest.mark.parametrize('s,exp', [
    (['12', '34'], ['12', '34']),
    ('12', ['1', '2', ]),
    ([1, [2, ], (3, ), {4: 5, }, ], [1, 2, 3, 4, ]),
    (MyIteration.SimpleIterator(2), [1, 1, ]),
    (MyIteration.SomeIterable([]), []),
])
def test_flatten(s, exp):
    flat = list(funcs.flatten(s))
    assert exp == flat


@pytest.mark.parametrize('s,exp', [
    (['12', '12', ], ['12', ]),
    (MyIteration.SimpleIterator(2), [1, ]),
    (MyIteration.SomeIterable([]), []),
])
def test_distinct(s, exp):
    dist = list(funcs.distinct(s))
    assert exp == dist


@pytest.mark.parametrize('s,exp', [
    ([
        {'color': 'red', 'clothing': 'jeans'},
        {'color': 'blue', 'clothing': 'jeans'},
        {'color': 'red', 'clothing': 'shirt'},
     ],
     {
        'red': [{'color': 'red', 'clothing': 'jeans'}, {'color': 'red', 'clothing': 'shirt'},],
        'blue': [{'color': 'blue', 'clothing': 'jeans'}, ]
     }),
])
def test_groupby(s, exp):
    grouped = funcs.groupby('color', s)
    assert exp == grouped


@pytest.mark.parametrize('length, s, exp', [
    (5, [1, 2, 3, ], [(1, 2, 3), ]),
    (2, [1, 2, 3, ], [(1, 2), (3, )]),
    (0, [1, 2, 3, ], [(1, 2, 3), ]),
    (1, [1, 2, 3, ], [(1,), (2,), (3,), ]),
])
def test_chunks(length, s, exp):
    list_of_chunks = list(funcs.chunks(length, s))
    assert exp == list_of_chunks


@pytest.mark.parametrize('s, exp', [
    (MyIteration.SimpleIterator(2), 1),
    (MyIteration.SomeIterable([1, 2]), 1),
    ([], None)
])
def test_first(s, exp):
    f_el = funcs.first(s)
    assert exp == f_el


@pytest.mark.parametrize('s, exp', [
    (MyIteration.SimpleIterator(2), 1),
    (MyIteration.SomeIterable([1, 2]), 2),
    ([], None)
])
def test_last(s, exp):
    l_el = funcs.last(s)
    assert exp == l_el

