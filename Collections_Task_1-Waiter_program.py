print("Hello, what would you like to order? You may order three to five items from each menu")
choices = []

smenu = {1:"bread",2:"tomatoes",3:"cheese",4:"caviar",5:"mushrooms",6:"peppers"}
print("the starter menu is", smenu)
print("what starters would you like please give me the number")
schoice=1
while schoice == 1:
    a1 = int(input("what number your first item:"))
    if a1 in range(1,7):
        choices.append(smenu.get(int(a1)))
        schoice +=1
    else:
        print("That's not right, please repeat your number")
while schoice == 2:
    a2 = int(input("what number your second item:"))
    if a2 in range(1, 7):
        choices.append(smenu.get(int(a2)))
        schoice += 1
    else:
        print("That's not right, please repeat your number")
while schoice == 3:
    a3 = int(input("what number your third item:"))
    if a3 in range(1, 7):
        choices.append(smenu.get(int(a3)))
        schoice += 1
    else:
        print("That's not right, please repeat your number")

print("would you like to order another starter ")
if input("(y/n):") == "y":
    while schoice == 4:
        x1 = int(input("what number your fourth item:"))
        if x1 in range(1, 7):
            choices.append(smenu.get(int(x1)))
            schoice += 1
        else:
            print("That's not right, please repeat your number")

    print("would you like to order another starter ")
    if input("(y/n):") == "y":
        while schoice == 5:
            x2 = int(input("what number your fifth item:"))
            if x2 in range(1, 7):
                choices.append(smenu.get(int(x2)))
                schoice += 1
            else:
                print("That's not right, please repeat your number")


mmenu = {1:"pizza",2:"spaghetti",3:"lamb roast",4:"mixed grill",5:"bean soup",6:"stuffed aubergine"}
print("the main menu is",mmenu)
print("what main would you like please give me the number")
mchoice=1
while mchoice == 1:
    b1 = int(input("what number your first item:"))
    if b1 in range(1,7):
        choices.append(mmenu.get(int(b1)))
        mchoice +=1
    else:
        print("That's not right, please repeat your number")
while mchoice == 2:
    b2 = int(input("what number your second item:"))
    if b2 in range(1, 7):
        choices.append(mmenu.get(int(b2)))
        mchoice += 1
    else:
        print("That's not right, please repeat your number")
while mchoice == 3:
    b3 = int(input("what number your third item:"))
    if b3 in range(1, 7):
        choices.append(mmenu.get(int(b3)))
        mchoice += 1
    else:
        print("That's not right, please repeat your number")

print("would you like to order another main ")
if input("(y/n):") == "y":
    while mchoice == 4:
        x1 = int(input("what number your fourth item:"))
        if x1 in range(1, 7):
            choices.append(mmenu.get(int(x1)))
            mchoice += 1
        else:
            print("That's not right, please repeat your number")

    print("would you like to order another main ")
    if input("(y/n):") == "y":
        while mchoice == 5:
            x2 = int(input("what number your fifth item:"))
            if x2 in range(1, 7):
                choices.append(mmenu.get(int(x2)))
                mchoice += 1
            else:
                print("That's not right, please repeat your number")

dmenu = {1:"ice cream",2:"cake",3:"apple pie",4:"cheesecake",5:"crumble",6:"brownie"}
print("the dessert menu is",dmenu)
print("what dessert would you like please give me the number")
dchoice=1
while dchoice == 1:
    c1 = int(input("what number your first item:"))
    if c1 in range(1,7):
        choices.append(dmenu.get(int(c1)))
        dchoice +=1
    else:
        print("That's not right, please repeat your number")
while dchoice == 2:
    c2 = int(input("what number your second item:"))
    if c2 in range(1, 7):
        choices.append(dmenu.get(int(c2)))
        dchoice += 1
    else:
        print("That's not right, please repeat your number")
while dchoice == 3:
    c3 = int(input("what number your third item:"))
    if c3 in range(1, 7):
        choices.append(dmenu.get(int(c3)))
        dchoice += 1
    else:
        print("That's not right, please repeat your number")

print("would you like to order another dessert ")
if input("(y/n):") == "y":
    while dchoice == 4:
        x1 = int(input("what number your fourth item:"))
        if x1 in range(1, 7):
            choices.append(dmenu.get(int(x1)))
            dchoice += 1
        else:
            print("That's not right, please repeat your number")

    print("would you like to order another dessert ")
    if input("(y/n):") == "y":
        while dchoice == 5:
            x2 = int(input("what number your fifth item:"))
            if x2 in range(1, 7):
                choices.append(dmenu.get(int(x2)))
                dchoice += 1
            else:
                print("That's not right, please repeat your number")

print("would you like to order up to five drinks?")
drchoice = 0
cdrinks = []
while drchoice < 5:
    if input("(y/n):") == "y":
        drinks = {1:"wine",2:"beer",3:"juice",4:"tea",5:"coffee",6:"mojito"}
        print(drinks)
        x1 = int(input("what is your drink choice:"))
        if x1 in range(1, 7):
            cdrinks.append(drinks.get(int(x1)))
            drchoice += 1
        else:
            print("That's not right, please repeat your number")
        if drchoice != 5:
            print("would you like to order another drink ")



print("thank you for your order so we have:", choices)
print("I will bring you the following drinks:", cdrinks)
