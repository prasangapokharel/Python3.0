path = 'dwsample1-bin.bin'
with open(path, "rb") as file:
    content = file.read()
    print(f"Your contetn is {content}")