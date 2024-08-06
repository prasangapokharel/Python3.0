initial = 'Prasanga.txt'
destination = 'ram.txt'

with open(initial, "r") as file:
    copy = file.read()
    with open(destination, "w") as file:
        paste = file.write(copy)
        print(f"Sucessfully pasted as destination\n {paste}")