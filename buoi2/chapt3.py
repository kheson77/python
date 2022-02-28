# bai 1
# 1m = 1000mm
# x = 0.1
# soLan = 0
# while x < 10000:
#     print(x)
#     soLan +=1
#     x *= 2

# bai 2
# tuoiCha = input("> ")
# tuoiCha = int(tuoiCha)
# tuoiCon = input("> ")
# tuoiCon = int(tuoiCon)
# soNamNua = 0
# while tuoiCon*2 < tuoiCha:
#     tuoiCha +=1
#     tuoiCon +=1
#     soNamNua +=1
# print(soNamNua)

# bai 3
# g + c = 36
# 2*(36 -c) + 4*c = 100
# cho = 0
# while 72 + 2*cho < 100:
#     cho +=1
# else: 
#     print(cho)
#     print(36 - cho)

# bai 4
# n = input("> ")
# def fibonacci(n):
#     if (n < 0):
#         return -1
#     elif (n == 0 or n == 1):
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(n)    
# sb = 0
# for i in range(0, n):
#     sb = sb + int(fibonacci(i))
# print(sb)

# bai 7
n = input("> ")
kq = ''
kyTuTruoc = n[0]
for i in n:
    if kyTuTruoc == '':
        kyTuTruoc = i
    else:
        if i == ' ':
            kq += kyTuTruoc
            kyTuTruoc = ''
kq += kyTuTruoc
sorted_characters = sorted(kq)
a_string = "".join(sorted_characters)
print(a_string)

# bai 8
sentence = "This is a common interview question"
