import os
from pathlib import Path

# Uses the script location so the file works on other computers
Seat = Path(__file__).parent / "2of12inf.txt"

def merge_files(folder, output_path): #Function that merges all text files in a folder into one text file.
    merged = []

    for filename in os.listdir(folder): #Iterates through all files in the specified folder and checks if they are text files. If they are, it reads their contents and appends them to a list.
        if filename.endswith(".txt"):
            with open(os.path.join(folder, filename), "r") as f:
                merged.append(f.read())

    with open(output_path, "w") as out:
        out.write("\n".join(merged))

# Merge text files from the folder into one output file
folder = Path(__file__).parent / "MergedTxtFiles"

merge_files(folder, Path(__file__).parent / "merged_output.txt")
# Uses the script location so the program works on other computers

with open(Seat) as seat:
    Reader = [w.strip() for w in seat.read().split()]

Dictionary = set(Reader)
Counter = 0
for words in Dictionary:
    Counter += 1
print(Counter) #Prints the number of words in the dictionary to the console.

for Current_Word in Dictionary: #Loop that iterates through the dictionary and checks if the word can be reduced by one letter and still be in the dictionary.
    Active = True
    for i in range(len(Current_Word)):  #Goes over each index position in the current word.
        reduced = Current_Word[:i] + Current_Word[i+1:] #Loop that iterates through the letters of the current word and creates a new word with one letter removed.
        if reduced not in Dictionary:
            Active = False
            break

    if Active == True:
        open("reducible_words.txt", "a").write(Current_Word + "\n")  #Writes the current word to a new file if it can be reduced by one letter and still be in the dictionary.
