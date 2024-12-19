from collections import deque


def bfs_traversal(g, integrator, opaque):
    (i, k, f) = (True, set(), deque())
    while i or f:
        neighbours = g.roots() if i else g.neighbors(f.popleft())
        i = False
        for n in neighbours:
            if n not in k:
                k.add(n)
                f.append(n)
                terminate = integrator(n, opaque)
                if terminate:
                    return opaque, k
    return opaque, k

def predicate_finder(g, predicate):
    def integrate(n, opaque):
        opaque[2] += 1
        opaque[0] = predicate(n)
        opaque[1] = n if opaque[0] else None
        return opaque[0]
    return bfs_traversal(g, integrate, [False, None, 0])
