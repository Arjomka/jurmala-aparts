
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        number = input("What number you want to see?: ")
        apart_number = int(number) - 1
        print(apartments[apart_number])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        
        
        
        def sort_price(apartment):
            return int(apartment[8])
        apartments.sort(key=sort_price, reverse = True)
        print(apartments[:10])

        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        def sort_price(apartment):
            return int(apartment[8])
        apartments.sort(key=sort_price)
        print(apartments[:10])

        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
      
        
        
        price = input("What price is?: ")
        

        top20cheaper = []

        for aparment in apartments:
            if int(aparment[-1]) <= int(price):
                top20cheaper.append(aparment)

        print(top20cheaper[:20])
        


        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        price = input("What price is?: ")
        

        top20expensive = []

        for aparment in apartments:
            if int(aparment[-1]) >= int(price):
                top20expensive.append(aparment)

        print(top20expensive[:20])

        pass

    elif choice == '6':
        # 
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("==========================")


