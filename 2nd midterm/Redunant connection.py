from collections import defaultdict
import ast

def isConnected(src,target,visited,adjList):
  if src == target:
    return True
  visited[src] = True
  for neighbor in adjList[src]:
    if not visited[neighbor]:
      if isConnected(neighbor,target,visited,adjList):
        return True
  return False

def findRedunantConnection(edges):
  adjList = defaultdict(list)

  for u,v in edges:
    visited = [False]*1001
    if isConnected(u,v,visited,adjList):
      return [u,v]
    adjList[u].append(v)
    adjList[v].append(u)
  return []

edge_input = input("Enter edges:")
edges = ast.literal_eval(edge_input)
print(findRedunantConnection(edges))