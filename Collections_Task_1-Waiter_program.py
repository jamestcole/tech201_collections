print("Hello, what would you like to order? You may order three to five items from each menu")
choices = []

smenu = {1:"bread",2:"tomatoes",3:"cheese",4:"caviar",5:"mushrooms",6:"peppers"}
print("the starter menu is", smenu)
print("what starters would you like please give me the number")
a1 = input("what number your first item:")
choices.append(smenu.get(int(a1)))
a2 = input("what number your second item:")
choices.append(smenu.get(int(a2)))
a3 = input("what number your third item:")
choices.append(smenu.get(int(a3)))
print("would you like to order another starter ")
if input("(y/n):") == "y":
    x1 = input("what number your fourth item:")
    choices.append(smenu.get(int(x1)))
    print("would you like to order another starter ")
    if input("(y/n):") == "y":
        x2 = input("what number your fifth item:")
        choices.append(smenu.get(int(x2)))


mmenu = {1:"pizza",2:"spaghetti",3:"lamb roast",4:"mixed grill",5:"bean soup",6:"stuffed aubergine"}
print("the main menu is",mmenu)
print("what main would you like please give me the number")
b1 = input("what number your first item:")
choices.append(mmenu.get(int(b1)))
b2 = input("what number your second item:")
choices.append(mmenu.get(int(b2)))
b3 = input("what number your third item:")
choices.append(mmenu.get(int(b3)))
print("would you like to order another main ")
if input("(y/n):") == "y":
    x1 = input("what number your fourth item:")
    choices.append(mmenu.get(int(x1)))
    print("would you like to order another starter ")
    if input("(y/n):") == "y":
        x2 = input("what number your fifth item:")
        choices.append(mmenu.get(int(x2)))

dmenu = {1:"ice cream",2:"cake",3:"apple pie",4:"cheesecake",5:"crumble",6:"brownie"}
print("the dessert menu is",dmenu)
print("what dessert would you like please give me the number")
b1 = input("what number your first item:")
choices.append(dmenu.get(int(b1)))
b2 = input("what number your second item:")
choices.append(dmenu.get(int(b2)))
b3 = input("what number your third item:")
choices.append(dmenu.get(int(b3)))
print("would you like to order another desert ")
if input("(y/n):") == "y":
    x1 = input("what number your fourth item:")
    choices.append(dmenu.get(int(x1)))
    print("would you like to order another desert ")
    if input("(y/n):") == "y":
        x2 = input("what number your fifth item:")
        choices.append(dmenu.get(int(x2)))

print("would you like to order up to five drinks?")
cdrinks = []
if input("(y/n):") == "y":
    drinks = {1:"wine",2:"beer",3:"juice",4:"tea",5:"coffee",6:"mojito"}
    print(drinks)
    x1 = input("what is your first drink:")
    cdrinks.append(drinks.get(int(x1)))
    print("would you like to order another drink ")
    if input("(y/n):") == "y":
        x2 = input("what number your fifth item:")
        cdrinks.append(drinks.get(int(x2)))
        print("would you like to order another drink ")
        if input("(y/n):") == "y":
            x3 = input("what number your fifth item:")
            cdrinks.append(drinks.get(int(x3)))
            print("would you like to order another drink ")
            if input("(y/n):") == "y":
                x4 = input("what number your fifth item:")
                cdrinks.append(drinks.get(int(x4)))
                print("would you like to order another drink ")
                if input("(y/n):") == "y":
                    x5 = input("what number your fifth item:")
                    cdrinks.append(drinks.get(int(x5)))

print("thank you for your order so we have:", choices)
print("I will bring you the following drinks:", cdrinks)
