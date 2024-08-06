initial = 'Clear_content.txt'
line = 'with open(initial, "w") as file:'
content = 'file.write("This is the latest fresh data")'
with open(initial, "w") as file:
    pass
exec(line+content)
print(f"Sucess: ")



