print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
print('')
shopService1=input("Select first service:\n")
shopService2=input("Select second service:\n")
totalServiceAmount=0
print("\nDavy's auto shop invoice\n")

if(shopService1.lower()=="oil change"):
    print("Service 1: Oil change, $35")
    totalServiceAmount=totalServiceAmount+35
elif(shopService1.lower()=="tire rotation"):
    print("Service 1: Tire rotation, $19")
    totalServiceAmount=totalServiceAmount+19
elif(shopService1.lower()=="car wash"):
    print("Service 1: Car wash, $7")
    totalServiceAmount=totalServiceAmount+7
elif(shopService1.lower()=="car wax"):
    print("Service 1: Car wax, $12")
    totalServiceAmount=totalServiceAmount+12
elif(shopService1=="-"):
    print("Service 1: No service")
if(shopService2.lower()=="oil change"):
    print("Service 2 Oil change, $35")
    totalServiceAmount=totalServiceAmount+35
elif(shopService2.upper()=="tire rotation"):
    print("Service 2: Tire rotation, $19")
    totalServiceAmount=totalServiceAmount+19
elif(shopService2.lower()=="car wash"):
    print("Service 2: Car wash, $7")
    totalServiceAmount=totalServiceAmount+7
elif(shopService2.lower()=="car wax"):
    print("Service 2: Car wax, $12")
    totalServiceAmount=totalServiceAmount+12
elif(shopService2=="-"):
    print("Service 2: No service")

print("\nTotal: $%d"%totalServiceAmount)