# f = open("bear.txt")
# print(f.read())

with open("fruits.txt", "w") as myfile:
    for i in range(10):
        myfile.write(f"{str(i)}\n")
print("Done")