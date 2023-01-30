# Lists

# Lists == Arrays

# here's our first list
#shopping_list = ["milk", "Eggs", "Bread", "fruit"]

# print(type(shopping_list))
# print(shopping_list[0]) # milk
# print(shopping_list[3]) # fruit
# print(shopping_list[-1]) # fruit
#
# shopping_list[0] = "suger"
# print(shopping_list)

#List methods

# add to a list
# shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[4])
# print(len(shopping_list))
#
# #remove from a list
#
# shopping_list.remove("Bread")
# print(len(shopping_list))
# print(shopping_list)
#
# # remove last item of list , without specificity
#
# shopping_list.pop()
# print(shopping_list)

# Mixed data type lists

# mixture = [1 , 2, 3.5, "one", "two", "three"]
#
# print(mixture)
#
# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[-2:])
# print(mixture[::2])

# Tuples

# Exactly the same as lists , except they are immutable
# tuples are useful for elements that should not be changed

essentials = ("bread", "eggs", "milk")

print(essentials)
print(essentials.count("bread"))

essentials[1] = "beans"