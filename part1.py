import sys
from py2cfg.builder import CFGBuilder


def generate_cfg(file_path):
  builder = CFGBuilder()
  cfg = builder.parse_file(file_path)

  # Sort nodes by ID for consistent output
  nodes = sorted(cfg.nodes, key=lambda n: n.id)
  print(f"# of nodes = {len(nodes)}")

  for node in nodes:
    start = getattr(node, "start_line", getattr(node, "lineno", 1))
    end = getattr(node, "end_line", start)
    print(f"NODE {node.id}: line {start} - {end}")
    # Print the source code lines corresponding to this node
    source_code = getattr(node, "source", "")
    print(source_code.strip())

  # Edges extraction
  edges = cfg.edges
  print(f"# of edges = {len(edges)}")

  for edge in edges:
    # Handle different py2cfg edge representations robustly
    source_id = (
        edge.source.id if hasattr(edge, "source") else edge[0].id
    )
    target_id = (
        edge.target.id if hasattr(edge, "target") else edge[1].id
    )
    condition = getattr(edge, "conditional", getattr(edge, "condition", None))

    if condition:
      print(f"EDGE: node {source_id} -> node {target_id}, when ({condition})")
    else:
      print(f"EDGE: node {source_id} -> node {target_id}")


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python part1.py <path_to_python_file.py>")
    sys.exit(1)
  generate_cfg(sys.argv[1])