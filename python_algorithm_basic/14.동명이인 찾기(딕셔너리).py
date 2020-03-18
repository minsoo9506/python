# 예제
def find_name(ls):
    d = dict()
    for name in ls:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    result = set()
    for name in d:
        if d[name] >= 2:
            result.add(name)
    return result


ls = ['song', 'kim', 'song', 'park']
print(find_name(ls))
    