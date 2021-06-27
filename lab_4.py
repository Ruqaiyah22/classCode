#
# PRACTICE WITH FUNCTIONS, LOOPS, AND OPERATORS
#

# # HOW TO CREATE A FUNCTION
# STEP 1 - 7
'''def triangleArea(base, height) : # def == define, nameOfTheFunction + initiates a function + adds parameters
    area = (1/2)(base*height) # creating a variable + storing a value in it
    return area # returning the variable

print(triangleArea(3, 4)) # this argument returns 6, then prints
print(triangleArea(8, 11)) # this argument returns 11, then prints'''

# creating a dictionary
menuPrices = {
    "chicken sandwich": 4.99,
    "fries": 2.99,
    "juice": 1.99
}

# STEP 2 || create a function that adds two menu item prices


# what's the significance of including "Dict" + does it have to be that
def calcPrices(Dict, priceOfChickenSandwich, priceOfFries, priceOfJuice):
    sum = Dict[priceOfChickenSandwich] + Dict[priceOfFries]
    print("")
    print("Step 2 || printing the sum of two menu items")
    print(str(sum))
    print("")

    print("STRETCH || forming a sentence with the data")
    print("The total price of a " + priceOfChickenSandwich + " and "
          + priceOfFries + " is $" + str(sum))
    print("")

    print("STRETCH || searching for an unfound argument")
    unfoundArgument = "soda"  # defining the argument

    if unfoundArgument in menuPrices:
        print("We have found the key!\n")
    else:
        print("The key does not exist :/")
    print("")

    # STEP 3 || create a function to finds the difference between two menu items
    print("Step 3 || printing out the price difference between two menu items")
    # taking inputs and defining them
    priceOne = float(input("Enter the first price: "))
    priceTwo = float(input("Enter the second price: "))

    # finding the difference
    priceDifference = abs(priceOne - priceTwo)

    # print to console
    print(str(round(priceDifference, 2)))
    print("")

    print("STRETCH || forming a sentence with the data")
    print("The difference between the prices you have entered is " +
          str(round(priceDifference, 2)))
    print("")
    print("*******************************************************************")
    print("")


calcPrices(menuPrices, "chicken sandwich", "fries", "juice")

# STEP 4 || going back to the sneaker inventory dictionary
print("STEP 4 || taking one value and multiplying it by a number")
shoeCount = {
    "jordans": 1,
    "yeezy": 8,
    "foamposite": 10,
    "air max": 5,
    "sb dunk": 20,
}
print("This is the current inventory.")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# creating a function that would update one of the sneakers
multiplyPriceOfOne = {
    "yeezy": 24
}

# using python built in function to update the dictionary + print
shoeCount.update(multiplyPriceOfOne)
print("We got a new shipment of Yeezys. This is the updated inventory. ( Yeezy inventory multiplied by 3 )")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# multiplying each value in the dictionary
shoeCount.update((x, y*5) for x, y in shoeCount.items())
print("STRETCH || Another huge shipment, this is the updated inventory. ( Everything multiplied by 5 )")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# searching for unfound argument
print("STRETCH || searching for an unfound argument")
print("Search up a shoe and we'll let you know if it's available!")
sneakerSearch = input("Type the shoe name here: ")  # defining the argument
# making the user input all lowercase since it's case sensitive
sneakerSearch = sneakerSearch.lower()

if sneakerSearch not in shoeCount:
    print("")
    print("OH SHOOT! We don't have anymore " +
          sneakerSearch + " in stock :/\n")
else:
    print("")
    print("YAY! We have " + sneakerSearch + " in stock!")
    print("")
print("*******************************************************************")

# STEP 5 || dividing the inventory
print("This is the current inventory.")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# creating a function that would update one of the sneakers
dividingPriceOfOne = {
    "sb dunk": 20
}

# using python built in function to update the dictionary + print
shoeCount.update(dividingPriceOfOne)
print("Ppl buyin up the SB's. This is the updated inventory. ( SB Dunks are divided by 5 )")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# dividing each value in the dictionary
shoeCount.update((x, y//5) for x, y in shoeCount.items())
print("STRETCH || HUGE SALE! Everything must go! This is the updated inventory. ( Everything divided by 5 )")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# searching for unfound argument
print("STRETCH || searching for an unfound argument")
print("Search up a shoe and we'll let you know if it's available!")
sneakerSearch = input("Type the shoe name here: ")  # defining the argument
# making the user input all lowercase since it's case sensitive
sneakerSearch = sneakerSearch.lower()

if sneakerSearch not in shoeCount:
    print("")
    print("OH SHOOT! We don't have anymore " +
          sneakerSearch + " in stock :/\n")
else:
    print("")
    print("YAY! We have " + sneakerSearch + " in stock!")
    print("")

# come back?
'''# combining the two ( multiplying and dividing ) 
print("STRETCH || searching for an unfound argument")
if i < 10 :
    shoeCount.update((x, y*100) for x, y in shoeCount.items())
elif i > 20:
    shoeCount.update((x, y*10) for x, y in shoeCount.items())
else :
    shoeCount.update((x, y//2) for x, y in shoeCount.items())

for i in shoeCount :
    print(i, shoeCount[i])
print("")'''
print("*******************************************************************")
print("")

# STEP 6
print("STEP 6 || coming up with my own unique function")
print("")

# creating a dictionary
numOfTasks = {
    "Kaiyah": 8,
    "Kimon": 8,
    "Alaiah": 8,
    "Aairah": 0
}

# declaring variables
totalNumOfTasks = 24
evenTasks = totalNumOfTasks//4

print(
    "Heyyoo!\n \
    Kaiyah, Kimon, and Alaiah have a list of 24 tasks to do. They've\n \
    hired Aairah to help out. We need to evenly divide up the tasks to\n \
    figure out how many tasks each person should do."
)
print("")
signIn = input("Please enter your name to see how many tasks you have: ")

for signIn in numOfTasks: # hella cheated, need to figure out how to actually do this
    if signIn == "Aairah":
        numOfTasks.update((x, evenTasks) for x, y in numOfTasks.items())
        print("Thanks for signing in " + signIn + "! We've updated everyone's number of tasks!")
        print("Please sign out so others can see their updated number of tasks :)")
        print("")
        signOut = ("Please enter (y/n) to continue: ")
        if signOut == "y" :
            break
        else :
            print(":|")
            print("")
    else:
        print("")
        print("Hello! You have 8 tasks to do!")
        print("")
        break
        '''print("")
        print("Hmmm, doesn't look like you're in our system")
        print("")
        signIn = input(
            "Please re-enter your name to see how many tasks you have: ")'''
