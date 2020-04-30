class Node():
	def __init__(self, parent=None, X=None, Y=None):
		self.parent = parent
		self.x = X
		self.y = Y
		self.g = 0
		self.h = 0
		self.f = 0

def valid_index(x,y, l_row, l_col):
	return x >= 0 and y >= 0 and x < l_row and y < l_col

def walkable(maze, x, y):
	return maze[x][y] == 0

def h_distance(child, end_node):
	return ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
	
def node_in_list(node, list):
	for l in list:
		if l.x == node.x and l.y == node.y:
			return True
	return False

def find_min_f(opened):
	node, i_node = opened[0], 0
	for i,n in enumerate(opened):
		if n.g < node.g:
			node = n
			i_node = i
	return i_node
	
def astar(graph, sr, sc, tr, tc):
	s_node = Node(None, sr, sc)
	row, col = [1,1,1,0,-1,-1,-1,0], [-1,0,1,1,1,0,-1,-1]
	l_row, l_col = len(graph), len(graph[0])
	opened, closed, path = [], [], []
	opened.append(s_node)
	while len(opened) > 0:
		curr_i = find_min_f(opened)
		curr = opened[curr_i]
		if curr.x == tr and curr.y == tc:
			while curr:
				path.append([curr.x, curr.y])
				curr = curr.parent
			return path[::-1]
		del opened[curr_i]
		closed.append(curr)
		for i in range(8):
			test_row = curr.x + row[i]
			test_col = curr.y + col[i]
			test_node = Node(curr, test_row, test_col)
			test_node.g = curr.g + 1
			test_node.h = test_col + test_row - tr - tc
			test_node.f = test_node.g + test_node.h
			if valid_index(test_row, test_col, l_row, l_col) and walkable(graph, test_row, test_col) and not node_in_list(test_node, closed):
				if not node_in_list(test_node,opened):
					opened.append(test_node)
				else:
					for l in opened:
						if l.x == test_node.x and l.y == test_node.y and l.g > test_node.g:
								l.parent = curr
								temp = l.g
								l.g = test_node.g
								l.f = l.f - temp + test_node.g
	return None

maze = [
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,1,0]
]

path = astar(maze, 0, 0, 3, 4)
print(path)
