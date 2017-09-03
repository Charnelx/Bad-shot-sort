from random import randint


def bad_shot_sort(lst: list, reverse=False):
    """
    This function implements one of worsts sorting algorithms ever.
    Also, it support brand new feature - REVERSE SORT!

    How it works:
        - randomly (146% randomness guarantied!) chose two indexes
        and swap elements between them
        - check each element pairs to meet conditions; result of
        this check append to list
        - check if all values in checklist are True
        - negative result? Don't worry, someday you'll be lucky enough.
        Some day...no jokes.

    This algorithm could be improved:
     - randomly select more then one index at ones and swap values
       behind this indexes with other indexes values randomly.
     - randomly swap indexes N times and check the result on each
       iteration

    Uncomment code to force fast memory consumption.

    Example:

    >>> import time
    ...
    >>> s_time = time.time()
    >>> s = sorted([randint(0, 99) for i in range(1000000)])
    >>> print('Build-in sort done in: {:.6} sec.'.format(time.time() - s_time))

    Build-in sort done in: 2.32962 sec.

    >>> s_time = time.time()
    >>> s = bad_shot_sort([randint(0, 99) for i in range(10)])
    >>> print('Bad-shot sort suffers for: {:.6} sec.'.format(time.time() - s_time))

    Bad-shot sort suffers for: 49.9636 sec.


    :param lst: list
    :param reverse: bool
    :return: list
    """
    length = len(lst)

    # steps = []
    # from_indexes = []
    # to_indexes = []

    run = True
    while run:
        from_cell = randint(0, length-1)
        to_cell = randint(0, length-1)
        in_buffer = lst[from_cell]
        out_buffer = lst[to_cell]
        lst[to_cell] = in_buffer
        lst[from_cell] = out_buffer

        # steps.append(lst)
        # from_indexes.append(from_cell)
        # to_indexes.append(to_cell)

        mask = []
        for i in range(1, length):
            if reverse:
                if lst[i - 1] >= lst[i]:
                    mask.append(True)
                    continue
                else:
                    mask.append(False)
                    break
            else:
                if lst[i - 1] <= lst[i]:
                    mask.append(True)
                    continue
                else:
                    mask.append(False)
                    break
        if all(mask):
            run = False
    return lst