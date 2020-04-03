original_enumerate = enumerate


def enumerate(iterable, start=0):
    class Inner:
        def __iter__(self):
            yield from original_enumerate(iterable, start=start)

        def __reversed__(self):
            rev = reversed(iterable)  # First, for accurate exception msg
            rng = range(len(iterable) - 1 + start, -1 + start, -1)
            yield from zip(rng, rev)

    return Inner()


if __name__ == "__main__":
    for i, v in enumerate(range(3), start=5):
        print(i, v)

    for i, v in reversed(enumerate(range(3), start=5)):
        print(i, v)

    for i, v in reversed(enumerate(iter([1, 2, 3]), start=5)):
        print(i, v)
