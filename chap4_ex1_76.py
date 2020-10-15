
def is_greater(a,b):
    if a > b :
        return a

    else:
        return b
a = int(input("Enter any two numbers: "))
b = int(input("Enter any two numbers: "))
big = is_greater ( a , b)

print(f"{big} is greater")