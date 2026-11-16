class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        q = [(0,-1)]
        visited.add(0)

        while q:
            node, parent = q.pop(0)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                visited.add(neigh)
                q.append((neigh,node))

        return len(visited) == n