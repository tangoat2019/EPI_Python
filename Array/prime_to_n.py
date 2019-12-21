def prime_to_n(n):
    prime_list = [k] range n
    for i in range(len(n)):
        if prime_filter(i):
            mul = 2
            while i * mul < n:
                del n[i* mul]
                mul += 1       
    return prime_list


def prime_filter(n):
    for i in range(2, sqrt(n)):
        if n % i = 0:
            return False
    return True

n = 29
for p in prime_to_n(n):
    print(p)