path = 'Prasanga.txt'
with open(path, "a") as file:
    content = file.write("\nThis will be added at last of file \nThis is third")
    print (f"Your content is {content}")