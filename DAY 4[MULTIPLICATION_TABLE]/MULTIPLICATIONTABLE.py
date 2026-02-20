#making a multiplication tyable using loops and string formatting
print("give me a number you want to find table of ")
num = int(input("number:"))
for i in range(11):
    print(f"{num}x{i}=",num*i)
