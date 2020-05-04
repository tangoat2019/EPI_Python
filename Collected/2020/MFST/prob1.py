def solution(N: int):
	s, ans, inserted, positive = str(abs(N)), "", False, False
	if N > 0: positive = True
	if N == 0: return 50
	for i,char in enumerate(s):
		if not inserted and ((5 >= int(char) and positive) or (5< int(char) and not positive)):
			ans = s[:i] + '5' + s[i:]
			inserted = True
	if not inserted:
		ans = s + '5'
	return int(ans) * (1 if positive else -1)

def main():
	print(solution(670))
		
if __name__ == "__main__":
	main()