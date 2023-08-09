n = int(input("Nhap N: "))
b = []
t = 0
for i in range (1, n + 1):
	gt = input(f"Nhap gia tri thu {i}: ")
	if gt.startswith('-'):
		s2 = gt.replace('-', '')
		if(s2.isdigit() == True or s2.replace('.', '').isdigit() == True):
			t += float(s2)
		else:
			b.append(gt)
	else:
		if(gt.isdigit() == True or gt.replace('.', '').isdigit() == True):
			t += float(gt)
		else:
			b.append(gt)

print(f"Tong cac phan tu cua A = {t}")
b1 = '-'.join(b)
print(f"B = {b1}")