import inspect

from towards_mc.model import ParentTraceProxy
from towards_mc.traversal import predicate_finder


def get_trace(parents, n, i):
    trace = [n]
    try:
        parent = parents[n]
    except KeyError:
        parent = None
    if isinstance(parent, list):
        parent = parent[0] if len(parent) > 0 else None
    while parent is not None:
        trace.append(parent)
        if parent in i:
            return trace
        try:
            parent = parents[parent]
            if isinstance(parent, list):
                parent = parent[0] if len(parent) > 0 else None
        except KeyError:
            parent = None
    return trace


def predicate_mc(transition_relation, predicate):
    print(f'{"-" * 50}\npredicate model-checking for:\n{inspect.getsource(predicate)}')

    op_tracer = ParentTraceProxy(transition_relation)

    [pred, found, count, target], known = predicate_finder(op_tracer, predicate)
    print(f'has reachable accepting state {found} after exploring ', count, ' configurations')

    the_trace = []
    if found is True:
        the_trace = get_trace(op_tracer.parents, target, op_tracer.roots())
        trace_string = f'\n{"-" * 20}\n'.join(str(x) for x in the_trace)
        print(f'The trace is: \n{trace_string}')
