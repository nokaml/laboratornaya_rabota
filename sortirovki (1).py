from random import randint
import math
sr = 0
pr = 0

# def Puzirek(n):
#    sr = 0
#    pr = 0 
#    for i in range(len(n) - 1):
#        for j in range(len(n) - i -1):
#            sr += 1
#            if n[j] > n[j+1]:
#                n[j], n[j+1] = n[j+1], n[j]
#                pr += 1
#    print(sr, pr)
#    return n

# def Vibor(n):
#    sr = 0
#    pr = 0
#    for i in range(len(n) - 1):
#        L = i
#        for j in range(i + 1, len(n)):
#            sr += 1
#            if n[j] < n[L]:
#                L = j
#                pr += 1
#        n[i], n[L] = n[L], n[i]
#    print (sr, pr)
#    return n

# def Vstavki(n):
#    sr = 0
#    pr = 0
#    for i in range(1, len(n)):
#        m = n[i]
#        j = i - 1
#        sr += 1
#        while (j >= 0 and m < n[j]):
#            pr += 1
#            sr += 1
#            n[j + 1] = n[j]
#            j = j - 1
#        n[j + 1] = m
#    print (sr, pr)
#    return n

def Qsort(n):
    global sr
    global pr
    if len(n) <= 1:
        return n
    else:
        otbor = n.pop()
    ig = []
    il = []
    for i in n:
        sr += 1
        if i > otbor:
            pr += 1
            ig.append(i)
        else:
            il.append(i)
    return Qsort(il) + [otbor] + Qsort(ig)

# def Shell(n): 
#     global sr
#     global pr
#     a = len(n)
#     k = int(math.log2(a))
#     r = 2**k -1
#     while r > 0:
#         for i in range(r, a):
#             t = n[i]
#             j = i
#             sr+=1
#             while (j >= r) and (n[j - r] > t):
#                 n[j] = n[j - r]
#                 j -= r
#                 pr += 1
#                 sr += 1
#             n[j] = t
#         k -= 1
#         r = 2**k -1
#     return n

#на 10 элементов
# a = [randint(0, 1000) for i in range(10)] 
# a.sort(reverse=False)
# b = [randint(0, 1000) for i in range(5)]
# b.sort(reverse=False)
# for i in range(5):
#     b.append(randint(0,1000))
# c = [randint(0, 1000) for i in range(10)]
# c.sort(reverse=True)
# print(Qsort(a),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
# print(Qsort(b),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
# print(Qsort(c),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные

#на 100 элементов
# a = [randint(0, 1000) for i in range(100)]
# a.sort(reverse=False)
# b = [randint(0, 1000) for i in range(50)]
# b.sort(reverse=False)
# for i in range(50):
#  b.append(randint(0,1000))
# c = [randint(0, 1000) for i in range(100)]
# c.sort(reverse=True)
# print(Qsort(a),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
# print(Qsort(b),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
# print(Qsort(c),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные

#на 1000 элементов
a = [randint(0, 1000) for i in range(1000)]
a.sort(reverse=False)
b = [randint(0, 1000) for i in range(500)]
b.sort(reverse=False)
for i in range(500):
   b.append(randint(0,1000))
c = [randint(0, 1000) for i in range(1000)]
c.sort(reverse=True)
print(Qsort(a),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
print(Qsort(b),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
print(Qsort(c),sr,pr) #Введите название сортировки, которую вы хотите использовать, а также "sr,pr", если в функции используются глобальные переменные
