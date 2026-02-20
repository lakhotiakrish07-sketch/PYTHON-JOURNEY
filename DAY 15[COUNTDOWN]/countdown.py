# to day i learn time module and make a countdown timer 
import time 

t = int(input("countdown time:"))
for i in range(t , 0, -1):
    print(i)
    time.sleep(1)

print("go!")