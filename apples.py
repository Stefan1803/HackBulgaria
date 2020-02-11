import math

# casket_size = input("Enter the size of the box (example: 20x10): ")
casket_size = "10x10"
(Nstr, Mstr) = casket_size.strip().split("x")
N = int(Nstr)
M = int(Mstr)

casket = [['0']*N for i in range(M)]

def printCasket():
    for line in casket:
        print(''.join(line))

# cooridantes_input = input("Еnter the coordinates of the rotten apples (example: (3,8) (16,4)): ")
# cooridantes_input = "(3,4) (6,7)"
cooridantes_input = "(6,7)"

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

def markAsRotten(x, y):
    try:
        casket[x][y] = "X"
    except:
        print("out of range ({},{})".format(x, y))

print("Initial rotten apples:")
printCasket()

for (x, y) in rotten_coordinates:
    for i in range(1, rotten_range + 1):
        print(i)
        markAsRotten(x-i, y-i)
        markAsRotten(x-i, y)
        markAsRotten(x-i, y+i)
        markAsRotten(x, y-i)
        markAsRotten(x, y)
        markAsRotten(x, y+i)
        markAsRotten(x+i, y-i)
        markAsRotten(x+i, y)
        markAsRotten(x+i, y+i)

print("Rotten apples after {} days:".format(days_until_return))
printCasket()

X0X0X
0XXX0
XXXXX
0XXX0
X0X0X