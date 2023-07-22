def countWords(text):
    words =[]

    for line in text:
        words.extend(line.split())
    
    longest = max(words, key=len)
    smallest = min(words, key=len)

    return longest, smallest


def create_file():
    name = input("enter file name ")
    with open(name,'w') as file:
        lines =[]
        for _ in range(6):
            print(f"Enter line {_+1}")
            line = input()
            lines.append(line)
        file.write("\n".join(lines))

    return lines

lines = create_file()
longest,shortest = countWords(lines)

print(f"shortest word {shortest}")
print(f"length of shortest word {len(shortest)}")
print(f"longest word {longest}")
print(f"length of longest word {len(longest)}")
