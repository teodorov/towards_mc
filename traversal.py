from collections import deque


def bfs(graph,
        acc,
        on_entry=lambda source, n, acc: False,
        on_known=lambda source, n, acc: False,
        on_exit =lambda source,    acc: False):
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        source = None
        if at_start:
            neighbours = graph.roots()
            at_start = False
        else:
            source = frontier.popleft()
            neighbours = graph.next(source)
        for n in neighbours:
            if n in known:
                if on_known(source, n, acc):
                    return acc, known
                continue
            else:
                if on_entry(source, n, acc):
                    return acc, known
                known.add(n)
                frontier.append(n)
        if on_exit(source, acc):
            return acc, known
    return acc, known


def predicate_finder(
        graph,
        predicate=lambda n: False):
    def check_predicate(s, n, a):
        # increment the count
        a[2] += 1
        # check predicate
        a[1] = predicate(n)
        # return true if predicate is true - stop the traversal
        return a[1]

    return bfs(graph, [predicate, False, 0], on_entry=check_predicate)
