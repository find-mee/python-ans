def newList(lists):
    result =[]
    for list in lists:
        n = len(list)
        result.append((list,n))
    result.sort(key = lambda x : x[1])
    return result

lists = ["hello","Im a","string","nice to","meet you"]
result = newList(lists)
print(result)