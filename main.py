import baconator
import proverb 
import html
from os import system, name 

def strip_tags(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out

system('cls') 

name = baconator.generate(delimiter=' ', token_len=0) 
print("Hello, your Hollywood generated name is: " + name)
print() 

print("Your proverb today, " + name + ", is ... ")
print(strip_tags(proverb.saying()))
print()

input("Press any key to continue.")

