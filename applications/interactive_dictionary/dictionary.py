import os, json


def load_data():
    data = json.load(open("data.json"))
    # print(len(data))
    # print(data["hunger"])
    return data


def transform(w):
    word = w.lower()
    data = load_data()
    if word in data:
        return data[word]
    else:
        print("That word does not exist. Please try again.\n")
        return None


def run():
    inp = input("Enter a word (Enter 'end' to quit): \n")
    while inp != "end":
        result = transform(inp)
        if len(result) > 1:
            for idx, val in enumerate(result):
                print(f"{idx + 1}.", val)
        else:
            print("".join(result))

        # print(result)
        inp = input("Enter a word (Enter 'end' to quit): \n")


run()
