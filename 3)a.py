dict ={}

def add_entry():
    word = input("Enter word ")
    meaning = input("Enter meaning")
    dict[word] = meaning
    print("Successfully added")
    print()

def search_word():
    word = input("Enter word to be searched ")
    if word in dict:
        print("word found")
    else:
        print("Not found")
    print()

def search_meaning():
    given_meaning = input("Enter meaning to be searched ")
    words_with_same_meaning =[]
    for word, meaning in dict.items():
        if given_meaning == meaning:
            words_with_same_meaning.append(word)
    print("words: ", words_with_same_meaning)
    print()

def remove_entry():
    word = input("Enter word to remove ")
    if word in dict:
        del dict[word]
        print("word removed")
    else:
        print("word Not found")
    print()

def display_sorted_words():
    sorted_dict = sorted(dict.keys())
    print(sorted_dict)

while True:
    print("\n--- Dictionary Menu ---")
    print("1. Add an entry")
    print("2. Search for a word")
    print("3. Search for a meaning")
    print("4. Remove an entry")
    print("5. Display all words sorted alphabetically")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_entry()
    elif choice == '2':
        search_word()
    elif choice == '3':
        search_meaning()
    elif choice == '4':
        remove_entry()
    elif choice == '5':
        display_sorted_words()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
