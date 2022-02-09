# David Lim, 1625277

cups_lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
cups_water = float(input('Enter amount of water (in cups):\n'))
cups_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
# input the number of servings the recipe yields
cups_serving = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving))
print('%.2f cup(s) lemon juice' %(cups_lemon_juice))
print('%.2f cup(s) water'%(cups_water))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar))

cups_serving_needed = float(input('\nHow many servings would you like to make?\n'))

lemon_juice_for_one = cups_lemon_juice/cups_serving
water_for_one= cups_water/cups_serving
agave_nectar_for_one = cups_agave_nectar/cups_serving

cups_lemon_juice_needed = lemon_juice_for_one*cups_serving_needed
cups_water_needed = water_for_one*cups_serving_needed
cups_agave_nectar_needed = agave_nectar_for_one*cups_serving_needed

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f cup(s) lemon juice' %(cups_lemon_juice_needed))
print('%.2f cup(s) water'%(cups_water_needed))
print('%.2f cup(s) agave nectar'%(cups_agave_nectar_needed))

gallons_lemon_juice = cups_lemon_juice_needed/16
gallons_water = cups_water_needed/16
gallons_agave_nectar = cups_agave_nectar_needed/16

print('\nLemonade ingredients - yields %.2f servings' %(cups_serving_needed))
print('%.2f gallon(s) lemon juice' %(gallons_lemon_juice))
print('%.2f gallon(s) water'%(gallons_water))
print('%.2f gallon(s) agave nectar'%(gallons_agave_nectar))
