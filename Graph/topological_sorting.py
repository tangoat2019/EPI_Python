class Graph():
    def __init__(self, graph, v):
        self.graph = graph
        self.v = v
    def top_sorting_util(self,i_v, ans, visited):
        visited[i_v], current_v = True, self.v[i_v]
        for e in self.graph[current_v]:
            i_v_current = self.v.index(e)
            if visited[i_v_current] == False:
                self.top_sorting_util(i_v_current, ans, visited)
        ans.insert(0,current_v)
    def top_sorting(self):
        visited, ans = [False for j in range(len(self.v))], []
        for i_v in range(len(self.v)):
            if visited[i_v] == False:
                self.top_sorting_util(i_v, ans, visited)
        print(ans)
graph = {
    'a': [],
    'b': [],
    'c': ['d'],
    'd': ['b'],
    'e': ['a','b'],
    'f': ['a','c']
}
v = ['a','b','c','d','e','f']
g = Graph(graph, v)
g.top_sorting()