# tech201_collections
# tech201_collections
## Lists
### Intoduction

In most other languages Lists are referred to as Arrays, this can lead to confusion when reading documentation and is worth bearing in mind.

Firstly to explain this topic, let's make a simple list:

`shopping_list = ["milk", "Eggs", "Bread", "fruit"]`

We can see with the following code that python recognises it as being list type:

`print(type(shopping_list))`

If we want to get individual data from the list we can use square brackets, remembering that we always count up from 0 but down from -1.

 `print(shopping_list[0]) # milk`

 `print(shopping_list[3]) # fruit`

 `print(shopping_list[-1]) # fruit`
 
We can change individual data in a similar way, by selecting the position and making it equal to new data.

 `shopping_list[0] = "suger"`


### List methods

 To add to a list we can use the .append() method on our chosen list. This will add the new data to the end of the list.

 `shopping_list.append("vegetables")`

 Printing individual items can be done with square brackets
 
 `print(shopping_list[4]) #vegetables`

 We can find the length of the list, which may be useful for many purposes with the len function just like we would in a string.

 `print(len(shopping_list))`

 To remove an item from a list, we can use the .remove function.

 `shopping_list.remove("Bread")`

 remove last item of list , without specificity. This will just remove the last item.

 `shopping_list.pop()`

## Mixed data type lists
 Here is a list of mixed data types:

 `mixture = [1 , 2, 3.5, "one", "two", "three"]`

 Lists of mixed data types will also work in a similar way

 `print(mixture)` #[1, 2, 3.5, 'one', 'two', 'three']

 `print(mixture[1:3])` #[2, 3.5]

 `print(mixture[-2::])` #['two', 'three']

 `print(mixture[-2:])` #['two', 'three']

 `print(mixture[::2])` #[1, 3.5, 'two']

## Tuples

 Exactly the same as lists , except they are immutable.
 tuples are useful for elements that should not be changed.
 Let's start with a basic tuple, using () to make our tuple.

 `essentials = ("bread", "eggs", "milk")` 

 `print(essentials)` #('bread', 'eggs', 'milk')

 Here we can use the count method to return the number of times something is in the tuple:
 
 `print(essentials.count("bread"))` #1

 The following code results in an error as the tuple is immutable:

 essentials[1] = "beans"
 
## Sets and Frozen sets

 Lists and sets are very similar, however sets will have a random placement when they are formed.

### Create a set
 To demonstrate this, let's create a set

 `car_parts = {"wheels","doors","exhausts"}`

 We can see that our set has a random placement.

 `print(car_parts)` #{'doors', 'wheels', 'exhausts'}

 To remove things from a set we can use the discard method.

 `car_parts.discard("doors")`

 `print(car_parts)` #{'wheels', 'exhausts'}

 To add things to a set we can use the add method

 `car_parts.add("windows")`

 `print(car_parts)` #{'wheels', 'exhausts', 'windows'}

### Frozen sets

 frozen sets are immutable versions of a set. still unordered and un indexed.

 `x = frozenset([1,2,3,4,"Five"])`

 `print(x)` #frozenset({1, 2, 3, 4, 'Five'})
 
## Dictionaries

 Dictionaries use key/value pairs

 key = a reference to a particular object
 value = data storage mechanism you want to use

### Create a dictionary
First let's create a simple dictionary, note lists can also be stored within a dictionary:

`student_1 = {
    "name": "Susan",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables","data_types","setup"]
}`

### Access data within a dictionary

`print(student_1["stream"])`

 how to access a particular part of a list in a dictionary
`print(student_1["completed_lesson_names"][1])`

changing a value in a dictionary

`student_1["completed_lessons"]=3`

`print(student_1["completed_lessons"])` #3

removing items from our dictionary

`student_1["completed_lesson_names"].remove("data_types")`

`print(student_1["completed_lesson_names"]`)` #['variables', 'setup']

### Dictionary methods

`print(student_1.keys())`



### Get the keys
If we don't know what our keys are or need to return all of our keys, we can print this using the keys method.
`print(student_1.keys())`
If we want to return one value associated with a key we can use the get method and select a key.
`print(student_1.get("name"))`

### Get the values



`print(student_1.values())`

outputs array of tuples with key value pairs in dictionary

`print(student_1.items())`