print("Welcome To PYTHON Restaurant,Foodie")
menu = {"tea":20,"coffee":30,"sandwich":40,"pasta":80,"pizza":100,"patties":25}
print("Tea☕= 20\nCoffee🍵 = 30\nSandwich🥪= 40\nPasta🍝= 80\nPizza🍕= 100\nPatties🥐= 25")
grand_total=0
while True:
    order1 =input("Enter The Item You Want to Order :-").lower()
    if order1 in menu:
        print(f"Your {order1} has been added to the list")
        grand_total+=menu[order1]
        # print(f"Your Bill is{grand_total}")
    else:
        print(f"Please Enter a Valid Item from menu")
    # print("Do You Want to Order Another Item? (Yes/No)")
    another_item=input("Do You Want to Order Another Item? (Yes/No):-").lower()
    if another_item=="yes":
        item2=input("Enter The Item You Want to Order :-")
        grand_total+=menu[item2]
        print(f"Your {item2} has been added to the List")
        print(f"Thank You,For Visiting Our Cafe,Your Total Bill is {grand_total},Have a Nice Day,Foodie")
    else:
        print(f"Thank You,For Visiting Our Cafe,Your Total Bill is {grand_total},Have a Nice Day,Foodie")
    break