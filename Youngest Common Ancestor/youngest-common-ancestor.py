# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, d1, d2):
    visited = set()
    visited.add(topAncestor)
    node = d1
    while node != topAncestor:
        visited.add(node)
        node = node.ancestor
    node = d2
    while node not in visited:
        node = node.ancestor
    return node
