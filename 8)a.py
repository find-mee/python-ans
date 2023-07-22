def count_characters(text):
    up = 0
    low =0
    num =0
    
    for word in text:
        if word.isupper():
            up+=1
        if word.islower():
            low+=1
        if word.isdigit():
            num+=1
    return up,low,num

def create_file():
    file_name = input("Enter file name ")
    with open(file_name,'w') as file:
        lines=[]
        for _ in range(6):
            print(f"Enter line {_+1}")
            line = input()
            lines.append(line)
        file.write("/n".join(lines))
    return lines

lines = create_file()
text = '\n'.join(lines)

upper_count, lower_count, digit_count = count_characters(text)

print("File Details:")
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
print(f"Number of digits: {digit_count}")