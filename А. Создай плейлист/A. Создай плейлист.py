with open('input.txt', 'r', encoding="utf8") as fin:
    with open('output.txt', 'w', encoding="utf8") as fout:
        n = int(fin.readline())
        id_ru = fin.readline().strip().split(' ')
        id_en = fin.readline().strip().split(' ')
        playlist = ['0' for _ in range(n * 2)]
        for i in range(0, n * 2, 2):
            playlist[i] = id_ru[i // 2]
        for j in range(1, n * 2 + 1, 2):
            playlist[j] = id_en[j // 2]
        fout.write(' '.join(playlist))
