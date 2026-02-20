record={}
def notepad(): 
    a = int(input("what do you want 1.recordbook , 2.add_record , 3.remove_record , 4.exit"))
    if a==2:
        roll= int(input("rollnumber:"))
        name = input("name:")
        record.update({roll:name})
        record_file = str(record)
        file = open("recordbook.txt",'w')
        file.write(record_file)
        file.close()
    elif a==1:
        file = open("recordbook.txt",'r')
        data =file.read()
        print(data)
        file.close()
    elif a==3:
        roll= int(input("rollnumber:"))
        if roll in record:
            record.pop(roll)
            record_file = str(record)
            file = open("recordbook.txt",'w')#if i use a insteed of w then it can add what we want to remove 
            file.write(record_file)
            file.close()
        else:
            print("record not found!")
    elif a==4:
        return False          
    else:
        print("invalid output!")  
        return True 


while True:
    notepad()         

