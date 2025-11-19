"""
HW05 — Warehouse Robot Path (Grid BFS)

Implement:
- parse_grid(lines)
- grid_shortest_path(lines)
"""

from collections import deque

def parse_grid(lines):
    """Return (graph, start, target) built from the grid lines.

    Graph keys are "r,c" strings for open cells. Neighbors move 4 directions.
    """
    graph = {}
    start = None
    target = None

    R = len(lines)
    C = len(lines[0]) if R else 0

    # collect open cells
    for r in range(R):
        for c in range(C):
            ch = lines[r][c]
            if ch == '#':
                continue

            node = f"{r},{c}"

            # detect start and target
            if 'S' in ch and 'T' in ch:
                start = target = node
            elif 'S' in ch:
                start = node
            elif 'T' in ch:
                target = node

            graph[node] = []

    # add neighbors only for open cells
    for r in range(R):
        for c in range(C):
            if lines[r][c] == '#':
                continue
            u = f"{r},{c}"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and lines[nr][nc] != '#':
                    v = f"{nr},{nc}"
                    graph[u].append(v)

    return graph, start, target


def grid_shortest_path(lines):
    """Return a shortest path list of "r,c" from S to T; or None if unreachable."""
    graph, start, target = parse_grid(lines)

    if start is None:
        return None
    if target is None:
        target = start
    if start == target:
        return [start]

    q = deque([start])
    parent = {start: None}

    while q:
        u = q.popleft()
        if u == target:
            break
        for v in graph.get(u, []):
            if v not in parent:
                parent[v] = u
                q.append(v)

    if target not in parent:
        return None

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path
