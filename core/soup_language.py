import copy
import inspect

from towards_mc.model import SemanticTransitionRelation, STR2TR
from towards_mc.model_checking import predicate_mc


class Behavior:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def __eq__(self, other):
        if not isinstance(other, Behavior):
            return False
        return self.name == other.name and self.guard == other.guard and self.action == other.action


class BehaviorSoup:
    def __init__(self, initial):
        self.initial = initial
        self.behaviors = []

    def add(self, name, guard, action):
        self.behaviors.append(Behavior(name, guard, action))

    def extend(self, beh):
        if isinstance(beh, Behavior):
            self.behaviors.append(beh)
        else:
            self.behaviors.extend(beh)


class BehaviorSoupSemantics(SemanticTransitionRelation):

    def __init__(self, soup):
        self.soup = soup

    def initial(self):
        return [self.soup.initial]

    def actions(self, configuration):
        return list(map(lambda ga: ga.action, filter(lambda ga: ga.guard(configuration), self.soup.behaviors)))

    def execute(self, action, configuration):
        target = copy.deepcopy(configuration)
        the_output = action(target)
        return target


def soup_predicate_model_checker(soup_program, predicate):
    semantics = BehaviorSoupSemantics(soup_program)
    transition_relation = STR2TR(semantics)
    predicate_mc(transition_relation, predicate)
