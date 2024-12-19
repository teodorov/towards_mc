class ParentTracer:
    def __init__(self, operand):
        self.operand = operand
        self.parent = dict()

    def roots(self):
        rs = self.operand.roots()
        for r in rs:
            self.parent[r] = []
        return rs

    def neighbors(self, r):
        ns = self.operand.neighbors(r)
        for n in ns:
            if n not in self.parent:
                self.parent[n] = r
        return ns

    def trace(self, r):
        if r not in self.parent:
            return []
        trace = [r]
        current = self.parent[r]
        while current:
            trace.append(current)
            current = self.parent[current]
        trace.reverse()
        return trace