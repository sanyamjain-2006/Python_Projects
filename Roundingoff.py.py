try:
    a = int(input("Enter The Integer Value only :"))
    b = float(input("Enter The Decimal Value only:"))
except ValueError:
    print("Please enter Integer and Decimal in there Individual Columns,")
else:
    if b >= 0.5:
        a += 1
        print(f"The rounded value is {a}")
    else:
        print(f"The number is {a}")
