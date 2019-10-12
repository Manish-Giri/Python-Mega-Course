content = []
with open("bear.txt", "r") as myfile:
    data = myfile.read()
    content = data[:91]

print(content)
print(len(content))   

with open("first.txt", "w") as myfile:
    myfile.write(content)
    