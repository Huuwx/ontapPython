n = int(input("N = "))
t = 0
rs = 0
import math
for i in range(1, n + 1):
	t += i
	rs += i / math.sqrt(t)

print(f"F({n}) = {rs:.7f}")