data = ""
with open("data.txt", 'r') as myfile:
    data = myfile.read()
print(data)
with open("data.txt", 'a') as myfile:
    for i in range(2):
        myfile.write(data)