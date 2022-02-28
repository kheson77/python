from re import X
import mplcyberpunk
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# Bai1
# plt.style.use("cyberpunk")
# data = {1940: 120, 1941: 122, 1942: 130, 1943: 110, 1944: 154, 1945: 165,
#         1946: 134, 1947: 128, 1948: 180, 1949: 170, 1950: 180, 1951: 192}
# x = list(data.keys())
# y = list(data.values())
# fig, ax = plt.subplots(dpi=100) # tạo figure và 1 axes
# fig.suptitle("Drama films by year")  # đặt title cho figure
# ax.set_xticks(x)
# ax.set_yticks(y)

# ax.plot(x, y, marker='o')   # vẽ dữ liệu
# plt.show()

# Bai2
# datas = {
#     "HN": {
#         2011: 2031.09,
#         2012: 2065.59,
#         2013: 2098.79,
#         2014: 2134.00,
#         2015: 2171.00,
#         2016: 2182.00,
#         2017: 2209.00,
#         2018: 2239.00,
#         2019: 2410.00,
#         2020: 2455.00,
#     },
#     "ND": {
#         2011: 1110.27,
#         2012: 1110.43,
#         2013: 1113.20,
#         2014: 1116.00,
#         2015: 1119.00,
#         2016: 1110.00,
#         2017: 1111.00,
#         2018: 1111.00,
#         2019: 1067.00,
#         2020: 1067.00,
#     },
#     "HCM": {
#         2011: 3578.16,
#         2012: 3655.42,
#         2013: 3731.63,
#         2014: 3809.00,
#         2015: 3888.00,
#         2016: 4025.00,
#         2017: 4097.00,
#         2018: 4171.00,
#         2019: 4385.00,
#         2020: 4476.00,
#     }
# }
# city = []
# plt.style.use("cyberpunk")

# fig, ax = plt.subplots(dpi=200)

# fig.suptitle("Mật độ dân số ở 1 số thành phố")

# ax.set_ylabel("Dân số")   # label cho các trục

# for value in datas.values():
#     x = list(value.keys())
#     y = list(value.values())
#     ax.plot(x,y,marker='o')
    
# ax.set_xticks([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

# mplcyberpunk.add_glow_effects()
# plt.show()

# Bai3
# data = {
#     "Nam": 28324.05,
#     "Nữ": 25285.53
# }
# values = data.values()
# explode = [0.05]
# for i in range(len(values)):
#     if i!=0:
#         explode.append(0)

# fig, ax = plt.subplots(dpi=150)
# fig.suptitle("")
# ax.pie(values, labels=data.keys(), autopct="%.2f%%", explode=explode)
# plt.show()

# Bai4
data = dict(apples=10, oranges=15, lemons=5, limes=20)
plt.style.use("cyberpunk")
fig, ((ax1, ax2, ax3)) = plt.subplots(
    1, 3, constrained_layout=True, figsize=(20, 10), dpi=50)
x = list(data.keys())
y = list(data.values())

# creating the bar plot
ax1.bar(x, y,
        width = 0.3)
ax2.scatter(x, y)
ax3.plot(x, y)
 
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.legend()
plt.show()

# Bai5
