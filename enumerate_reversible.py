original_enumerate = enumerate


def enumerate(iterable, start=0):
    class Inner:
        def __iter__(self):
            yield from original_enumerate(iterable, start=start or 0)

        def __reversed__(self):
            stt = start or 0
            rev = reversed(iterable)  # First, for accurate exception msg
            rng = range(len(iterable) - 1 + stt, -1 + stt, -1)
            yield from zip(rng, rev)

    return Inner()
