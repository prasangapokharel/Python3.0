path ='ram.txt'
with open(path, "r") as file:
    content= file.readlines()
    print(f"Your content is {content}")  