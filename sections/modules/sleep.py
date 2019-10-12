import time
with open("sleep_demo.txt", "w") as file:
    for i in range(30):
        file.write(f"{str(i)}\n")
        time.sleep(3)