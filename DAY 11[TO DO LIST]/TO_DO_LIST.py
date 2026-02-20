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
#makind a add or remove function for user 
def manage_cart():
    a = input("add/remove/exit:").lower().strip()
    if a =="add":
        print(products) 
        n = input("what you want to add:") 
        if n == products.keys():
            cart.update(products.keys(n),products.values(n)) 
            bill = bill + products.values(n)
        else:
            return False    
    elif a=="remove":
        print("what you wnat to remove----------------------------------------------")    
        print(products)
        if n == cart.keys(n):
            bill = bill - cart.value(n)
        else:    
            return False
    elif a=="exit":
        print("thanks for shopping ") 
        print(f"your total bill is{bill}")   

while True:
    manage_cart()




