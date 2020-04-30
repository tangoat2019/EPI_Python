# https://leetcode.com/discuss/interview-question/373202
def solution(arr1: list, arr2: list, target:int)-> int:
	arr1.sort(key = lambda x: x[1])
	arr2.sort(key = lambda x: x[1])
	L1, L2, closest, ans  = len(arr1), len(arr2), [], []
	i1, i2 = 0, L2-1
	while i1 < L1 and i2 > -1:
		D = target - (arr1[i1][1] + arr2[i2][1])
		V = [i1,i2]
		if D >=0:
			if closest == []:
				closest = [V]
			else:
				C = target - (arr1[closest[0][0]][1] + arr2[closest[0][1]][1])
				if D < C:
					closest = [V]
				elif D == C:
					closest.append(V)
		if D >= 0: i1 += 1
		else: i2 -= 1
	for cl in closest:
		ans.append([arr1[cl[0]][0], arr2[cl[1]][0]])
	return ans

def main():
	print(solution(
		[[1, 8], [2, 7], [3, 14]],
		[[1, 5], [2, 10], [3, 14]],
		20))
		
if __name__ == "__main__":
	main()