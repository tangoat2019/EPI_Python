def validIndex(r,c,l_r,l_c):
	return r>=0 and r<l_r and c>=0 and c<l_c	
def validate (num):
	return num >0
def unstacking(s,visited,t_row, t_col, tr,tc,l_row,l_col):
	c, r = [0,-1,1,0], [-1,0,0,1]
	while len(s) > 0:
		g = s[len(s)-1]
		if g[0] == tr and g[1] == tc:
			return visited
		else:
			s.pop()
			visited[g[0]][g[1]]= True
			for i in range(4):
				t_row = g[0]+ r[i]
				t_col = g[1] + c[i]
				if validIndex(t_row, t_col, l_row, l_col) and validate(graph[t_row][t_col]) and visited[t_row][t_col] == False:
					visited[t_row][t_col]= True
					s.append([t_row, t_col])
					unstacking(s,visited,t_row,t_col,tr,tc,l_row,l_col)
def dfs(graph, sr, sc, tr, tc):
	l_row, l_col, s, dist = len(graph), len(graph[sr]), [], 0
	if sr == tr and sc == tc:
		return 0
	visited = [[False for i in range(l_col)] for j in range(l_row)]
	visited[sr][sc]= True
	s.append([sr,sc])
	unstacking(s,visited,0,0,tr,tc,l_row,l_col)
	return visited		
graph =     [
	[1, 0, 1, 1], 
	[1, 1, 1, 0], 
	[1, 0, 1, 1],
	[1, 1, 1, 0]
]; 
dos = dfs(graph, 0, 0, 3, 2)
print(dos)
