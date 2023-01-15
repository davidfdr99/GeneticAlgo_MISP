import itertools
import networkx as nx
from collections import OrderedDict


def genome_to_solution_nodes(graph, genome) -> list:
    dict = OrderedDict(sorted(nx.to_dict_of_lists(graph).items()))
    res = []
    for i, node in enumerate(dict.keys()):
        if genome[i] == 1:
            res.append(node)
    return res

def _is_independet_set(graph, nodes) -> bool:
    if len(graph) == 0:
        print("The Graph does not contain any vertices")
    if len(graph) == 1:
        print("The Graph is an independent set of one Node")
    else:
        xi = []
        for u in graph.nodes():
            if u in nodes:
                neighbors = nx.all_neighbors(graph, u)
                for v in neighbors:
                    if v not in xi:
                        xi.append(u)
                    else:
                        return False
    return True

class BruteForce():

    def __init__(self, graph):
        self.graph = graph
        self.nodes = list(graph.nodes)
    
    def Run(self):

        res = 0
        best_score = 0
        combinations = [list(i) for i in itertools.product([0, 1], repeat=len(self.nodes))]
        solutions = [genome_to_solution_nodes(self.graph, comb) for comb in combinations]

        for sol in solutions:
            if _is_independet_set(self.graph, sol) == True:
                score = len(sol)
                if score > best_score:
                    res = sol
                    best_score = score
        
        return res