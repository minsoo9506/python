def print_all_friend(group, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu:
        p = qu.pop(0)
        print(p)
        for x in group[p]: 
            if x not in done:
                qu.append(x)
                done.append(x)