class Node():
	def __init__(self,key):
		self.l = None
		self.r = None
		self.val = key
def insert(root, val):
	if val > root.val:
		if not root.r:
			root.r = Node(val)
		else:
			insert(root.r,val)
	if val <= root.val:
		if not root.l:
			root.l = Node(val)
		else:
			insert(root.l,val)
def search(root, k):
	if root:
		if root.val == k:
			return root.val
		elif root.val < k:
			print(root.val)
			return search(root.l,k)
		else:
			print(root.val)
			return search(root.r,k)
def delete(root, k):
	if root:
		if root.val == k:
			if not root.l:
				root = root.r
			else:
				far_temp, temp = root, root.l
				while temp.r:
					far_temp = temp
					temp = temp.r
				root.val = temp.val
				if temp.l:
					far_temp.r = temp.l
		elif root.val < k:
			return delete(root.l, k)
		else:
			return delete(root.r, k)
def bfs(root,k):
	if root:
		if root.val == k:
			return root
		else:
			print(root.val)
			bfs(root.l, k)
			bfs(root.r, k)
g = Node(10)
insert(g,7)
insert(g,19)
insert(g,12)
insert(g,21)
insert(g,9)
delete(g,9)
bfs(g,9)
		
