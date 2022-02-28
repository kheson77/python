# Chapt 2

# Bai 2
# numbers = [1, 3, 6, 4, 2, 6, 7]
# set(numbers)
# kq = sum(set(numbers))
# print(kq)

# Bai 3
# numbers = [1, 3, 6, 4, 2, 6, 7]
# set(numbers)
# kq = sorted(set(numbers))
# print(f"So lon thu 3 la: {kq[2]}") 


# Bai 5
# dict1 = {1: 'a', 2: 'b'}
# dict2 = {2: 'c', 4: 'd'}
# kq = dict1 | dict2
# print(f"kết hợp 2 dictionary thành 1 la: {kq}") 

# Bai 6
l1 = [(1, 2), (3, 4)]
l2 = [("a", "b"), ("c", "d")]
kq1 = sum(l1, ())
kq2 = sum(l2, ())
kq = set(kq1) | set(kq2)
print(kq)