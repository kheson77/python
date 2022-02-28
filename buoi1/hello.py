import math

#cach print python3 hello.py
# bai 1
# a = input("> ")
# b = input("> ")

# print(int(a+b))

# bai2 
# print('Nhap vao do C')
# c = input("> ")
# kq = 1.8* float(c) + 32
# print(f"Nhiet do khi chuyen sang do F la: {kq}") 

# bai3
# print('Nhap a:')
# a = input("> ")
# print('Nhap b:')
# b = input("> ")
# kq = int(a)*int(b)
# print(f"S hinh chu nhat la: {kq}")

# bai 4
# print('Nhap số tiền gốc ban đầu p:')
# p = input("> ")
# print('Nhap lãi suất hàng năm r:')
# r = input("> ")
# print('Nhap số lần ghép lãi 1 năm n:')
# n = input("> ")
# print('Nhap số năm gửi ngân hàng t:')
# t = input("> ")

# kq = float(p) * (1 + float(r)/float(n))**(float(n)*float(t))
# print(f"Tính và in ra lãi suất kép theo công thức co kq: {kq}")

# # bai 5
# print('So a:')
# a = input("> ")
# print('So b:')
# b = input("> ")
# print('So c:')
# c = input("> ")

# a = float(a)
# b = float(b)
# c = float(c)


# S = (a+b+c)/2

# area = (S * (S - a) * (S - b) * (S - c))
# kq = area**(1/2)
# print(f"diện tích hình tam giác theo công thức {kq}")
a = ()

# Chapt2
#Bai1 
# print('Nhập vào:')
# s = 'tHE fOX iS cOMING fOR tHE cHICKEN'
# kq = s.swapcase()
# print(kq)

# Bai2
# numbers = [1, 3, 6, 4, 2, 6, 7]
# set(numbers)
# kq = sum(set(numbers))
# print(kq)

# Bai3
# numbers = [1, 3, 6, 4, 2, 6, 7]
# kq = sorted(set(numbers))
# print(kq[3])


# Bai 4
l = [1, 2, 3, 5 ,2]
so_dau = l[0]
chieu_dai = len(l)
so_cuoi = l[chieu_dai-1]

l[0] = so_cuoi
l[so_cuoi] = so_dau
print(l)