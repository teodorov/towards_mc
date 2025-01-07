from copy import deepcopy

from algos import predicate_finder
from kernel import ParentTracer


class HanoiConfiguration:
    def __init__(self, disk2stack, n_stacks):
        self.disk2stack = disk2stack
        self.stacks_top = self.stacks_top(n_stacks)

    def stacks_top(self, n_stacks):
        stacks_top = [None] * n_stacks
        for i, _ in enumerate(self.disk2stack):
            stack = self.disk2stack[i]
            if stacks_top[stack] is None:
                stacks_top[stack] = i
        return stacks_top

    def __repr__(self):
        return "H[" + str(self.stacks_top) + "]"

    def __eq__(self, other):
        if isinstance(other, HanoiConfiguration):
            return self.stacks_top == other.stacks_top and self.disk2stack == other.disk2stack
        return False

    def __hash__(self):
        return 1


class Hanoi:
    def __init__(self, n_disks, n_stacks):
        self.n_disks = n_disks
        self.n_stacks = n_stacks

    def roots(self):
        return [HanoiConfiguration([0] * self.n_disks, self.n_stacks)]

    def neighbors(self, source):
        ns = []
        for i in range(self.n_stacks):
            disk = source.stacks_top[i]
            if disk is None:
                continue
            for j in range(self.n_stacks):
                if source.stacks_top[j] is None or (
                        source.stacks_top[j] is not None and source.stacks_top[j] > disk):
                    d2s = deepcopy(source.disk2stack)
                    d2s[disk] = j
                    ns.append(HanoiConfiguration(d2s, self.n_stacks))
        return ns

    def is_solution(self, source):
        for i in range(self.n_stacks):
            if source.stacks_top[i] is not None and i != self.n_stacks - 1:
                return False
        return True


if __name__ == "__main__":
    h = Hanoi(3, 3)
    (s, v, c), _ = predicate_finder(h, lambda _: False)
    print(s, v, c)
    (s, v, c), _ = predicate_finder(h, h.is_solution)
    print(s, v, c)

    h = Hanoi(4, 4)
    (s, v, c), _ = predicate_finder(h, lambda _: False)
    print(s, v, c)
    (s, v, c), _ = predicate_finder(h, h.is_solution)
    print(s, v, c)

    h = Hanoi(3, 3)
    ht = ParentTracer(h)
    (s, v, c), _ = predicate_finder(ht, h.is_solution)
    print(s, v, c)
    if s:
        trace = ht.trace(v)
        print(trace)