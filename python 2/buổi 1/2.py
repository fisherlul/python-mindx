list = []
def getScore(inp: int):
    if 0 <= inp <= 100:
        list.append(inp) 
    
def findLowest(a: list):
    a.sort(reverse=True)
    a.pop(-1)

def calcAverage(b: list):
    average = 0
    findLowest(b)
    average = sum(b) / 4
    print(f"Average: {average}")

for i in range(5):
    inp = int(input("Input points: "))
    getScore(inp)

calcAverage(list)