import math
wallHeight = float(input("Enter wall height (feet):\n"))
wallWidth = float(input("Enter wall width (feet):\n"))
area = wallHeight*wallWidth
print("Wall area:",int(area),"square feet")
paintNeeded = area/350
print("Paint needed: %0.2f gallons"%paintNeeded)
print("Cans needed:",math.ceil(paintNeeded),"can(s)")
paintColors = {
    'red': 35,
    'blue': 25,
    'green':23
}
color = input("\nChoose a color to paint the wall:\n")
print("Cost of purchasing",color,"paint:")
print("$",str(paintColors[color]))