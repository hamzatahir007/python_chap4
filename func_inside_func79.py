#first function
def is_greater(a,b):
    if a > b :
        return a

    else:
        return b

#second function
def new_greatest(a,b,c):
    bigger = is_greater(a,b)
    return is_greater (bigger , c)

print(new_greatest(11,45,0)) 