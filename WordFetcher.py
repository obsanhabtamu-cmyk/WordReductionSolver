import re
import gzip
seen = set() # prevent duplicate
words = []
# set the amount of word you want to fetch for example if you add 100 it will get you 100 word from the file.gz
word_amount = 1000000 
file = r"File.gz"

finished = 0

def clean_line(line: str) -> str:
    if not isinstance(line, str):
        return ""  # safeguard against non-string input

    # Remove Some metadata listed
    line = re.sub(
        r'"?(glosses|senses|examples|entries|meaning)"?\s*:?',
        '',
        line
    )
    # Remove braces and commas 
    line = re.sub(r'[{},]', '', line)
    # Keep only letters and spaces
    line = re.sub(r'[^a-zA-Z\s]', '', line)
    return line

# there is error ignore so you should ignore it too
with gzip.open(file, "rt", encoding="utf-8", errors="ignore") as f:
    for line in f:
        cleaned_line = clean_line(line)
        line_words = cleaned_line.lower().split()

        for word in line_words:
            if word not in seen:
                seen.add(word)

                # why 6 to 7 letter length cuz 7 is for plausible and 6 is when we remove the word we check against
                if len(word) in (6, 7):
                    words.append(word)
                    # stops once you hit the word limit you set
                    if len(words) >= word_amount:
                        break
        if len(words) >= word_amount:
            break

# Save results into our word.txt file
with open("word.txt", "w", encoding="utf-8") as out_file:
    for word in words:
        out_file.write(word + "\n")
        finished += 1

        percentage = finished / word_amount * 100
        bar_length = 30
        filled = int(bar_length * finished / word_amount)
    
        bar = "█" * filled + "-" * (bar_length - filled)
    
        print(f"\r[{bar}] {percentage:.0f}%", end="", flush=True)
    
print()

print(f"The file 'word.txt' with {word_amount} words of length 6 to 7 is created now.")