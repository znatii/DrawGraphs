import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import scrolledtext
from Modules.search_algorithms import dfs, bfs
from Modules.minimum_spanning_tree import kruskal, prim
from Modules.shortest_path import dijkstra


class InteractiveGraph:
    def __init__(self, root, N, M, edges, directed, weighted):
        self.root = root
        self.root.title("DrawGraphs")

        # Create the graph: directed or undirected
        self.G = nx.DiGraph() if directed else nx.Graph()

        # Add nodes and edges to the graph
        for i in range(N):
            self.G.add_node(i)

        if weighted:
            for (n1, n2, weight) in edges:
                self.G.add_edge(n1, n2, weight=weight)
        else:
            for (n1, n2) in edges:
                self.G.add_edge(n1, n2)

        # Initial position of the nodes
        self.pos = nx.spring_layout(self.G, k=0.5)

        # Setting up for interactivity
        self.selected_node = None

        # Create the figure from matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Draw the graph
        self.directed = directed
        self.weighted = weighted
        self.draw_graph()

        # Connect events
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)

        # Add the button panel
        self.create_buttons()

        # Add the output text box
        self.output_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10)
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def draw_graph(self):
        # Clear the current graph
        self.ax.clear()

        # Draw nodes and edges
        nx.draw(
            self.G,
            self.pos,
            ax=self.ax,
            with_labels=True,
            node_color='skyblue',
            node_size=2000,
            font_size=12,
            font_weight='bold',
            arrows=self.directed,  # Show arrows if the graph is directed
            connectionstyle="arc3"  # Use straight lines for connections
        )

        # Draw edge weight labels if the graph is weighted
        if self.weighted:
            labels = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=labels, font_color="red", font_size=10)

        # Update figure in Tkinter
        self.canvas.draw()

    def on_click(self, event):
        # Detects if the click was near any node
        if event.inaxes != self.ax:
            return
        for node, (x, y) in self.pos.items():
            if (event.xdata - x) ** 2 + (event.ydata - y) ** 2 < 0.02:
                self.selected_node = node
                break

    def on_release(self, event):
        # Release the selected node
        self.selected_node = None

    def on_motion(self, event):
        # Move the selected node with the mouse
        if self.selected_node is not None and event.inaxes == self.ax:
            # Updates the node position
            self.pos[self.selected_node] = (event.xdata, event.ydata)
            self.draw_graph()  # Redraw the graph at the new position

    def create_buttons(self):
        # Create a frame for the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create buttons
        tk.Button(button_frame, text="DFS (Depth First Search)", command=self.run_dfs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="BFS (Breadth First Search)", command=self.run_bfs).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="MST (Minimum Spanning Tree)", command=self.run_mst).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Shortest Paths", command=self.run_shortest_paths).pack(side=tk.LEFT, padx=5)

    def run_dfs(self):
        #start_node = 0  # If you want to select the initial node
        #result = list(nx.dfs_edges(self.G, source=start_node)) # Use the NX libraries
        result = dfs(self.G)
        self.output_result("DFS from graph: {}".format(result))

    def run_bfs(self):
        #start_node = 0  # If you want to select the initial node
        #result = list(nx.bfs_edges(self.G, source=start_node)) # Use the NX libraries
        result = bfs(self.G)
        self.output_result("BFS from graph: {}".format(result))

    def run_mst(self):
        # Example: Replace with your actual function call
        if self.weighted:
            # With NX libraries
            #mst = nx.minimum_spanning_tree(self.G)
            #result = list(mst.edges(data=True))
            # With Kruskal
            result, mst_edges = kruskal(self.G.number_of_nodes(), self.G.adj)
            self.output_result("Minimum Spanning Tree Edges: {}. Value of MST: {}.".format(mst_edges, result))
            # With Prim
            #result, mst_nodes = prim(self.G.adj)
            #self.output_result("Minimum Spanning Tree Nodes: {} Value of MST: {}.".format(mst_nodes, result))
        else:
            self.output_result("MST calculation requires a weighted graph.")

    def run_shortest_paths(self):
        if self.weighted:
            lengths = ''
            for i in range (0, len(self.G)):
                start_node = i  # Example starting node
                try:
                    # With nx libraries
                    #lengths = nx.single_source_dijkstra_path_length(self.G, source=start_node)
                    #output.append("node {}: {}".format(start_node, lengths))
                    #self.output_result("Shortest paths from node {}: {}".format(start_node, lengths))
                    lengths += dijkstra(self.G.adj, start_node)
                except nx.NetworkXNoPath:
                    self.output_result("No paths found from node {}.".format(start_node))

            self.output_result("Shortest paths from:\n{}".format(lengths))
        else:
            self.output_result("Shortest paths requires a weighted graph.")


    def output_result(self, message):
        # Clear the output text box and insert the new message
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)


# Main function to run the interactive graph in Tkinter
def main():
    # Ask if the graph is weighted
    weighted = input("Is the graph weighted? (yes/no): ").strip().lower() == "yes"

    # Ask if the graph is directed
    directed = input("Is the graph directed? (yes/no): ").strip().lower() == "yes"

    # Read the number of nodes and edges
    N = int(input("Enter the number of nodes (N): "))
    M = int(input("Enter the number of edges (M): "))

    edges = []
    if weighted:
        print("Enter the connections (n1, n2, weight) for each edge:")
        for _ in range(M):
            n1, n2, weight = map(int, input().split())
            edges.append((n1, n2, weight))
    else:
        print("Enter the connections (n1, n2) for each edge:")
        for _ in range(M):
            n1, n2 = map(int, input().split())
            edges.append((n1, n2))

    # Create the Tkinter window and run the interactive graph
    root = tk.Tk()
    app = InteractiveGraph(root, N, M, edges, directed, weighted)
    root.mainloop()


if __name__ == "__main__":
    main()
