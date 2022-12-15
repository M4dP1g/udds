def conv(x):
    res = [0, 0, 0]
    for i in range(x):
        m = max(res)
        if m == res[0]:
            if m == res[1]:
                if m == res[2]:
                    res[0] += 1
                    res[1] = 0
                    res[2] = 0
                else:
                    res[2] += 1
                    if res[2] < m:
                        res[0] = m
                    else:
                        res[0] = 0
                    res[1] = 0
            else:
                res[1] += 1
                if res[1] < m and res[2] < m:
                    res[0] = m
                else:
                    res[0] = 0
        else:
            res[0] += 1
    return res


results = []
for i in range(0, 10648 + 1):
    converted = conv(i)
    print(f'{i} -> {converted}')
    if converted in results:
        print('AAAAAAAAAAAAAAAAAAA')
        exit(-1)
    results.append(converted)
