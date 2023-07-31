n = int(input("N = "))
a = int(input("A = "))
b = int(input("B = "))
t = 0
for i in range(1, n + 1):
	if i % a == 0 or i % b == 0:
		t += i

print(f"Ket qua = {t}")