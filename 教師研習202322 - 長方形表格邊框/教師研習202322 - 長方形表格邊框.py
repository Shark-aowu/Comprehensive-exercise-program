num = [int (i) for i in input("row column grld_size: ").split(" ")]
sci = [['+']]
scl = [['|']]
for i in range(0, num[2], 1): 
    sci[0] = sci[0] + ['-']
    scl[0] = scl[0] + [' ']
for i in range(0, num[2], 1): 
    sci = sci + scl
for i in range(0, num[0], 1):
    for i_ in range(0, num[2] + 1, 1):
        for j in range(0, num[1], 1):
            for j_ in sci[i_]:
                print(j_, end = "")
        print(sci[i_][0])
for j in range(0, num[1], 1):
    for j_ in sci[0]:
        print(j_, end = "")
print(sci[0][0])