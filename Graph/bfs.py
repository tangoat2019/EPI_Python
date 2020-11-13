graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)
	while queue:
		s = queue.pop(0)
		print(s)
		for n in graph[s]:
			if n not in visited:
				visited.append(n)
				queue.append(n)

# Driver Code
bfs(visited, graph, 'A')