# some of these variables used as a switch or to calculate the score of players
counter, h, point1, point2, x, k, m, n, o, g, f, s, c, b, j = 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
sos_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# take copy from the original list to used in check horizontal function
x = sos_list.copy()
def sos():
    global sos_list
    for i in sos_list:
        print(i)

def game(h):
    sos()
    global sos_list, counter
    char = input("player " + h + "\nplease enter the character (s or o): ")
    while char != "s" and char != "o":
        char = input("player " + h + "\nplease enter the character (s or o) only: ")
    place = int(input("please enter the number of the place you need to put the character in: "))
    while place <= 0 or place > 16:
        place = int(input("please enter the number of the place in range 1 to 16 you need to put the character in: "))
    for i in sos_list:
        for x in i:
            if x == place:             # 1
                index = i.index(x)     # 2 in these three lines we replace the place by the character which the user choose
                i[index] = char        # 3
    counter += 1
    check_dia()
    check_horiz()
    check_ver()

def check_horiz():
    global point2, point1, sos_list, x
    for i in x:
        D = 0
        if i[0] == "s" and i[2] == "s" and i[1] == "o":     # 1
            D = 1                                           # 2
        elif i[1] == "s" and i[3] == "s" and i[2] == "o":   # 3 in these 4 lines we check if the first or the last 3 items in each small list make s-o-s
            D = 1                                           # 4
        if D == 1:
            index = x.index(i)
            x.pop(index)
            print("play again!")
            if h == "one":
                point1 += 1
            else:
                point2 += 1
            game(h)

def check_ver():
    global point2, point1, g, f, s, c
    v, z = 0, 0
    for i in range(2):
        # in this 4 lines (if statements) we check if there are three items above each other make s-o-s
        if sos_list[i][v] == "s" and sos_list[i+1][v] == "o" and sos_list[i+2][v] == "s" and c == 0:
            z += 1
            c = -1
        elif sos_list[i][v + 1] == "s" and sos_list[i+1][v + 1] == "o" and sos_list[i+2][v + 1] == "s" and s == 0:
            z += 1
            s = -1
        elif sos_list[i][v + 2] == "s" and sos_list[i+1][v + 2] == "o" and sos_list[i+2][v + 2] == "s" and f == 0:
            z += 1
            f = -1
        elif sos_list[i][v + 3] == "s" and sos_list[i+1][v + 3] == "o" and sos_list[i+2][v + 3] == "s" and g == 0:
            z += 1
            g = -1
    if z == 1:
        print("play again!")
        if h == "one":
            point1 += 1
        else:
            point2 += 1
        game(h)

def check_dia():
    global point2, point1, b, j, h, k, m, n, o, sos_list
    x, l = 0, 0
    for a in range(2):
        # in this 6 lines (if statements) we check if there are three items in diagonal shape make s-o-s
        if sos_list[a][a] == "s" and sos_list[a + 2][a + 2] == "s" and sos_list[a + 1][a + 1] == "o" and m == 0: #
            x += 1
            m = -1
    if sos_list[0][1] == "s" and sos_list[2][3] == "s" and sos_list[1][1] == "o" and n == 0:
        x += 1
        n = -1
    elif sos_list[1][0] == "s" and sos_list[3][2] == "s" and sos_list[2][1] == "o" and o == 0:
        x += 1
        o = -1
    for a in range(2):
        if sos_list[a][-(a+1)] == "s" and sos_list[a+2][-(a+3)] == "s" and sos_list[a+1][-(a+2)] == "o" and k == 0:
            l += 1
            k = -1
    if sos_list[0][2] == "s" and sos_list[2][0] == "s" and sos_list[1][1] == "o" and j == 0:
        l += 1
        j = -1
    if sos_list[1][-1] == "s" and sos_list[3][-3] == "s" and sos_list[2][-2] == "o" and b == 0:
        l += 1
        b = -1
    if l == 1 or x == 1:
        print("play again!")
        if h == "one":
            point1 += 1
        else:
            point2 += 1
        game(h)

for i in range(1, 33):
    if i % 2 == 0:
        h = "two"
    else:
        h = "one"
    game(h)
    if counter == 16:
        break
if point1 > point2:
    print("player one won!")
elif point1 < point2:
    print("player two won!")
else:
    print("your scores are equal,play again if you need!")