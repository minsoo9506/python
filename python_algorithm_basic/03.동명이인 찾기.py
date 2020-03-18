# 예제
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ['kim', 'park', 'kim', 'song']
print(find_same_name(name))

# 연습문제 1
name = ['kim', 'park', 'song']
def pair(name):
    n = len(name)
    for i in range(n-1):
        for j in range(i+1, n):
            print(f'{name[i]} - {name[j]}')
pair(name)