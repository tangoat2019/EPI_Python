graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set()

def dfs(visited, graph, node):
	if node not in visited:
		print(node)
		visited.add(node)
		for n in graph[node]:
			dfs(visited, graph, n)

dfs(visited, graph, 'A')