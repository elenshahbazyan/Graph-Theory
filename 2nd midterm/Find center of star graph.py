import ast
def findCenter(edges):
  a,b = edges[0]
  c,d = edges[1]
  if a == c or a == d:
    return a
  return b

edge_input = input("Enter edges list:")
edges = ast.literal_eval(edge_input)

print(findCenter(edges))