# David Lim, 1625277

import math

paintColors = {'red':35, 'blue':25, 'green':23}

wallHeight = int(input("Enter wall height (feet):\n"))

wallWidth = int(input("Enter wall width (feet):\n"))

wall_area = (wallHeight*wallWidth)

paint_needed = (wall_area/350)

print("Wall area:",wall_area,'square feet')

print("Paint needed: {:.2f} gallons".format(paint_needed))

cans = math.ceil(paint_needed)

print("Cans needed:", cans,'can(s)')

color = input('\nChoose a color to paint the wall:\n')

print("Cost of purchasing",color,"paint: $"+str(cans*paintColors[color]))
