with open('input.txt', 'r', encoding="utf8") as fin:
    with open('output.txt', 'w', encoding="utf8") as fout:
        n = fin.readline()  # целое число n, по модулю не превосходящее 10000
        if int(n) != 0:
            n = n.rstrip('0')
        if int(n) < 0:
            res = '-' + n[:0:-1]
        else:
            res = n[::-1]
        fout.write(res)
