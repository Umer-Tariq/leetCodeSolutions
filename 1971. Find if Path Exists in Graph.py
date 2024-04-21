class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        def dfs(d, source, destination, visited):
          if source == destination:
            return True
          visited.add(source)
          for neighbour in d[source]:
            if neighbour not in visited:
              if(dfs(d, neighbour, destination, visited)):
                return True

          #visited.discard(source)
          return False

        d = dict()
        for i in range(n):
          d[i] = []

        for edge in edges:
          d[edge[0]].append(edge[1])
          d[edge[1]].append(edge[0])
        visited = set()
        return dfs(d, source, destination, visited)

        

