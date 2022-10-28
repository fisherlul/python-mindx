import random as r

def coinToss(inp: int):
    head = 0
    tail = 0
    for i in range(inp):
        if r.randint(1,2) == 1:
            head += 1
        else:
            tail += 1
    print(f"""Number of:
- Heads: {head}
- Tails: {tail} """)

inp = int(input("Input number of toss(es): "))
coinToss(inp)
