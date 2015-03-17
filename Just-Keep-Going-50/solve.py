from base64 import b64decode

def rot13(text):
    string_list = []
    for c in text:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            c = chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
        elif ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
        string_list.append(c)
    return "".join(string_list)

f = open("persevere.txt")
encrypted = f.read()

temp = encrypted
while True:
    temp = rot13(temp)
    temp = b64decode(temp)
    print temp
