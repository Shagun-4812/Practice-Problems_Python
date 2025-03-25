from collections import defaultdict

class MiningTunnels:
    def __init__(self):
        self.graph = defaultdict(list)
        self.longest_path = []
        self.max_depth = 0

    def add_connection(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited, path, depth):
        visited.add(node)
        path.append(node)

        if depth > self.max_depth:
            self.max_depth = depth
            self.longest_path = list(path)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, path, depth + 1)

        path.pop()
        visited.remove(node)

    def find_deepest_path(self, start):
        self.dfs(start, set(), [], 0)
        return self.longest_path, self.max_depth

# Example usage
tunnels = MiningTunnels()
tunnels.add_connection(1, 2)
tunnels.add_connection(1, 3)
tunnels.add_connection(2, 4)
tunnels.add_connection(2, 5)
tunnels.add_connection(3, 6)
tunnels.add_connection(5, 7)
tunnels.add_connection(5, 8)
tunnels.add_connection(7, 9)

path, depth = tunnels.find_deepest_path(1)
print(f"Deepest path: {path}")
print(f"Maximum depth: {depth}")