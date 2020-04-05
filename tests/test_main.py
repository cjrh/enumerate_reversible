import sys
import pytest
from enumerate_reversible import enumerate as new_enumerate


sequences = [
    # Lists
    [],
    [1],
    [1, 2, 3],
    ['a'],
    ['a', 'b', 'c'],
    # Tuples
    tuple(),
    (1, ),
    (1, 2, 3),
    # Ranges
    range(0),
    range(3),
    range(1000),
    # Strings
    '',
    'a',
    'abc',
    # Bytes
    b'',
    b'a',
    b'abc',
    # Bytearray
    bytearray(b''),
    bytearray(b'a'),
    bytearray(b'abc'),
    # Memoryview
    memoryview(b''),
    memoryview(b'a'),
    memoryview(b'abc'),
]


if sys.version_info >= (3, 8):
    sequences.extend([
        # Views
        dict().keys(),
        dict().values(),
        dict().items(),
        dict(a=1, b=2, c=2).keys(),
        dict(a=1, b=2, c=2).values(),
        dict(a=1, b=2, c=2).items(),
    ])


forward_values = [
    (
        s, start, list(enumerate(s, start=start))
    ) for s in sequences for start in range(5)
]


reverse_values = [
    (
        s, start, list(reversed(list(enumerate(s, start=start))))
    ) for s in sequences for start in range(5)
]


@pytest.mark.parametrize('seq,start,result', [
    *forward_values,
])
def test_enumerate_forward(seq, start, result):
    outputs = []
    for i, v in new_enumerate(seq, start=start):
        outputs.append((i, v))

    assert outputs == result


@pytest.mark.parametrize('seq,start,result', [
    *reverse_values,
])
def test_enumerate_reverse(seq, start, result):
    outputs = []
    for i, v in reversed(new_enumerate(seq, start=start)):
        outputs.append((i, v))

    assert outputs == result
