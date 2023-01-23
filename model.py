from abc import abstractmethod


class TransitionRelation:
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class IdentityProxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class PreInitializedProxy(IdentityProxy):
    def __init__(self, operand, configurations):
        super().__init__(operand)
        self.configurations = configurations

    def initial(self):
        return self.configurations


class ParentTraceProxy(IdentityProxy):
    def __init__(self, operand, parents=None):
        super().__init__(operand)
        self.parents = {} if parents is None else parents

    def initial(self):
        neighbours = self.operand.initial()
        for n in neighbours:
            self.parents[n] = []
        return neighbours

    def next(self, configuration):
        neighbours = self.operand.next(configuration)
        for n in neighbours:
            if self.parents.get(n) is None:
                self.parents[n] = [configuration]
        return neighbours
