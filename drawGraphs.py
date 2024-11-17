import networkx as nx
import matplotlib.pyplot as plt


def create_graph(N, M, edges):
    G = nx.Graph()

    for i in range(N):
        G.add_node(i)

    for (n1, n2, weight) in edges:
        G.add_edge(n1, n2, weight=weight)

    return G


def draw_graph(G):
    # increase "k" to separate nodes
    pos = nx.spring_layout(G, k=0.5)

    # We draw the nodes with a larger size and select the color
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')

    # We draw the edge weight labels with a more visible color and size
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=10)

    plt.title("DrawGraphs")
    plt.show()


def main():
    N = int(input("Enter the number of nodes (N): "))
    M = int(input("Enter the number of edges (N): "))

    edges = []
    print("Enter the connections (n1, n2, weight) for each edge:")
    for _ in range(M):
        n1, n2, weight = map(int, input().split())
        edges.append((n1, n2, weight))

    G = create_graph(N, M, edges)
    draw_graph(G)


if __name__ == "__main__":
    main()

