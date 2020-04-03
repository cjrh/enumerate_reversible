original_enumerate = enumerate


def enumerate(iterable, start=0):
    class Inner:
        def __iter__(self):
            yield from original_enumerate(iterable, start=start)

        def __reversed__(self):
            end = len(iterable) - 1 + start
            yield from ((end - i, v) for i, v in original_enumerate(iterable))

    return Inner()


if __name__ == "__main__":
    for i, v in enumerate(range(3), start=5):
        print(i, v)

    for i, v in reversed(enumerate(range(3), start=5)):
        print(i, v)
