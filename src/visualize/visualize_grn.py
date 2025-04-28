import argparse
import csv
import networkx as nx
import matplotlib.pyplot as plt

def load_interactions(file_path):
    """
    Reads a gene interaction file where each row is:
    target, nRegs, reg1, reg2, ..., regN, K1, K2, ..., KN, coop1, coop2, ..., coopN
    Returns a directed graph with edge weights (regulatory strengths).
    """
    G = nx.DiGraph()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row or len(row) < 5:
                continue  # skip invalid lines
            target = row[0]
            nregs = int(float(row[1]))
            regs = row[2:2+nregs]
            Ks = row[2+nregs:2+2*nregs]
            # coop values are row[2+2*nregs : 2+3*nregs], usually unused for coloring
            for reg, k in zip(regs, Ks):
                weight = float(k)
                G.add_edge(reg, target, weight=weight)
    return G

def visualize_grn(G, title="Gene Regulatory Network"):
    """
    Visualizes the directed graph G using spring layout.
    Positive weights are colored green, negative red; edge thickness scales with magnitude.
    """
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600)
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    # Prepare edges
    edges = G.edges(data=True)
    colors = ['green' if data['weight'] > 0 else 'red' for _, _, data in edges]
    widths = [max(0.5, abs(data['weight'])) for _, _, data in edges]  # minimum width 0.5
    
    nx.draw_networkx_edges(
        G, pos,
        edge_color=colors,
        width=widths,
        arrowstyle='-|>',
        arrowsize=15
    )

    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Visualize a gene regulatory network from a CSV file.")
    parser.add_argument('file', help="Path to the gene interactions file (CSV)")
    args = parser.parse_args()

    G = load_interactions(args.file)
    visualize_grn(G)

if __name__ == "__main__":
    main()

# To run:
# python visualize_grn.py gene_interactions.txt
