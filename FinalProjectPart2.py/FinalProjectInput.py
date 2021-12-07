data = {"id" : [1167234, 2390112, 9034210, 3001265, 2347800, 1009453],

"manufacturer":["Apple", "Dell", "Dell", "Samsung", "Apple", "Lenovo"],

"type" : ["phone", "laptop", "tower", "phone", "laptop", "tower"],

"price": [534, 799, 345, 1200, 999, 599]}

while True:

   q = input("Type your query or either allow q to quit: ")
   if(q == "q"):
      break
      
   item = ""
   type = ""

   for i in data["manufacturer"]:
      if i in q:
         item = i

   for i in data["type"]:
      if i in q:
         type = i

   if(item == "" or type == ""):
      print("No such item in invetory")

   else:
      information = ["", "", "", 0]
      for i in range(len(data["id"])):
         if(data["manufacturer"][i] == item and data["type"][i] == types):
            if(information[3] < data["price"][i]):

               information[0] = data["id"][i]
               information[1] = data["manufacturer"][i]
               information[2] = data["type"][i]
               information[3] = data["price"][i]

   print("Your item is " + str(information[0]) + " " + str(information[1]) + " " + str(information[2]) + " " + str(information[3]))

   left = []
   for i in range(len(data["id"])):
      if(data["type"][i] == type and data["manufacturer"][i] != item):
         left.append([data["id"][i], data["manufacturer"][i], data["type"][i], data["price"][i]])

   if(len(left) != 0):
      print("You may also consider ")

      for i in range(len(left)):
         print(str(left[i][0]) + " " + left[i][1] + " " + left[i][2] + " " + str(left[i][3]))
