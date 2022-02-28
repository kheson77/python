import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 100)
y = (6 * x - 30) ** 2

# fig, ax = plt.subplots(dpi=100) # tạo figure và 1 axes

# fig.suptitle("Simple Example")  # đặt title cho figure

# ax.set_xlabel("X-Axis label")   # label cho các trục
# ax.set_ylabel("Y-Axis label")

# ax.plot(x, y)   # vẽ dữ liệu

# plt.show()  # hiển thị biểu đồ


# fig, ax = plt.subplots(dpi=100)

# fig.suptitle("Multiple Graphs")

# ax.set_xlabel("X-Axis label")
# ax.set_ylabel("Y-Axis label")

# ax.plot(np.sin(x), label="sin(x)")
# ax.plot(np.cos(x), label="cos(x)")

# ax.legend() # hiển thị label cho từng biểu đồ

# plt.show()


# tạo figure và 4 axes (2 hàng, 2 cột)
# fig, axes = plt.subplots(2, 2)  

# hoặc sử dụng cú pháp unpacking
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
#     2, 2, constrained_layout=True, figsize=(20, 10), dpi=100)

# fig.suptitle("Multiple Axes", fontsize=30)

# # vẽ dữ liệu trên từng axes
# ax1.set_title("sin(x)", fontsize=20)
# ax1.set_xlabel("X-Axis label", fontsize=13, color="#888")
# ax1.set_ylabel("Y-Axis label", fontsize=13, color="#888")
# ax1.plot(np.sin(x), linewidth=3, linestyle="solid", color="green")

# ax2.set_title("tan(x)", fontsize=20)
# ax2.set_xlabel("X-Axis label", fontsize=13, color="#888")
# ax2.set_ylabel("Y-Axis label", fontsize=13, color="#888")
# ax2.plot(np.tan(x), linewidth=3, linestyle="dashdot", color="red")

# ax3.set_title("cos(x)", fontsize=20)
# ax3.set_xlabel("X-Axis label", fontsize=13, color="#888")
# ax3.set_ylabel("Y-Axis label", fontsize=13, color="#888")
# ax3.plot(np.cos(x), linewidth=3, linestyle="dashed", color="grey")

# ax4.set_title("log(x)", fontsize=20)
# ax4.set_xlabel("X-Axis label", fontsize=13, color="#888")
# ax4.set_ylabel("Y-Axis label", fontsize=13, color="#888")
# ax4.plot(np.log(x), linewidth=3, linestyle="dotted", color="brown")

# plt.show()

# import mplcyberpunk
# plt.style.use("cyberpunk")

# fig, ax = plt.subplots(dpi=200)

# fig.suptitle("Cyberpunk Stylesheet")

# ax.plot([1, 3, 9, 5, 2, 1, 1], marker='p')
# ax.plot([4, 5, 5, 7, 9, 8, 6], marker='p')

# mplcyberpunk.add_glow_effects()
# plt.show()

# ba = (90, 67, 87, 76)
# beo = (80, 80, 47, 66)
# u = (40, 95, 76, 89)
# skills = ("Python", "Java", "Networking", "Machine Learning")

# width = 0.2
# index = np.arange(4)

# fig, ax = plt.subplots(dpi=150)

# ax.bar(index, ba,
#         width=width, label="Ba")
# ax.bar(index + width, beo,
#         width=width, label="Béo")
# ax.bar(index + width * 2, u,
#         width=width, label="Ú")

# ax.set_xticks(index + width, skills)
# ax.set_ylim(0, 120)
# ax.set_title("IT Skill Levels")
# ax.set_ylabel("Skill Level")
# ax.set_xlabel("IT Skill")
# ax.legend()
# plt.show()

# labels = ("Male", "Fermale", "Gay", "Other")
# values = (47, 42,13, 11)
# explode = (0, 0,0, 0.1)

# fig, ax = plt.subplots(dpi=150)
# fig.suptitle("Suptitle")

# ax.pie(values, labels=labels, autopct="%.2f%%", explode=explode)

# plt.show()

import mplcyberpunk
plt.style.use("cyberpunk")

fig, ax = plt.subplots(dpi=200)

fig.suptitle("Cyberpunk Stylesheet")

ax.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
ax.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

mplcyberpunk.add_glow_effects()
plt.show()