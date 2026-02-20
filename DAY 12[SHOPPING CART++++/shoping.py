#making a list of products and their prices using dictionaries 
products={
    "rice": 100,
    "flour":50,
    "dal":60,
    "oil":100,
    "comb":20,
    "colgate":120,
    "besan":110,
    "millets":110,
    "biscuts":50,
    "soap":60,
    "bodywash":100,
    "facewash":300,
    "wheyprotien":2000,
}
#making my presonal bill , dictionary for my items 
cart={}
bill = 0  
#add/remove/final/exit items on cart 
def manage_cart():
    global bill #here we use global other wise pithon treat bill as a local variable
    a = input("add/remove/final/exit:").strip().lower()
    if a=="add":
        print("--------------------------------------------------------------------")
        print(products)
        print("--------------------------------------------------------------------")
        want= input("what you want:").strip().lower()
        if want in products:
            cart[want]=products[want]
            bill = bill + products[want]
            print(cart,bill)
        else:
            print("item is not present in mall")  
    elif a == "remove":
        print("-------------------------------------------------------------------")
        print(f"{cart} ")
        unwanted = input(" what you want to remove in this:").strip().lower()
        if unwanted in cart:
            cart.pop(unwanted)
            bill = bill - products[unwanted]
            print(cart,bill)
        else:
            print("this item already not in cart")
    elif a=="final":
        coupen_code = input("add coupen code:").strip().lower()
        if coupen_code=="save10" :
            print(f"you get a discount of 10 % on {bill} ")
            bill = bill - (bill/10)
            print(f"final bill = {bill}")
        else:
            print(f" finall bill is{bill} ")    
        exit()
    elif a=="exit":
        print("meet you next time :")
        exit()    

print("welcome to shopping mall")
#discount 2000 + shopping user get 10 % dicount 
while True :
    manage_cart()
    

    


        

        