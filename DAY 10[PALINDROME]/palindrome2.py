#palindrome using reverse the strings 
char  = input("write the character:").lower().strip()
char2 = char[::-1]    
if char == char2:
    print(f"{char} is the palindrome ")
else:
    print(f"{char} is not the palindrome ") 
