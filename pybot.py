num = input("NUMBER ONE:\n")
operator = input("OPERATOR(+,-,*,/):\n")
num_2 = input("NUMBER TWO:\n")

num = float(num)
num_2 = float(num_2)
out = None
if operator == "+":
    out = num + num_2
elif operator == "-":
    out = num - num_2
elif operator == "*":
    out = num * num_2
elif operator == "/":
    out = num / num_2

print("ANSWER= " +str(out))
