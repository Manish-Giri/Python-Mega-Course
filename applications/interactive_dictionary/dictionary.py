import os, json
from difflib import get_close_matches


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
        # calculate ratio
        matches = get_close_matches(word, data.keys())
        if len(matches) > 0:
            response = input(f"Did you mean {matches[0]}? (Y/N) > ")
            if response.lower() == 'y':
                return data[matches[0]]
            else:
                return "Bye"
        else:
            return "That word does not exist. Please try again."


def run():
    inp = input("Enter a word (Enter 'end' to quit): \n")
    while inp != "end":
        result = transform(inp)
        # check for return type
        # list if match found
        if type(result) == list:
            if len(result) > 1:
                print("Possible meanings: ")
                for idx, val in enumerate(result):
                    print(f"{idx + 1}.", val)
            else:
                print("".join(result))
        else:
            print(result)
        # print(result)
        inp = input("Enter a word (Enter 'end' to quit): \n")
    else:
        print("Thank You for playing!")


run()
