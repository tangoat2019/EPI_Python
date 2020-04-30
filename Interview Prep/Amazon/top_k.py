# https://leetcode.com/discuss/interview-question/542597/
import collections

def top_k(keyword: list, review: list, k:int)-> int:
	c = collections.Counter()
	for r in review:
		temp_c = collections.Counter(r.lower().split(' '))
		d = [key for key in keyword if key in list(temp_c.keys())]
		c.update(d)
	return sorted(list(c.keys()), key= lambda x: (-c[x], x))[:k]

def main():
	print(top_k(
		["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
		[ "I love anacell Best services; Best services provided by anacell","betacellular has great services","deltacellular provides much better services than betacellular","cetracular is worse than anacell","Betacellular is better than deltacellular.",],
		2
		))
		
if __name__ == "__main__":
	main()