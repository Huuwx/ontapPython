s = input("Nhap S: ")
dem = 0
for i in range(0, len(s)):
	if(s[i] == '!'):
		dem += 1
if (dem != 0) and (dem % 2 != 0):
	s += '!'

print(f"Chuoi S sau khi xu ly: {s}")