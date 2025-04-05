from collections import defaultdict

def build_adjacency_list(edges: list)-> dict:
    """辺のリストから隣接リストを作成します。"""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # 無向グラフなので双方向に追加
    return adj

def get_vertices(adj):
    """隣接リストから全ての頂点の集合を取得します。"""
    vertices = set(adj.keys())
    for neighbors in adj.values():
        vertices.update(neighbors)
    return vertices

def is_connected(adj: dict) -> bool:
    """深さ優先探索でグラフが連結かどうかを判定します。"""
    vertices = get_vertices(adj)
    if not vertices:
        return True  # 空のグラフは連結とみなす

    start_node = next(iter(vertices))
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited == vertices

def classify_eulerian_standard(edges: list) -> str:
    """
    与えられた辺のリストから、グラフがオイラーグラフ、準オイラーグラフ、
    そうでないグラフのいずれであるかを分類します（標準モジュールのみ使用）。

    Args:
        edges: 辺のリスト (例: [(1, 2), (2, 3), ...])

    Returns:
        str: グラフの種類
    """
    adj = build_adjacency_list(edges)

    if not is_connected(adj):
        return "Not Eulerian or Semi-Eulerian graph (disconnected)"

    odd_degree_nodes = 0
    for node in get_vertices(adj):
        degree = len(adj.get(node, []))
        if degree % 2 != 0:
            odd_degree_nodes += 1

    if odd_degree_nodes == 0:
        return "Eulerian graph"
    elif odd_degree_nodes == 2:
        return "Semi-Eulerian graph"
    else:
        return "Not Eulerian or Semi-Eulerian graph"

if __name__ == '__main__':

    # グラフの辺のリストの例
    edges1 = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)]
    edges2 = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (4, 6)]
    edges3 = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4), (1, 4)]
    edges4 = [(1, 2), (2, 3)]
    edges5 = [(1, 2), (1, 4), (2, 3), (2, 6), (2, 5), (3, 6), (4, 5), (4, 7), (4, 8), (5, 6), (5, 8), (6, 9), (7, 8), (8, 9)]

    # 分類を実行して結果を表示
    print(f"Graph 1: {classify_eulerian_standard(edges1)}")
    print(f"Graph 2: {classify_eulerian_standard(edges2)}")
    print(f"Graph 3: {classify_eulerian_standard(edges3)}")
    print(f"Graph 4: {classify_eulerian_standard(edges4)}")
    print(f"Graph 5: {classify_eulerian_standard(edges5)}")

    # 非連結なグラフの例
    edges6 = [(1, 2), (3, 4)]
    print(f"Graph 6 (disconnected): {classify_eulerian_standard(edges6)}")