import re

def findAll(text):
    vowels = len(re.findall(r'[aeiouAEIOU]',text))
    digits = len(re.findall(r'\d',text))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVXYZ]', text))

    return vowels,consonants,digits


text = "Hello everyone! Have a great day 007"
print("Text is ",text)
vowels,consonants,digits = findAll(text)
print(f"Total num of \vowels are {vowels}\nconsonants are {consonants}\ndigits are {digits}")