def validIndex(r,c,l_r,l_c):
	return r>=0 and r<l_r and c>=0 and c<l_c	
	
def validate (num):
	return num >0
		
def bfs(graph, sr, sc, tr, tc):
	l_row, l_col, q, dist = len(graph), len(graph[sr]), [], 0
	c, r = [0,-1,1,0], [-1,0,0,1]
	if sr == tr and sc == tc:
		return 0
	visited = [[False for i in range(l_col)] for j in range(l_row)]
	visited[sr][sc]= True
	q.append([sr,sc,dist])
	while len(q) > 0:
		sr, sc, dist = q[0][0], q[0][1], q[0][2]
		if sr==tr and sc==tc:
			return dist
		else:
			s = q.pop(0)
			for i in range(4):
				test_r = sr + r[i]
				test_c = sc + c[i]
				if validIndex(test_r, test_c, l_row, l_col) and validate(graph[test_r][test_c]) and visited[test_r][test_c] != True:
						visited[test_r][test_c] = True
						q.append([test_r, test_c, dist + 1])
	return -1
			
graph =     [
	[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], 
	[1, 0, 1, 0, 1, 1, 1, 1, 1, 1 ], 
	[1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ], 
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], 
	[1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ], 
	[1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ], 
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], 
	[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], 
	[1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ] 
]; 
dos = bfs(graph, 0, 0, 2, 7)
print(dos)
