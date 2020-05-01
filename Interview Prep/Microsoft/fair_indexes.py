# https://github.com/galaumang/problemsolving/issues/16
import collections
def main():
	print(solution([4,-1,0,3], [-2,5,0,3], 4))

def solution(arr1: list, arr2: list, N: int)-> list:
	SUM1, SUM2, sum_dict1, sum_dict2, ans = 0,0, [], [], []
	for i in range(N):
		SUM1 += arr1[i]; SUM2 += arr2[i]
		sum_dict1.append(arr1[i] if i == 0 else arr1[i]+ arr1[i- 1])
		sum_dict2.append(arr2[i] if i == 0 else arr2[i]+ arr2[i- 1])
	for k in range(1,N):
		right_sum_1 = SUM1 - sum_dict1[k-1]
		right_sum_2 = SUM2 - sum_dict2[k-1]
		if right_sum_1 == right_sum_2 == sum_dict1[k-1] == sum_dict2[k-1]:
			ans.append(k)
	return ans

if __name__ == "__main__":
	main()