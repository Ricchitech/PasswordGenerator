import string
import random

if __name__ == '__main__':
    s1=string.ascii_lowercase   #lowercase letters [a-z]
    s2=string.ascii_uppercase   #uppercase letters [A-Z]
    s3=string.digits            #1-9
    s4=string.punctuation       #lowercase letters Special Characters
    plen=int(input("Enter Password length \n"))
    s=[]
    #merging 
    s.extend(list(s1))  
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s) #shuffling the list
    print("".join(s[0:plen])) #method join random password to a ""