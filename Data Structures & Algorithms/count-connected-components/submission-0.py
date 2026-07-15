class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create empty dictionary
        Map = {i:[] for i in range(n)}
        components = 0
        for node, nei in edges:
            Map[node].append(nei)
            Map[nei].append(node)
        visit = set()

        def dfs(node):
            for i in Map[node]:
                if i not in visit:
                    visit.add(i)
                    dfs(i)

        for i in range(n):
            if i not in visit:
                dfs(i)
                components +=1
                
        return components        

