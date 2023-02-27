import time

#   Вывод простых чисел
def delit(x,y):
    if x%y == 0:
        return True

def prost(x):
    for i in range(2, int(x**0.5)+1):
        if delit(x,i):
            return False
    return True

a=[]
k=2
while len(a) != 500:
    if prost(k)==True:
        a.append(k)
    k+=1
b=""
for i in a:
    b += str(i)

#Алгоритм Кнута-Морриса-Пратта
#Создаем массив пи
def CreatePiList(arr):
    pi = [0]*len(arr)
    pi[0] = 0
    j = 0
    i = 1
    while i < len(arr):
        if arr[i] == arr[j]:
            pi[i] = j+1
            i += 1
            j += 1
        elif j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
    return pi
#Движения с индексами
def KMPsearch(s,txt):
    pi = CreatePiList(s)
    k=0 #индекс в образе
    l=0 #индекс в тексте
    count = 0
    while l < len(txt):
        if s[k] == txt[l]:
            k += 1
            l += 1
            if k == len(s):
                count += 1
                k=0
        elif s[k] != txt[l] and k != 0:
            k = pi[k-1]
        elif s[k] != txt[l] and k == 0:
            l+=1
    return count
a="31"
start = time.time()
print(KMPsearch(a, b))
print(time.time() - start)




            