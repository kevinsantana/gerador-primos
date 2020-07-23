from math import sqrt
from itertools import count, islice


def eh_primo(x: int) -> bool:
    return x > 1 and all(x % i for i in islice(count(2), int(sqrt(x)-1)))
