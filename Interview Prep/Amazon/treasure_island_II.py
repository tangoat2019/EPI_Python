# https://leetcode.com/discuss/interview-question/356150
import collections
import sys

def solution(maps: list)->int:
	def neighbor(maps: list, r: int, c: int)-> list:
		for i,j in [[0,-1], [-1,0], [0,1], [1,0]]:
			R= r+i; C= c+ j
			if 0 <= R < len(maps) and 0 <= C < len(maps[0]) and maps[R][C] != 'D' and maps[R][C] != 'S':
				yield R, C
	
	s_point, ans = [], sys.maxsize
	for i in range(len(maps)):
		for j in range(len(maps[0])):
			if maps[i][j] == 'S': s_point.append([i,j])
	
	for s in s_point:
		q = collections.deque([[s[0],s[1], 0]])
		seen = [[s[0], s[1], 0]]
		while q:
			curr = q.popleft()
			if maps[curr[0]][curr[1]] == 'X':
				if curr[2] < ans: ans = curr[2]
			else:
				for nei in neighbor(maps, curr[0], curr[1]):
					if nei not in seen:
						seen.append(nei); q.append([nei[0], nei[1], curr[2]+ 1])
	return ans if ans != sys.maxsize else -1

def main():
	print(solution([['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]))

if __name__ == "__main__":
	main()