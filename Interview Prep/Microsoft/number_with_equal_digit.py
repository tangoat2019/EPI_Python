# https://leetcode.com/discuss/interview-question/365872/
import sys
def main():
	print(number([4,33,60]))

def cal_total_digit(n: int)-> int:
	ans = 0
	while n //10 > 0:
		ans += n % 10
		n = n //10
	ans += n
	return ans


def number(arr: list)-> int:
	ans, d = -1, {}
	for a in arr:
		ctd = cal_total_digit(a)
		if d.get(ctd) is None:
			d[ctd] = [a]
		else:
			arr = d.get(ctd)
			if len(arr) ==1:
				d[ctd].append(a)
			else:
				min_e = min(arr[0], arr[1])
				if a > min_e:
					arr.remove(min_e)
					arr.append(a)
	for k in list(d.keys()):
		arr = d.get(k)
		if arr is not None and len(arr) > 1:
			total = arr[0] + arr[1]
			if total > ans:
				ans  = total
	return ans


if __name__ == "__main__":
	main()