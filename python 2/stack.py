input = "324*+"
def operator(result: int, s: str, a: int, b: int):
    if s == "+": 
        result = a + b
    elif s == "-": 
        result = a - b
    elif s == "*": 
        result = a * b
    elif s == "/": 
        result = a / b
    return result

def pushStack(stack_arr: list, num: int) -> None:
    stack_arr.append(num)
    return

def popStack(stack_arr: list) -> int:
    num_return = stack_arr[-1]
    stack_arr.pop(-1)
    return num_return

def preFix(input: str):
    stack_arr = list(input)
    
