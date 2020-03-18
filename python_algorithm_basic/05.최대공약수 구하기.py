# 예제
# def gcd(a, b):
#     i = min(a, b)
#     while True:
#         if a % i == 0 and b % i == 0:
#             return i
#         i = i - 1

# print(gcd(10,17))

# 재귀호출
# def gcd_recursive(a, b):
#     print("gcd : ", a, b)
#     if b == 0:
#         return a
#     return gcd(b, a%b) 

# gcd_recursive(10,16)
# gcd_recursive(64,16)    

# 연습 문제
def fibo(n):
    if n == 1:
        return 1
    return n + fibo(n-1)

print(fibo(10))