#!/usr/bin/env python3
import csv
import sys
import networkx as nx
from itertools import combinations

def load_graph(path):
    G = nx.DiGraph()
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            target = row[0]
            nregs  = int(float(row[1]))
            regs   = row[2:2+nregs]
            # Ks and coops ignored here
            for r in regs:
                G.add_edge(r, target)
    return G

def find_master_subdags(G):
    # masters = nodes with out_degree>0 and in_degree==0
    masters = [n for n in G.nodes() if G.in_degree(n)==0 and G.out_degree(n)>0]
    subdags = {}
    for m in masters:
        # all nodes reachable from m (excluding m itself if you like)
        reachable = set(nx.descendants(G, m))
        subdags[m] = reachable
    return subdags

def report_overlaps(subdags):
    for m1, m2 in combinations(subdags, 2):
        common = subdags[m1] & subdags[m2]
        if common:
            print(f"Masters {m1} and {m2} both regulate these genes:")
            print(" ", sorted(common))
    if not any(subdags[m1] & subdags[m2]
               for m1, m2 in combinations(subdags, 2)):
        print("No overlap between any two master‐driven sub‐DAGs.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_subdag_overlap.py gene_interactions.txt")
        sys.exit(1)
    G = load_graph(sys.argv[1])
    subdags = find_master_subdags(G)
    print("Master regulators and their downstream DAG sizes:")
    for m, nodes in subdags.items():
        print(f"  Master {m}: {len(nodes)} downstream genes")
    print("\nChecking for overlaps between sub-DAGs...\n")
    report_overlaps(subdags)
