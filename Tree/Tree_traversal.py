class Node():
	def __init__ (self, key):
		self.l = None
		self.r = None
		self.val = key
def in_order(root):
	if root:
		in_order(root.l)
		print(root.val)
		in_order(root.r)
def post_order(root):
	if root:
		post_order(root.l)
		post_order(root.r)
		print(root)
def pre_order(root):
	if root:
		print(root.val)
		pre_order(root.l)
		pre_order(root.r)
def bfs(root,level):
	if root:
		if level == 0:
			print(root.val)
		if root.l:
			print(root.l.val)
		if root.r:
			print(root.r.val)
		bfs(root.l, level+1)
		bfs(root.r, level+1)
def dfs(root, level):
	if root:
		if level == 0:
			print(root.val)
		dfs(root.l, level+1)
		dfs(root.r, level+1)
		if root.l:
			print(root.l.val)
		if root.r:
			print(root.r.val)
root = Node(1) 
root.l      = Node(2) 
root.r     = Node(3)
root.r.l = Node(7)
root.l.l  = Node(4) 
root.l.r  = Node(5)
root.l.r.r = Node(6)
pre_order(root)
