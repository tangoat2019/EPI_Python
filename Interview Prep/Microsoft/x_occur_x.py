# https://github.com/galaumang/problemsolving/issues/16
import collections
import sys
def main():
	print(solution([5,5,5,5,5]))

def solution(arr1: list)-> list:
	c,ans = collections.Counter(arr1), -sys.maxsize
	for k in list(c.keys()):
		if k == c[k] and k > ans:
			ans = k
	return ans

if __name__ == "__main__":
	main()
