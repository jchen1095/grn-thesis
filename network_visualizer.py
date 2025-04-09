import matplotlib.pyplot as plt
import networkx as nx
import csv

# Set the file path to your data file
file_path = 'data/input/differentiation_input_GRN.txt'  # Change this to your actual file path

# Create a directed graph
G = nx.DiGraph()

# Read and parse data
with open(file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 4:
            continue  # Skip invalid rows
        try:
            regulated = int(float(row[0]))
            regulator = int(float(row[2]))
            regulation_value = float(row[3])
            color = 'green' if regulation_value > 0 else 'red'

            G.add_edge(regulator, regulated, weight=abs(regulation_value), color=color)
        except ValueError:
            continue  # Skip rows with bad values

# Draw the network
pos = nx.spring_layout(G, seed=42)
edge_colors = [G[u][v]['color'] for u, v in G.edges()]

plt.figure(figsize=(12, 10))
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True)

plt.title("Gene Regulatory Network\n(Green = Positive, Red = Negative)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()