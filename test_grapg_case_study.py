from read_file import get_edges
import Graph_case_study.graph as graph_sample
import Graph_case_study.algorithms as algorithms


def stanfort_read(path):
    edges = get_edges(path)
    graph = graph_sample.LinkedDirectedGraph()

    for edge in edges:
        if edge[0] not in graph.vertices():
            graph.addVertex(edge[0])
        if edge[1] not in graph.vertices():
            graph.addVertex(edge[1])
        graph.addEdge(edge[0], edge[1], None)
    return graph


def topological_sort(graph):
    return algorithms.topoSort(graph)


if __name__ == "__main__":
    g = stanfort_read("stanford_cs.txt")
    print(f"Topological sort: \n{topological_sort(g)}")
