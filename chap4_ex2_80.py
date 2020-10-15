
def is_plindrome (name):
    reversed_word = name[::-1] 
    if name == reversed_word:
        return True
    else:
        return False
user_name = input("Enter a name in plindrome: ")
#Enter a name in plindrome: naman (true)
#Enter a name in plindrome: hamza (false)
print(is_plindrome(user_name))




#another way to write 
def is_plindrome (name):
    return name == name[::-1]:
user_name = input("Enter a name in plindrome: ")
print(is_plindrome(user_name))


