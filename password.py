Password = input("Enter The Password Here:- ")
b = len(Password)

# As Length Should be Greater than 12
if b >= 12 :
# As Strong Password Should Contains a Special Character
    if "@" in Password or "#" in Password or "$" in Password or "!" in Password:
        # As Strong Password Should Contains at Least One Number
        if "1" in Password or "2" in Password or "3" in Password or "4" in Password or "5" in Password or "6" in Password or "7" in Password or "8" in Password or "9" in Password or "0" in Password:
            print("You chose a strong password, but keep in mind that it shouldn't contain your name, DOB, address, or personal details.")
        else:
            print("Password must contain at least one number.")
    else:
        print("Password must contain at least one special character (@, #, $, or !).")
    print("Save this Password To Avoid Inconvenience and Enable Two-Factor Authentication For More Safety")
else:
    print("Password length must be between 12 and 14 characters.")
