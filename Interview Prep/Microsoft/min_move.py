# https://leetcode.com/discuss/interview-question/398026/

def main():
	print(min_move('baaaaa'))

def min_move(s: str)-> int:
	res, i = 0, 0
	while i < len(s):
		next = i+1
		while next < len(s) and s[i] == s[next]:
			next += 1
		res += (next - i)/3
		i = next
	return res

if __name__ == "__main__":
	main()
