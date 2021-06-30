#
# PRACTICE WITH FUNCTIONS, LOOPS, AND OPERATORS
#

# # HOW TO CREATE A FUNCTION
# STEP 1 - 7
def triangleArea(base, height) : # def == define, nameOfTheFunction + initiates a function + adds parameters
    area = 0.5*(base*height) # creating a variable + storing a value in it
    return area # returning the variable

print("")
print("This is the pregame example.")
print(triangleArea(3, 4)) # this argument returns 6, then prints
print(triangleArea(8, 11)) # this argument returns 11, then prints

# creating a dictionary
menuPrices = {
    "chicken sandwich": 4.99,
    "fries": 2.99,
    "juice": 1.99
}

# STEP 2 || create a function that adds two menu item prices
# what's the significance of including "Dict" + does it have to be that
# the significance^ 
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

    '''# STEP 2 || LIVE CODING IN CLASS ( unfinished code )
    food = {
        "milk" : 1.00,
        "cheese" : 1.99
    }
    total_price = input1 * input2

    goodToGo = True
    while (goodToGo) :
        input1 = input("pls give us a food: ")
        if (input1 in food) :
            print("thanks")
        else :
            goodToGo = False
        input2 = input("pls give us another food: ")
        if input2 in food :
            print("the total price is ", total_price(input1, input2))
        else:
            goodToGo = False'''

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