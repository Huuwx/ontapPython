n = int(input("N = "))
def tong(n):
	t = 0
	rs = 0
	for i in range (1, n + 1):
		t += i
		rs += i / t
	return rs

print(f"F({n}) = {tong(n):.6f}")