def solution(N,K):
	if N == 0:
		return [""]
	result = []
	for p in solution(N - 1, (K - 1 if N<=K else K)):
		# print('P ',p, ' res ', result, ' and K ', K)
		for l in "abc":
			# print('Test ' ,p[-1:])
			if p[-1:] != l:
				result.append(p + l)
		# print('After ', result)
	return result[:K]

def main():
	print(solution(5,5))
		
if __name__ == "__main__":
	main()