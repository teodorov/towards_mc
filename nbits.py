from model import TransitionRelation
from traversal import predicate_finder


class NBits(TransitionRelation):

    def __init__(self, roots: list, n: int):
        self.initial = roots
        self.nBits = n

    def roots(self):
        return self.initial

    def next(self, source):
        neighbours = []
        for i in range(self.nBits):
            neighbours.append(source ^ (1 << i))
        return neighbours


def binary_print(s):
    return set(map(
        lambda x: "{0:03b}".format(x),
        s))


if __name__ == '__main__':

    x = 16
    [target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))

    x = 5
    [target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))

    x = 1
    [target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))