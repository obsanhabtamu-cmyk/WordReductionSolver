Seat = r"CleanedDictionary.txt"

with open(Seat) as seat:
    Reader = [w.strip() for w in seat.read().split()]

Dictionary = set(Reader) 

valid_words = []

for Current_Word in Dictionary:
    Placeholder1 = True
    for i in range(len(Current_Word)):
        reduced = Current_Word[:i] + Current_Word[i+1:]
        
        if reduced not in Dictionary:
            Placeholder1 = False
            break

    if Placeholder1 == True:
        valid_words.append(Current_Word)

sorted_word = sorted(valid_words, key=len, reverse=True)

with open("reducible_words.txt","w") as file1:
    for file in sorted_word:
        file1.write(file + '\n')


