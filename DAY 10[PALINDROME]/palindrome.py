#making a palindrome checker 
char  = input("any character :").strip().lower()
list1  = list(char)
# print(list1)
# ['k', 'r', 'i', 's', 'h']
#using for loop and if else statements 
for i in range(int(len(list1)/2)):
    
    if list1[i]!=list1[-(i +1)]:
        print(f"{char } is not a palindrome")
        break
    else:
        print("this is a palindrome")    
          