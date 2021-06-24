# Step 2 create a dictionary from given table
groceryList = {
    "Chicken":"$1.59", 
    "Beef":"$1.99", 
    "Cheese":"$1.00", 
    "Milk":"$2.50"
}

# Step 3 create a new variable with a dictionary
fruitColors = {
    "grapes":"purple", 
    "grape fruit":"pink", 
    "strawberries":"red", 
    "lemons":"yellow"
}

lemonColor = fruitColors["lemons"]

# Step 4 store prices in a variables and print from Step 2
priceOfChicken = groceryList["Chicken"]
print ("The price of chicken is " + priceOfChicken + ".")
priceOfBeef = groceryList["Beef"]
print ("The price of beef is " + priceOfBeef + ".")
priceOfCheese = groceryList["Cheese"]
print ("The price of cheese is " + priceOfCheese + ".")
priceOfMilk = groceryList["Milk"]
print ("The price of milk is " + priceOfMilk + ".")
print("")

# Step 5 do the same^ but with the new dictionary
colorOfGrapes = fruitColors["grapes"]
print ("The color of a grape is " + colorOfGrapes + ".")
colorOfGrapeFruits = fruitColors["grape fruit"]
print ("The color of a grape fruit is " + colorOfGrapeFruits + ".")
colorOfStrawberries = fruitColors["strawberries"]
print ("The color of a strawberry is " + colorOfStrawberries + ".")
colorOfLemons = fruitColors["lemons"]
print ("The color of a lemon is " + colorOfLemons + ".")
print("")

# update the existing values
colorOfGrapes = "green"
print ("The color of a grape is " + colorOfGrapes + ".")
print("")

# Step 6 create a new dictionary from given table
shoeCount = {
    "Jordan 13":1,
    "Yeezy":8,
    "Foamposite":10,
    "Air Max":5,
    "SB Dunk":20,
}

# Step 7 update the dictionary and its stored values based on given prompts
# Prompt 1 
print("This is the current stock.")
for i in shoeCount :
    print(i, shoeCount[i])
print("")

print("A customer came in to purchase 2 pairs of SB Dunks.")
shoeCount["SB Dunk"] = 18
for i in shoeCount :
    print(i, shoeCount[i])
print("")

# Prompt 2 
print("A customer came in to return a pair of Yeezys.")
shoeCount["Yeezy"] = 9
for i in shoeCount :
    print(i, shoeCount[i])
print("")

# Prompt 3 
print("The store got a new shipment. All stock increases by 7.")
for key in shoeCount:
    shoeCount[key] += 7

for i in shoeCount :
    print(i, shoeCount[i])
print("")

# Prompt 4
print("There is a special sale at the store. All stock decreases by 3.")
for key in shoeCount:
    shoeCount[key] -= 3

for i in shoeCount :
    print(i, shoeCount[i])
print("")

# add new values to the dictionary
print("Not the cocaine whites...")
shoeCount["G Fazos"] = 100

for i in shoeCount :
    print(i, shoeCount[i])
print("")

# Step 8 || adding 3 new key : value pairs to all the dictionaries created
print("Adding to my grocery list...")
groceryList["Sour Patch Kids"] = "$1.49"
groceryList["Hot Ruffles"] = "$4.29"
groceryList["Agua"] = "$2.50"
for i in groceryList :
    print(i, groceryList[i])
print("")

print("Adding to my fruit list...")
fruitColors["blueberries"] = "blue"
fruitColors["banana"] = "yellow"
fruitColors["black berry"] = "black"
for i in fruitColors :
    print(i, fruitColors[i])
print("")

print("Adding to the shoe store...")
shoeCount["97s"] = 34
shoeCount["Vans"] = 80
shoeCount["The one that look like socks"] = 22
for i in shoeCount :
    print(i, shoeCount[i])
print("")

# Step 9 || Delete any two keys from all of your dictionaries and print
print("Deleting from my grocery list...")
del groceryList["Beef"]
del groceryList["Milk"]
for i in groceryList :
    print(i, groceryList[i])
print("")

print("Deleting from my fruit list...")
del fruitColors["grape fruit"]
del fruitColors["black berry"]
for i in fruitColors :
    print(i, fruitColors[i])
print("")

print("Getting rid of the shoes that aren't selling...")
del shoeCount["Jordan 13"]
del shoeCount["SB Dunk"]
for i in shoeCount :
    print(i, shoeCount[i])
print("")