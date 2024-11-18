import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


class InteractiveGraph:
    def __init__(self, root, N, M, edges, directed, weighted):
        self.root = root
        self.root.title("DrawGraph")

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
            connectionstyle="arc3"
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
