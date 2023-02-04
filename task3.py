_string = input("Enter: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if i not in _string.lower():
        print(False)
        quit()
print(True)
