import sys

def valid_index(r,c,l_r,l_c):
	return r>=0 and r<l_r and c>=0 and c<l_c and r != c
	
def validate (num):
	return num >0

def find_min_dis(q):
	m, k = sys.maxsize, 0
	for j in range(len(q)):
		if q[j][2] < m:
			m = q[j][2]
			k = j
	return k
	
def djisktra(graph, sr, sc, tr, tc):
	r,c = [1,1,1,0,-1,-1,-1,0],[-1,0,1,1,1,0,-1,-1]
	l_row, l_col = len(graph), len(graph[0])
	visited = [[False for i in range(l_col)] for j in range(l_row)]
	q = []
	q.append([sr,sc,0])
	while q:
		j = find_min_dis(q)
		s = q[j]
		if s[0] == tr and s[1] == tc:
			return s[2]
		visited[s[0]][s[1]] = True
		del q[j]
		for i in range(8):
			test_row = r[i] + s[0]
			test_col = c[i] + s[1]
			if valid_index(test_row, test_col, l_row, l_col) and validate(graph[test_row][test_col]) and visited[test_row][test_col]==False:
				q.append([test_row, test_col, graph[test_row][test_col] + s[2]])
	return 0

graph = [
	[1, 4, 3, 6],
	[2, 0, 6, 1],
	[1, 7, 0, 5],
	[0, 4, 2, 0]
]
dos = djisktra(graph, 0,0,2,3)
print(dos)
