story1 = {
    "start":"a disaster has struck metropolis, a giant tsunami has flooded the city hundreds are drowning!",
    "middle":"Hey look whats that, is it a bird , is it a plane ?",
    "end":"No its Captain Birdseye ! He's pulling them out with his fish fingers !"
}
print(story1.items())
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1.get("start"))
print(story1.get("middle"))
print(story1.get("start"))
story1["hero"] = "Captain Birdseye"
