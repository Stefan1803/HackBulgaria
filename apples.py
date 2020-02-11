import math

casket_size = input("Enter the size of the box (example: 20x10): ")
# casket_size = "5x5"
# casket_size = "7x7"
(Nstr, Mstr) = casket_size.strip().split("x")
N = int(Nstr)
M = int(Mstr)

casket = [['0']*N for i in range(M)]

def printCasket():
    for line in casket:
        print(''.join(line))

cooridantes_input = input("Еnter the coordinates of the rotten apples (example: (3,8) (16,4)): ")
# cooridantes_input = "(2,2)"
# cooridantes_input = "(3,3)"

rotten_coordinates = []
def init_rotten():
    for xy in cooridantes_input.split(" "):
        (xStr, yStr) = xy.replace("(", "").replace(")", "").split(",")
        x = int(xStr)
        y = int(yStr)
        rotten_coordinates .append((x, y))
        casket[x][y] = "X"
    print(rotten_coordinates)
init_rotten()

days_until_return = int(input("After how many days will you come back: "))
rotten_range = math.floor(days_until_return / 3)

print("Initial rotten apples:")
printCasket()

for (x, y) in rotten_coordinates:
    for i in range(1, rotten_range + 1):
        for m in range(x - i, x + i + 1):
            for n in range(x - i, x + i + 1):
                try:
                    casket[m][n] = "X"
                except:
                    print("out of range ({},{})".format(m, n))

print("Rotten apples after {} days:".format(days_until_return))
printCasket()
