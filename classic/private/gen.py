cells = list(map(lambda x: list(map(int, x.split())), '''17 18 33 1 49 2 3 34
50 51 52 4 19 5 6 35
53 54 20 55 56 36 7 57
37 8 38 39 58 9 21 22
59 60 40 23 10 11 41 12
24 42 13 25 26 61 27 28
14 43 44 62 45 29 30 31
15 46 47 32 48 16 63 64'''.split("\n")))

pos = [None] * 64

for i in range(len(cells)):
    for j in range(len(cells[i])):
        pos[cells[i][j] - 1] = (i, j)
        
table = [[None] * 8 for _ in range(8)]

letter = "Hello! Congratulations! Your reward: ©@rd4n0_is_not_classic_code"

assert(len(letter) == 64)

for i in range(len(letter)):
    x, y = pos[i]
    table[x][y] = letter[i]
    
print('\n'.join(map('\t'.join, table)))
