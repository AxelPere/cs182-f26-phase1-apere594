# Part 1: print the control flow graph of a Python program
# python part1.py <program.py>

import ast
import sys
import warnings

warnings.filterwarnings("ignore")

from py2cfg import CFGBuilder

file_path = sys.argv[1]
cfg = CFGBuilder().build_from_file("main", file_path)

# find every block by following the arrows from the first block
all_blocks = {}
to_visit = [cfg.entryblock]

while len(to_visit) > 0:
    block = to_visit.pop()
    if block.id in all_blocks:
        continue
    all_blocks[block.id] = block
    for link in block.exits:
        to_visit.append(link.target)

# keep only the blocks that have code in them
nodes = []
for block in all_blocks.values():
    if len(block.statements) > 0:
        nodes.append(block)

# sort the nodes by starting line
nodes.sort(key=lambda block: block.at())

node_ids = []
for node in nodes:
    node_ids.append(node.id)

# keep only the edges between nodes that have code
edges = []
for node in nodes:
    for link in node.exits:
        if link.target.id in node_ids:
            edges.append(link)

# sort the edges by source, then target
edges.sort(key=lambda link: (link.source.id, link.target.id))

lines = []

lines.append("# of nodes = " + str(len(nodes)))
for node in nodes:
    start = str(node.at())
    end = str(node.end())
    lines.append("NODE " + str(node.id) + ": line " + start + " - " + end)
    lines.append(node.get_source().rstrip("\n"))
    lines.append("")

lines.append("# of edges = " + str(len(edges)))
for link in edges:
    source = str(link.source.id)
    target = str(link.target.id)
    text = "EDGE: node " + source + " -> node " + target

    if link.exitcase is not None:
        condition = link.get_exitcase().strip()

        # calls and names do not get parentheses
        no_parens = (ast.Call, ast.Name, ast.Attribute, ast.Subscript)

        has_parens = False
        if condition.startswith("(") and condition.endswith(")"):
            has_parens = True

        if not isinstance(link.exitcase, no_parens) and not has_parens:
            condition = "(" + condition + ")"

        text = text + ", when " + condition

    lines.append(text)

sys.stdout.write("\n".join(lines))