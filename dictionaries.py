# Dictionaries

# Dictionaries use key/value pairs

# key = a reference to a particular object
# value = data storage mechanism you want to use

# Create a dictionary

student_1 = {
    "name": "Susan",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables","data_types","setup"]
}
#Access data within a dictionary
print(student_1["stream"])
# how to access a particular part of a list in a dictionary
print(student_1["completed_lesson_names"][1])
#changing a value in a dictionary
student_1["completed_lessons"]=3
print(student_1["completed_lessons"])
#removing items from our dictionary
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])
#dictionary methods
print(student_1.keys())
# dictionary methods
#keys
print(student_1.keys())
print(student_1.get("name"))
# get the values
print(student_1.values())
#outputs array of tuples with key value pairs in dictionary
print(student_1.items())