f = open("note.txt")
text = f.read().strip()

freq = {}
for c in text:
    if freq.has_key(c):
        freq[c] += 1
    else:
        freq[c] = 1
print freq
