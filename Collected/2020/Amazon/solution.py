#23280666857802
def solution(logFileSize, logLines):
	return sorted(logLines, key = sortFunc)

def sortFunc(x):
    _id, res = x.split(' ', 1)
    return (0, res, _id) if (res[0].isalpha()) else (1,)

def main():
	print(solution())
		
if __name__ == "__main__":
	main()