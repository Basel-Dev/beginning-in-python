prompt = "This is a calculator. What do you want to do? "

firstPrompt = input(prompt)
num1 = float(input("Insert a number: "))
num2 = float(input("Insert another number: "))


if firstPrompt == "+":
    result = num1+num2
elif firstPrompt == "*":
    result = num1*num2
elif firstPrompt == "-":
    result = num1-num2
elif firstPrompt == "/":
    result = num1/num2
elif firstPrompt == "^":
    result = num1**num2

print(result)