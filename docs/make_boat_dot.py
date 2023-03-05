"""
gen dot diagram for inspiration
"""
import random

def randstr(length, charset):
    """Generate a random string of given length from the given character set."""
    return "".join(random.choice(charset) for i in range(length))

# Set up node and edge data
NUM_NODES = 6
nodes = [f"boat{i}" for i in range(1, NUM_NODES+1)]
edges = []
for i in range(NUM_NODES):
    num_edges = random.randint(1, 5)
    for j in range(num_edges):
        k = random.randint(0, NUM_NODES-1)
        if k != i and (i, k) not in edges and (k, i) not in edges:
            edges.append((i, k))

# Generate dot file
with open("signal_k_observation.dot", "w") as f:
    f.write("graph signal_k_observation {\n")
    f.write("    node [style=filled, color=white, fontname=Arial, fontsize=16]\n")
    f.write("    edge [color=gray, penwidth=2, style=dashed]\n")
    f.write("    \n")
    for i, node in enumerate(nodes):
        f.write(f'    {node} [shape=circle, fontsize=16]\n')
        for j in range(4):
            LABEL = randstr(4, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            color = ["#8fb1cc", "#9bd3b4", "#f6b0b7", "#c6c6c6"][j]
            f.write(f'    {node}_{j} [label="{LABEL}", shape=rectangle, style=filled, color="{color}", fontcolor=white, width=0.7, height=0.7, fixedsize=true]\n')
            f.write(f'    {node} -- {node}_{j} [style=invis]\n')
    f.write("    \n")
    for edge in edges:
        f.write(f"    {nodes[edge[0]]} -- {nodes[edge[1]]} [penwidth=2, style=dashed]\n")
    f.write("}\n")
