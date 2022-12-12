import os

def splitter(filename):
    file = open(f"{os.getcwd()}//{filename}")

    data = file.read().split()

    exception = ("Mr.", "Ms.", "Dr.", "i.e.")
    mark = (".", "?", "!")

    for word in data:
        print(word, end=" ")
        if word[-1] in mark:
            if word in exception:
                continue

            print()

    print()
            

    print(data)