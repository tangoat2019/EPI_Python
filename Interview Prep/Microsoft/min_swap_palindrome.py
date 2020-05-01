# https://leetcode.com/discuss/interview-question/351783/
import collections
def main():
	print(solution('aabb'))

def invalid(s: str)-> bool:
	c, odd_count = collections.Counter(s), 0
	for k in list(c.values()):
		if k % 2 == 1:
			odd_count += 1
		if odd_count > 1:
			return True
	return False
	
def find_palindrome(s: str)-> str:
	c, ideal_s, odd_key = collections.Counter(s), "", ""
	for key in list(c.keys()):
		ideal_s += key * (c[key] // 2)
		if c[key] == 1: odd_key = key
	ideal_s += odd_key + ideal_s[::-1]
	return ideal_s
	
def find_swap_step(s:str, sW: str, N: int)-> int:
	res, s1, s2, i, j = 0, list(s), list(sW), 0, 0
	while i < N:
		j = i
		while s1[i] != s2[j]:
			j += 1
		while i < j:
			s2[j], s2[j-1]= s2[j-1], s2[j]
			j -= 1
			res += 1
		i += 1
	return res
	
def solution(s: str)-> int:
	if invalid(s):
		return -1
	ideal_str = find_palindrome(s)
	return find_swap_step(s, ideal_str, len(s))
		
if __name__ == "__main__":
	main()
