while True:
    letter = input("Enter a letter (а,б,в,г,д,е,ж,з,и,к) or enter 0 to exit: ")

    if letter == "0":
        print("Goodbye!")
        break
    elif letter == "а":
        for i in range(5):
            for j in range(5):
                if j >= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "б":
        for i in range(5):
            for j in range(5):
                if j <= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "в":
        for i in range(5):
            for j in range(5):
                if i <= j <= 4 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "г":
        for i in range(5):
            for j in range(5):
                if 4 - i <= j <= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "д":
        for i in range(5):
            for j in range(5):
                if 4 - i <= j <= i or i <= j <= 4 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "е":
        for i in range(5):
            for j in range(5):
                if j <= i <= 4 - j or 4 - j <= i <= j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "ж":
        for i in range(5):
            for j in range(5):
                if j <= i <= 4 - j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "з":
        for i in range(5):
            for j in range(5):
                if 4 - j <= i <= j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "и":
        for i in range(5):
            for j in range(5):
                if j <= 4 - i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif letter == "к":
        for i in range(5):
            for j in range(5):
                if 4 - j <= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else:
        print("Error")