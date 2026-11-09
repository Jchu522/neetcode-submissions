"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {node:Node(node.val)}
        queue = [node]
        while queue:
            n = queue.pop(0)
            for nei in n.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val)
                    queue.append(nei)
                clone[n].neighbors.append(clone[nei])
        
        return clone[node]




        # def dfs(node: Optional['Node']):
        #     if node in clone:
        #         return clone[node]
            
        #     copy = Node(node.val)
        #     clone[node] = copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))

        #     return copy 
            
        # return dfs(node)
        



