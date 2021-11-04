# David Lim, 1625277

import csv

print("[ID] [Manufacturer] [Type] [Price] [Service Date] [Damaged Item]")

with open('C:/Users/david/PycharmProjects/pythonProject/FullInventory.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row)

with open('C:/Users/david/PycharmProjects/pythonProject/PastServiceDateInventory.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row,'Expired Item(No longer service available)')

class AllInventory:
    def __init__(ddlim, item_list):
        ddlim.item_list = item_list

def full(ddlim):

      with open('C:/Users/david/PycharmProjects/pythonProject/FullInventory.csv', 'w') as file:
         items = ddlim.item_list
         keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
         for item in keys:
            id = item
            mf_name = items[item]['manufacturer']
            item_type = items[item]['item_type']
            price = items[item]['price']
            service_date = items[item]['service_date']
            damaged = items[item]['damaged']
            file.write('{},{},{},{},{},{}\n'.format(id,mf_name,item_type,price,service_date,damaged))

def by_type(ddlim):

      items = ddlim.item_list
      types = []
      keys = sorted(items.keys())
      for item in items:
         item_type = items[item]['item_type']
         if item_type not in types:
            types.append(item_type)
      for type in types:
         file_name = type.capitalize() + 'FullInventory.csv'
         with open('C:/Users/david/PycharmProjects/pythonProject/'+file_name, 'w') as file:
            for item in keys:
               id = item
               mf_name = items[item]['manufacturer']
               price = items[item]['price']
               service_date = items[item]['service_date']
               damaged = items[item]['damaged']
               item_type = items[item]['item_type']
               if type == item_type:
                  file.write('{},{},{},{},{}\n'.format(id, mf_name, price, service_date, damaged))

def past_service(ddlim):

      items = ddlim.item_list
      keys = sorted(items.keys(), key=lambda x: time.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse=True)
      with open('C:/Users/david/PycharmProjects/pythonProject/PastServiceDateInventory.csv', 'w') as file:
         for item in keys:
            id = item
            mf_name = items[item]['manufacturer']
            item_type = items[item]['item_type']
            price = items[item]['price']
            service_date = items[item]['service_date']
            damaged = items[item]['damaged']
            today = time.now().date()
            service_expiration = time.strptime(service_date, "%m/%d/%Y").date()
            expired = service_expiration < today
            if expired:
               file.write('{},{},{},{},{},{}\n'.format(id, mf_name, item_type, price, service_date, damaged))


def damaged(ddlim):

      items = ddlim.item_list
      keys = sorted(items.keys(), key=lambda x: items[x]['damaged'], reverse=True)
      with open('C:/Users/david/PycharmProjects/pythonProject/DamagedInventory.csv', 'w') as file:
         for item in keys:
          id = item
          mf_name = items[item]['manufacturer']
          item_type = items[item]['item_type']
          price = items[item]['price']
          service_date = items[item]['service_date']
          damaged = items[item]['damaged']
         if damaged:
            file.write('{},{},{},{},{}\n'.format(id, mf_name, item_type, price, service_date))


if __name__ == '__main__':
   items = {}
   files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
   for file in files:
      with open(file, 'r') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         for line in csv_reader:
            item_id = line[0]
            if file == files[0]:
               items[item_id] = {}
               mf_name = line[1]
               item_type = line[2]
               damaged = line[3]
               items[item_id]['manufacturer'] = mf_name.strip()
               items[item_id]['item_type'] = item_type.strip()
               items[item_id]['damaged'] = damaged.strip()
            elif file == files[1]:
               price = line[1]
               items[item_id]['price'] = price
            elif file == files[2]:
               service_date = line[1]
               items[item_id]['service_date'] = service_date

   inventory= FullInventory (items)
   inventory.full()
   inventory.by_type()
   inventory.past_service()
   inventory.damaged()

   types = []
   manufacturers = []
   for item in items:
      checked_manufacturer = items[item]['manufacturer']
      checked_type = items[item]['item_type']
      if checked_manufacturer not in types:
         manufacturers.append(checked_manufacturer)
      if checked_type not in types:
         types.append(checked_type)

   user_input = None
   while user_input != 'q':
      user_input = input("\nEnter an item manufacturer and item type (ex: Samsung phone) or enter 'q' to quit:\n")
      if user_input == 'q':
          break
      else:
         selected_manufacturer = None
         selected_type = None
         user_input = user_input.split()
         wrong = False
         for word in user_input:
            if word in manufacturers:
               if selected_manufacturer:
                  wrong = True
               else:
                  selected_manufacturer = word
            elif word in types:
               if selected_type:
                  wrong = True
               else:
                  selected_type = word
         if not selected_manufacturer or not selected_type or wrong:
            print("No such item in inventory")
         else:
            keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

            matching_items = []

            similar_items = {}
            for item in keys:
               if items[item]['item_type'] == selected_type:
                  service_date = items[item]['service_date']
                  if items[item]['manufacturer'] == selected_manufacturer:
                     if not items[item]['damaged']:
                        matching_items.append((item, items[item]))
                  else:
                     if not items[item]['damaged']:
                        similar_items[item] = items[item]

            if matching_items:
               item = matching_items[0]
               item_id = item[0]
               mf_name = item[1]['manufacturer']
               item_type = item[1]['item_type']
               price = item[1]['price']
               service_date = item[1]['service_date']
               damaged = item[1]['damaged']
               print("Your item is: {}, {}, {}, {}\n".format(item_id, mf_name, item_type, price))

               if similar_items:
                  matched_price = price
                  closest_item = None
                  closest_price_diff = None
                  for item in similar_items:
                     if closest_price_diff == None:
                        closest_item = similar_items[item]
                        closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                        item_id = item
                        mf_name = similar_items[item]['manufacturer']
                        item_type = similar_items[item]['item_type']
                        price = similar_items[item]['price']
                        continue
                     price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                     if price_diff < closest_price_diff:
                        closest_item = item
                        closest_price_diff = price_diff
                        item_id = item
                        mf_name = similar_items[item]['manufacturer']
                        item_type = similar_items[item]['item_type']
                        price = similar_items[item]['price']
                  print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, mf_name, item_type, price))

               else:
                  print("No such item in inventory")
