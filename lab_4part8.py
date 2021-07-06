# STEP 8 || Create a dictionary of cities
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

# STEP 9 || Create a function that prints the name of every city in the dictionary
print("")
print("STEP 9 || Printing out all the cities")
print("")
#print(cities, sep = "\n")
#print str(cities)[1:-1] 
print("")

# print(len(cities)) prints 10

# STRETCH || Only printing the names whose name is longer than the city that comes before it
print("STRETCH || Only printing the names whose name is longer than the city that comes before it")

def longestWordCount(cities) :
    longestWord = 0

    for x in cities :
        if (len(cities[x]) > longestWord) :
            longestWord = cities[x]
            print(cities[x])
        else :
            longestWord = cities[x+1]
            print(cities[x+1])
    print(longestWord)
longestWordCount(cities)



