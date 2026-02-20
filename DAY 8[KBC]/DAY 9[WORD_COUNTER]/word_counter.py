# Word Counter
# Use: .split(), dict
def counter(a):
    frequency   = {}
    b=a.split()
    print(" number of words: " , len(b))
    for word in b:  
        frequency[word]=frequency.get(word,0)+1

    print(frequency)    

word = input("write any sentense :") 
counter(word)



