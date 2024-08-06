path = 'Prasanga.txt'
with open(path, "r") as file:
    content = file.readline()
    print(f"Your contetn is {content}")