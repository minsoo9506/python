# 예제 1
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(factorial(5))

def real_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * real_factorial(n-1)

print(real_factorial(5))

# 연습 문제1
def sum_fac(n):
    if n <= 1: return 1
    else : return n + sum_fac(n-1)

print(sum_fac(5))

# 연습 문제2
num = [1,4,6,8,9,10,34,76,43]
def findMax(num, n):
    if n==1:
        return num[0]
    else:
        max = findMax(num, n-1)
        if max > num[n-1]:
            return max
        else:
            return num[n-1]
print(findMax(num, len(num)))


        

