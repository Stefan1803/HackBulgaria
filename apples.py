import math
import sys
casket_size = input("Enter the size of the box (example: 20x10): ")
(Nstr, Mstr) = casket_size.strip().split("x")
N = int(Nstr)
M = int(Mstr)

casket = [['0']*N for i in range(M)]
# casket = [['0']*M for i in range(N)]

def printCasket():
    for line in casket:
        print(''.join(line))

cooridantes_input = input("Еnter the coordinates of the rotten apples (example: (3,8) (16,4)): ")

rotten_coordinates = []
for xy in cooridantes_input.split(" "):
    (xStr, yStr) = xy.replace("(", "").replace(")", "").split(",")
    x = int(xStr)
    y = int(yStr)
    rotten_coordinates.append((x, y))
    try:
        casket[y-1][x-1] = "X"
    except:
        print("Given coordinates for rotten apples ({},{}) are out of range".format(x, y))
        sys.exit(0)
print(rotten_coordinates)

days_until_return = int(input("After how many days will you come back: "))
rotten_range = math.floor(days_until_return / 3)

print("Initial rotten apples:")
printCasket()

for (x, y) in rotten_coordinates:
    for i in range(1, rotten_range + 1):
        for n in range(y - i, y + i + 1):
            for m in range(x - i, x + i + 1):
                try:
                    casket[n-1][m-1] = "X"
                except:
                    print("out of range ({},{})".format(n, m))


print("Rotten apples after {} days:".format(days_until_return))
printCasket()
