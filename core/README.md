# towards_mc

## Graph traversal

The file *traversal.py* defines 
- the bfs traversal of a graph
- a function 'predicate_finder', which check if a predicate is verified by any node of the graph

The graph traversal defined here has two characteristics:
- it is independent of the data-structure used to encode the graph. However, the graph need to implement the TransitionRelation contract.
- it exposes 3 callbacks, that can be used to perform different action during the traversal

Besides verifying that a predicate is verified by at least a node in the graph, 
the function ```predicate_finder``` uses the accumulator (```acc```) to compute the number of nodes that have been 
explored during the search.

## Model

The file *model.py* defines the different contracts needed.
The ```TransitionRelation``` abstract class defines a multi-root graph model.

## DictGraph

The file *traversal_dictgraph* implements the ```TransitionRelation``` contract for a graph represented with a dictionary.

The ```__main__``` illustrated a simple usage pattern of the bfs traversal, to find particular nodes in the graph

## NBits

The file *nbits.py* implements an implicit graph encoding all n-bit numbers, related by a one-bit-flip relation. 
The graph relation is encoded in the next function of the transition relation.

Using the NBits transition relation, we can lookup numbers in the graph using the predicate_finder function, 
as illustrated in the ```__main__``` part of the file.