# in this code i am going to make a password strength checker using len(),isdigit()
# ,isalpha()
password = input("write the password:")
#password com=ntain minimum 8 character
#atleset 1digit , 1 numeric , and 1 special character 
#  (if else)
if len(password)<=8:
    print("make a new password whose minimum lengt is 8 ")
elif password.isdigit():
    print("give atleast 1 alphabet")
elif password.isalpha():
    print("give at least 1 numeric value") 
elif password.isalnum():
    print("give atleast 1 special character ")
else:
    print("you create a strong password ")






