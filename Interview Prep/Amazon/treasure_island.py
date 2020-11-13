# https://leetcode.com/discuss/interview-question/347457
import collections
import sys

def solution(maps: list)->int:
	def neighbor(maps: list, r: int, c: int)-> int:
		for i,j in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
			R= r+ i; C= c+ j
			if 0 <= R < len(maps) and 0 <= C < len(maps[0]) and maps[R][C] != 'D':
				yield R, C

	q = collections.deque([[0,0,0]]); ans = sys.maxsize; seen = [[0,0,0]]
	o = 4
	print('NAH:', o - (o>0))
	while q:
		curr = q.popleft()
		if maps[curr[0]][curr[1]] == 'X':
			if curr[2] < ans: ans = curr[2]
		else:
			for nei in neighbor(maps, curr[0], curr[1]): 
				if nei not in seen:
					seen.append(nei); q.append([nei[0], nei[1], curr[2]+ 1])
	return -1 if ans == sys.maxsize else ans

def main():
	print(solution([['O', 'O', 'O', 'X'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
))

if __name__ == "__main__":
	main()