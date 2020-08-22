with open('input.txt', 'r', encoding="utf8") as fin:
    with open('output.txt', 'w', encoding="utf8") as fout:
        n = fin.readline()
        info = fin.readline()
        users = [int(x) for x in info.split(' ')]
        infinity = float("inf")
        users.sort()
        users.append(infinity)
        res = []
        for x in range(1, int(n) + 1):
            if users[x - 1] != x:
                users.insert(x - 1, x)
                res.append(x)
        fout.write(' '.join(map(str, res)))
