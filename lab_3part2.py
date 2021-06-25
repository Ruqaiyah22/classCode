#
# PRACTICE WITH LISTS
#

print("")
# STEP 2 || Create a list with the city names provided
cities = [
    "Oakland",
    "Atlanta", 
    "New York City", 
    "Seattle", 
    "Memphis", 
    "Miami", 
    "Boston", 
    "Los Angeles", 
    "Denver", 
    "New Orleans"
]
print(*cities, sep = "\n")
print("")

# STEP 3 || Create a new python list with 10 elements 
colors = [
    "blue",
    "purple",
    "red",
    "gold",
    "brown",
    "silver",
    "orange",
    "yellow",
    "white",
    "gray"
]
print(*colors, sep = "\n")
print("")

# STEP 3..CONTINUED || Pick 3 values from the list and print it
print("Printing from the cities list")
print(cities[0], sep = "\n")
print(cities[1], sep = "\n")
print(cities[-3], sep = "\n")
print("")
print("Printing from the color list")
print(colors[0], sep = "\n")
print(colors[4], sep = "\n")
print(colors[-1], sep = "\n")
print("")

# STEP 4 || Use list slicing to create a new list of 4 items from both lists
print("List slicing for the cities list")
firstFourCities = cities[0:4]
print(firstFourCities)
print("")
print("List slicing for the color list")
firstFourColors = colors[0:4]
print(firstFourColors)
print("")

# STEP 5 || Update the data in the cities list
print("Updating the city names")
cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[-3] = "Hollywood"
cities[-5] = "Tampa"
print(cities)
print("")

# STEP 6 || Add the cities back to the list with append(), extend(), and insert()
print("Adding Oakland to the end of the list")
cities.append("Oakland")
print(cities)
print("")

print("Creating a new list and adding the list to the existing list")
twoCities = [
    "New York", 
    "Los Angeles"
]
cities.extend(twoCities)
print(cities)
print("")

print("Inserting Miami back as the very first element in the list")
cities.insert(0, "Miami")
print(cities)
print("")

# STEP 7 || Removing 3 cities with pop(), clear(), and remove()
print("Removing Denver from the list with the del keyword")
del cities[-5]
print(cities)
print("")

print("Removing Seattle from the list with the pop() function")
cities.pop(4) 
print(cities)
print("")

print("Removing Boston from the list with the remove() function")
cities.remove("Boston")
print(cities)
print("")

print("Clearing the list with the clear() function")
cities.clear()
print(cities)