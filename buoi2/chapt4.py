from random import randint

# bai 1
# def oldest_person(persons):
#     """Name personal max
#     Args:
#         person (dict):
#     """
#     nameMax = ''
#     max = 0
#     for key, value in persons.items():
#         if max < value:
#             max = value
#             nameMax = key
#     return nameMax
# persons = {
#   "Ba": 29,
#   "Phoebe": 22,
#   "Hà": 36,
#   "Anh": 27
# }
# print(oldest_person(persons))

# bai 2
# names = ["Nguyễn Ba", "Đỗ Phương Thảo", "Bùi Văn Hiên", "Lục Thanh Ngọc", "Bùi Tuấn Anh", "Phạm Thanh Hà"]
# def sort_by_name(names):
#     """Sort names
#     Args:
#         name (dict):
#     """
#     kq = sorted(names, key=lambda x: x.split(" ")[-1])
#     return kq
# print(sort_by_name(names))

# bai 3
# def get_random_hex():
#     """random hex
#     """
#     max = 16777216
#     kq = hex(randint(1, max)).replace('0x','#0')
#     return kq
# print(get_random_hex())

# bai 4
mang = [4,2,1]
def is_monotonic(list):
    listTangDan = sorted(list)
    listGiamDan = sorted(list, reverse=True)
    if list == listTangDan or list == listGiamDan:
        return True
    return False
print(is_monotonic(mang))       
    