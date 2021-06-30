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
    "yeezy": 8*3
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
print("")

# STEP 5 || dividing the inventory
print("This is the current inventory.")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

# creating a function that would update one of the sneakers
dividingPriceOfOne = {
    "sb dunk": 100/5
}

# using python built in function to update the dictionary + print
shoeCount.update(dividingPriceOfOne)
print("Ppl buyin up the SB's. This is the updated inventory. ( SB Dunks are divided by 5 )")
for i in shoeCount:
    print(i, shoeCount[i])
print("")

'''# LIVE CODING^ for Step 5 doesn't work w/ my code 
print("Ppl buyin up the SB's. This is the updated inventory. ( SB Dunks are divided by 5 )")
def clearanceSale(shoeName, updater) :
    return (shoeCount[shoeName]/updater)
print("The new inventory of the SB dunk is " + str(clearanceSale("sb dunk", 5)))
for i in shoeCount:
    print(i, shoeCount[i])
print("")
# end of live coding'''

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
sneakerSearch = sneakerSearch.lower() # making the user input all lowercase since it's case sensitive

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