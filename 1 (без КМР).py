import time

f = open('numbers.txt')
a = '' # записываем в переменную а 500 простых чисел
for i in range(42):
    b = f.readline().split()
    for j in b:
        a += j

def brute(a): # наивный метод
    answer = [0] * 90 # итоговый вывод: по индексу количество нахождений
                      # (напр. на 0 индексе число 10 и на этом месте количество нахождений)
    start = time.time()
    for i in range(10, 100): # берем всевозможные двузначные числа
        for j in range(len(a)-1):
            if i == int(a[j]+a[j+1]): # и сравниваем с каждой парой в строчке
                answer[i-10] += 1 # записываем если совпало
    print(time.time() - start)

    return answer

def rabin_karp(a): # алгоритм рабин карпа
    answer = [0] * 90
    x = 10 # размер алфавита
    
    start = time.time()
    for i in range(10, 100):
        if i//10 == i%10: # если числа совпали в шаблоне, то размер шаблона 1
            m = 1
        else:
            m = 2 # иначе размер шаблона 2
        h = (i//10)*x**m + (i%10)*x**(m-1) # подсчет хэша

        for j in range(len(a)-1):
            if h == int(a[j])*x**m + int(a[j+1])*x**(m-1): # сравниваем хэш шаблона и хэш в строчке
                if i == int(a[j]+a[j+1]): # если совпало сравниваем сами числа
                    answer[i-10] += 1 # записываем если все совпало
    print(time.time() - start)

    return answer

def boyer_moore(a): # алгоритм бойера мура
    answer = [0] * 90

    def check(element, pattern): # создаем рекурсивный метод
        for i in range(len(element)-1, -1, -1):
            if element[i] != pattern[i]:
                return element[i]
        return True

    
    start = time.time()
    for i in range(10, 100):
        pattern = str(i)
        j = 0
        while j < len(a)-1:
            element = a[j]+a[j+1]

            step = check(element, pattern)
            if step == True:
                answer[i-10] += 1
                j += 1
            else:
                if step in pattern:
                    j += len(pattern)-pattern.index(step)+1
                else:
                    j += len(pattern)
    print(time.time() - start)

    return answer

#b = boyer_moore(a)
#print(b.index(max(b))+10) # выводим число которое встречается чаще всего


#if brute(a) == rabin_karp(a) == b: # проверка что все алгоритмы работают правильно
#    print('yes')

naiv = brute(a)
rk = rabin_karp(a)
bm = boyer_moore(a)

print(naiv.index(max(naiv))+10)
print(rk.index(max(rk))+10)
print(bm.index(max(bm))+10)