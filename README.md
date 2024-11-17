# DrawGraphs

**DrawGraphs** is a Python program designed to generate and visualize weighted graphs. By providing the number of nodes, edges, and the connections between nodes with their respective weights, the program creates a visual representation of the graph and saves it as an image.

---

## Features

- **Customizable Graph Input:** Define the number of nodes, edges, and specific connections.
- **Weighted Edges:** Include weights for edges to create realistic graph models.
- **Visual Output:** Generates a clear graphical representation of the input graph.
- **Image Export:** Saves the graph as an image file for easy sharing or analysis.

---

## Requirements

Ensure you have the following installed in your environment:

- Python 3.6+
- Required Python libraries:
  - `networkx`
  - `matplotlib`

You can install the required libraries with the following command:

```bash
pip install networkx matplotlib
````

## How to Use

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/drawGraphs.git
cd drawGraphs
```

### 2. Run the Program
Execute the program using Python:
```bash
python3 drawGraphs.py
```

### 3. Input Data
### Input Data

When you run the program, you will be prompted to input the following:

1. **Number of Nodes (N):** Enter the total number of nodes in the graph.  
   Example: `4`  

2. **Number of Edges (M):** Enter the total number of edges in the graph.  
   Example: `3`  

3. **Connections and Weights:** For each edge, provide the following details:
   - `n1`: The starting node of the edge.
   - `n2`: The ending node of the edge.
   - `weight`: The weight of the edge.

#### Example Input:
```text
Enter the number of nodes (N): 4
Enter the number of edges (M): 5
Enter the connections (n1, n2, weight) for each edge:
0 1 5
0 2 1
1 2 3
1 3 2
2 3 7
```

### 4. Output
After processing the input, the program will:

1. Generate a graphical representation of the graph.
2. Save the graph as an image file (e.g., graph.png) in the same directory.

#### Example Output:
![img.png](img.png)

### 5. Contriubution
Contributions are welcome! Follow these steps to contribuite:
1. Fork the repository
2. Create a new branch (feature/my-feature):
```bash
git checkout -b feature/my-feature
```
3. Commit your chabges with a descriptive message:
```bash
git commit -am 'Add my feature'
```
4. Push the changes to your branch:
```bash
git push origin feature/my-feature
```
5. Open a Pull Request

### License 
This project is licensed under a Non-Commercial License. You may use, modify, and share the code for non-commercial purposes only. Commercial use requires prior written permission. See the [LICENSE](LICENSE) file for details.

### Contact 
If you have questions, feedback, or suggestions, feel free to reach out:

- Email: santiagotob0102@gmail.com
- GitHub: znatii
