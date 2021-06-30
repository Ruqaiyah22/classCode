# STEP 6
print("")
print("STEP 6 || coming up with my own unique function")
print("")

# STEP 6 || Live coding, below is a nested dictonary
jerseyNumbers = {
    1: {"name" : "Curry", "jerseyNum" : 30},
    2: {"name" : "Klay", "jerseyNum" : 11}, 
    3: {"name" : "Oubre", "jerseyNum" : 12},
    4: {"name" : "Draymond", "jerseyNum" : 23},
    5: {"name" : "Wiseman", "jerseyNum" : 33}
}

# creating a function to search through the values and print the jersey with the largest jersey number
''' suedo code:
    read the 1st jersey number
    compare to the 2nd jersey number
    if 1st > 2nd
    largest = 1st

    print largest jersey number
'''
# use for loop b/c wew know how many times we're going to compare // while loop is where you're uncertain about how many comparisons you're going to do
def largestJerseyNumber(jerseyNumbers) :
    largestJerseyNum = 0

    for x in range(1, 5) :
        if (jerseyNumbers[x]['jerseyNum'] > largestJerseyNum) :
            largestJerseyNum = jerseyNumbers[x]['jerseyNum']
            print(jerseyNumbers[x]['jerseyNum'])
        else :
            largestJerseyNum= jerseyNumbers[x+1]['jerseyNum']
            print(jerseyNumbers[x+1]['jerseyNum'])
    print(largestJerseyNum)

largestJerseyNumber(jerseyNumbers) # include the function call