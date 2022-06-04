import string
import random


def split(string): 
	return [letter for letter in string]


digits=split(string.digits)+split(string.punctuation)+split(string.ascii_uppercase)+split(string.ascii_lowercase)

random.shuffle(digits)
number=int(input("enter number of password:"))
result="".join(map(str,digits[0:number-1]))
print (result)


