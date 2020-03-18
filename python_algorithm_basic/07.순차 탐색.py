# 예제
def search(ls, x):
    for i in range(len(ls)):
        if ls[i] == x:
            return i
    return -1

print(search([1,2,3,4,5], 5))

# 연습문제
def search_multi(ls, x):
    index = []
    for i in range(len(ls)):
        if ls[i] == x:
            index.append(i)
    return index

print(search_multi([1,2,6,4,5,6], 6))

# 연습문제
def search_name(num_ls, name_ls, num):
    for i in range(len(name_ls)):
        if num_ls[i] == num:
            return name_ls[i]
num_ls = [26, 96, 59, 15]
name_ls = ['song', 'min', 'soo', 'kim']

print(search_name(num_ls, name_ls, 26))