#making a mini contact book in python using dictionaries , search , update)
contact = {
}
def diary ():
    a=input("contact add/remove/search/changenumber/exit").strip().lower()
    if a=="add":
        new_name = input("enter name:").strip().lower()
        new_number=(input("enter number:"))
        contact.update({new_name:new_number})
        print(f"updated contact list:",contact)
    elif a=="remove":
        name= input("name:").strip().lower()
        if name in contact :
            contact.pop(name)
            print(f"updated contact list:",contact)
        else:
            print("name not found in contact")
    elif a=="search":
        name_search = input("name:").strip().lower()
        if name_search in contact:
            print(contact.get(name_search))
        else:
            print(f"no name found in as{name_search}")           
    elif a=="changenumber" :
        change_number = input("name  for changing number:").strip().lower()
        if change_number in contact:
            new_canged_number = input("new number:").strip()
            # contact.pop(change_number)#this is correct but lengthy 
            # contact.update({change_number:new_canged_number}) 
            contact[change_number] = new_canged_number
    elif a=="exit":
        
        return False
    else:
        print("input invalid")
        return True

while True:
    if not diary():
        break


    


