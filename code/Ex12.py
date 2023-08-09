a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
arr = [a, b, c]
arr.sort()
if(arr[2] == arr[1] + (arr[1] - arr[0])): print("Nhiem vu hoan thanh")
else: print("Nhiem vu that bai")