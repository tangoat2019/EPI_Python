def valid_index(t_row, t_col, ROW, COL):
	return t_row >= 0 and t_col >= 0 and t_row < ROW and t_col < COL
def flood_fill(graph, sr, sc, re):
	if len(graph) == 0:
		return None
	else:
		visited = [[False for i in range(len(graph[0]))] for j in range(len(graph))]
		visited[sr][sc] = True
		q, cur_val = [], graph[sr][sc]
		c,r = [-1,0,1,1,1,0,-1,-1],[1,1,1,0,-1,-1,-1,0]
		q.append([sr,sc])
		while len(q) >0:
			s = q.pop(0)
			graph[s[0]][s[1]] = re
			for j in range(8):
				t_row= s[0] +r[j]
				t_col= s[1] + c[j]
				if valid_index(t_row, t_col, len(graph),len(graph[0])) and graph[t_row][t_col] == cur_val and visited[t_row][t_col] == False:
					visited[t_row][t_col] = True
					q.append([t_row,t_col])
graph =     [
	[1, 0, 1, 1, 2, 1, 0, 1, 1, 1 ], 
	[1, 0, 1, 0, 2, 1, 1, 0, 1, 1 ], 
	[1, 1, 1, 0, 2, 2, 2, 1, 0, 1 ], 
	[0, 0, 0, 0, 2, 0, 0, 0, 0, 1 ], 
	[1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ], 
	[1, 3, 1, 1, 1, 1, 2, 1, 2, 0 ], 
	[1, 3, 3, 0, 0, 0, 2, 2, 2, 1 ], 
	[1, 3, 3, 3, 1, 1, 2, 2, 1, 1 ], 
	[1, 1, 3, 0, 0, 0, 1, 0, 0, 1 ] 
]; 
flood_fill(graph, 2, 5, 3)
print(graph)
