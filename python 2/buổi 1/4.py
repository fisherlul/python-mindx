right_answer = ["A", "D", "B", "B", "C"]
inp_ans = []
wrong_ans = []

def showWrongAnswer(a : list,):
    print("- List of incorrect answers:")
    for i in range(0, len(a), 2):
        print(f"+ {a[i+1]} at position {a[i]}")

for i in range(len(right_answer)):
    inp = input(f"Input answer for question number {i+1}: ")
    if "A" <= inp <= "D":
        inp_ans.append(inp)
    else:
        inp_ans.append("x")
for i in range(len(inp_ans)):
    if inp_ans[i] != right_answer[i]:
        wrong_ans.append(inp_ans.index(inp_ans[i])+1)
        wrong_ans.append(inp_ans[i])

print(f"""Summary:
- Total number of correct answers: {20 - (len(wrong_ans) / 2)}
- Total number of incorrect answers: {len(wrong_ans) / 2}""")
showWrongAnswer(wrong_ans)