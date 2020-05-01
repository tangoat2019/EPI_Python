# https://leetcode.com/discuss/interview-question/398026/

def main():
	print(min_move('baabab'))

def min_move(s: str)-> int:
	r_count, ans = 0, 0
	if len(s) == 0: return 0
	r_char = s[0]
	for i,c in enumerate(s):
		if c == r_char:
			r_count += 1
			if r_count == 3:
				r_char = 'a' if c == 'b' else 'b'
				r_count = 1
				ans += 1
		else:
			r_char = c
			r_count = 1
	return ans
		
if __name__ == "__main__":
	main()
