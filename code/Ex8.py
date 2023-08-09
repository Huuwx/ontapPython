s = input("S = ")
k = int(input("K = "))
if(len(s) < k * 2):
	print("Day khong lap")
else:
	dem = 0
	for i in range(0, k):
		if(s[i] != s[i + k]):
			dem = 0
		else:
			dem += 1
	if(dem >= 1):
		print(f"Day lap bac {k}")
	else:
		print("Day khong lap")
