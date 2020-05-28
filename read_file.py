from Graph_map.graph_examples import graph_from_edgelist


def read_file(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()[:-1].split(' (')
            if len(line) <= 1:
                continue
            if len(line[-1].split(', ')) >= 2:
                for i in line[-1].split(', '):
                    edges.append((line[0], i))
            else:
                edges.append((line[0], line[-1]))
    # print(edges)
    g = graph_from_edgelist(edges, True)
    return g


def get_edges(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()[:-1].split(' (')
            if len(line) <= 1:
                continue
            if len(line[-1].split(', ')) >= 2:
                for i in line[-1].split(', '):
                    edges.append((line[0], i))
            else:
                edges.append((line[0], line[-1]))
    return edges


if __name__ == '__main__':
    print(read_file('stanford_cs.txt'))
