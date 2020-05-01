# Support for issue min swap to get palindrome
import collections
def main():
	print(solution('aabb', 'abba', 4))

def solution(s: str, sW: str, N: int)-> int:
	s1, s2, res, i, j = list(s), list(sW), 0, 0, 0
	while i < N:
		j = i
		while s1[i] != s2[j]:
			j+= 1
		while i<j:
			s2[j], s2[j-1]= s2[j-1], s2[j]
			j -= 1
			res += 1
		i += 1
	return res
if __name__ == "__main__":
	main()
