import Graph_map.dfs as dfs
import Graph_map.topological_sort as tp_sort
import Graph_map.bfs as bfs
from read_file import read_file


def graph_study(graph):
    bfs_test = bfs.BFS_complete(graph)
    dfs_test = dfs.DFS_complete(graph)
    topological_sort_test = tp_sort.topological_sort(graph)

    return bfs_test, dfs_test, topological_sort_test


def main(tests):
    names = ['bfs', 'dfs', 'topological_sort']
    for i in range(3):
        print(f"Result  of {names[i]}:")
        print(tests[i])
        print("-" * 40)



if __name__ == "__main__":
    g = read_file("stanford_cs.txt")
    main(graph_study(g))
