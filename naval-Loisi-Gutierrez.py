#tablero

print("  0 1 2 3 4 5 6 7 8 9")

hit = [21, 22]
miss = [20, 24, 12, 13]
comp = [23]

place = 0
for x in range(10):
    row = ""
    for y in range(10):
        ch = "  "
        if place in miss:
            ch = " x"
        elif place in hit:
            ch = " o"
        elif place in comp:
            ch = " 0"
        row = row + ch
        place = place + 1
    print(x, " ", row)