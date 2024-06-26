#Jeremy Roalef
#this program will store the main process of the project.
from Product import Product
from LinkedList import LinkedList
from Stack import Stack
#get the savedData.py file information
from savedData import *
#Get user account class
from UserAccount import UserAccount
#get Functionalities class
from Functionalities import Functionalities
#get Colors class for color coding
from Colors import Colors

#create empty dictionary to store products with their ID as a key & the object as the value.
#this INCLUDES the objects of the products
productDictionary = {}
#create empty list to store product names & organize the products. This DOES NOT INCLUDE the objects of the products
productList = []
#cerate Dictionary for the user accounts
userAccounts = {}

#create guest and admin accounts for user functionality
guestAccount = UserAccount("guest", "123", 0, "guest")

#initialize the user account to guest when program starts
currentUser = guestAccount

STR_GUEST = "guest"
STR_USER = "user"
STR_ADMIN = "admin"
STR_ADMIN_PASSWORD = "CITA225"

#store functionality objects in a list.
functionalities = [
    Functionalities("add_product","Add Product",[STR_ADMIN]),
    Functionalities("remove_product","Remove Product",[STR_ADMIN]),
    Functionalities("update_product_information","Update Product Information",[STR_ADMIN]),
    Functionalities("add_to_cart","Add To Cart",[STR_GUEST, STR_USER]),
    Functionalities("remove_from_cart","Remove From Cart",[STR_GUEST, STR_USER]),
    Functionalities("undo_remove_from_cart","Undo Remove From Cart",[STR_GUEST, STR_USER]),
    Functionalities("display_inventory","Display Inventory",[STR_GUEST, STR_USER, STR_ADMIN]),
    Functionalities("display_cart","Display Cart",[STR_GUEST, STR_USER]),
    Functionalities("login","Login",[STR_GUEST]),
    Functionalities("sign_up","Sign Up",[STR_GUEST]),
    Functionalities("sign_out","Sign Out",[STR_USER, STR_ADMIN]),
    Functionalities("delete_account","Delete Account",[STR_USER, STR_ADMIN]),
    Functionalities("get_user_names","Get User Names",[STR_ADMIN]),
    Functionalities("set_admin_permission","Set Admin Permission",[STR_USER]),
    Functionalities("change_user_name","Change User Name",[STR_USER, STR_ADMIN]),
    Functionalities("change_password","Change Password",[STR_USER]),
    Functionalities("check_account_information","Check Account Info",[STR_GUEST,STR_USER]),
    Functionalities("proceed_to_checkout", "Proceed To Checkout", [STR_USER]),
    Functionalities("add_funds", "Add Funds", [STR_USER])
]

def main():

    #initialize the program information
    initialize_program()
    print(productList)
    continueProgram = True
    #loop main function.
    while continueProgram:
        continueProgram = display_options()

    end_program()

#permissions: admin
def add_product():
    #this method should create a new product object with ID, Price, Name, & Quantity
    #ask user to enter values for a new product

    pID = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product ID, or type -1 to exit: "
                             f"{Colors.RESET}", "int")

    #exit if input is negative
    if pID < 0:
        return

    #if ID already exists, ask user to enter a different ID
    while pID in productDictionary:
        print(f"{Colors.RED}{Colors.BOLD}ID already exists. Please enter a different ID{Colors.RESET}")
        pID = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product ID, or type -1 to exit: "
                                 f"{Colors.RESET}", "int")
        # exit if input is negative
        if pID < 0:
            return

    pName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product Name,or type -1 to exit: "
                               f"{Colors.RESET}", "string")
    pName = pName.lower()

    #exit if input is negative
    if pName == "-1":
        return


    #if name already exists in productlist, ask user to enter a different name. this should igore case sensitivity
    while pName in productList:
        print(f"{Colors.RED}{Colors.BOLD}name already exists. Please enter a different name{Colors.RESET}")
        pName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product Name,or type -1 to exit: "
                                   f"{Colors.RESET}", "string")
        pName = pName.lower()

        # exit if input is negative
        if pName == "-1":
            return

    pPrice = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product price, or type -1 to exit: "
                                f"{Colors.RESET}", "float")

    # exit if input is negative
    if pPrice < 0:
        return

    pQuantity = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the quantity of the product, or type -1 to exit: "
                                   f"{Colors.RESET}", "int")

    # exit if input is negative
    if pQuantity < 0:
        return

    #create new obejct
    newProduct = Product(pID, pName, round(pPrice, 2), pQuantity)

    #add object to dictionary
    productDictionary[newProduct.get_id()] = newProduct

    #add product name to list
    productList.append(newProduct.get_name())

#permissions: admin
def remove_product():
    display_inventory()
    #remove the product from the list & dictionary
    userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product ID you want to remove, "
                                f"or type -1 to exit: {Colors.RESET}", "int")

    if userInput < 0:
        return

    #check if item is in the dictionary. if not, ask user to enter a different value
    while userInput not in productDictionary:
        print(f"{Colors.RED}{Colors.BOLD}Product ID not found. Please enter a different ID{Colors.RESET}")
        userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the product ID you want to remove, "
                                       f"or type -1 to exit: {Colors.RESET}", "int")
        if userInput < 0:
            return

    #store name of product in temp variable to remove from productList
    pName = productDictionary[userInput].get_name()

    #remove product from list & dictionary
    productDictionary.pop(userInput)
    productList.remove(pName)

#permissions: admin
def update_product_information():
    #store keys of dictionary in variable
    productKeys = productDictionary.keys()

    #display products and their ID to the user
    display_inventory()

    #ask the user for a product ID.
    userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter a product ID, or type -1 to exit: "
                                   f"{Colors.RESET}", "int")
    #check if ID exists. if not, ask for existing product ID
    while userInput not in productKeys:
        if userInput < 0:
            return
        print(f"{Colors.RED}{Colors.BOLD}ID not found. Please enter an existing product ID{Colors.RESET}")
        userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter a product ID, or type -1 to exit: "
                                       f"{Colors.RESET}", "int")

    #display functionality options to the user
    print(f"{Colors.BLUE}{Colors.BOLD}0. {Colors.RESET}"
          f"{Colors.LIME}{Colors.BOLD}Update Product Name{Colors.RESET}"
          f"{Colors.BLUE}{Colors.BOLD}\n1. "
          f"{Colors.LIME}{Colors.BOLD}Update Product Price\n{Colors.RESET}"
          f"{Colors.BLUE}{Colors.BOLD}2. {Colors.RESET}"
          f"{Colors.LIME}{Colors.BOLD}Update Product Quantity{Colors.RESET}")
    #ask user to enter an option
    userFunctionality = ask_for_user_input(f"{Colors.YELLOW}{Colors.BOLD}What would you like to update for the product: "
                                           f"{Colors.RESET}", "int")
    #check for valid input
    while userFunctionality != 0 and userFunctionality != 1 and userFunctionality != 2:
        if userFunctionality < 0:
            return
        else:
            print(f"{Colors.RED}{Colors.BOLD}Unsupported input. Please enter one of the following values{Colors.RESET}")
            print(f"{Colors.BLUE}{Colors.BOLD}0. {Colors.RESET}"
                  f"{Colors.LIME}{Colors.BOLD}Update Product Name{Colors.RESET}"
                  f"{Colors.BLUE}{Colors.BOLD}\n1. "
                  f"{Colors.LIME}{Colors.BOLD}Update Product Price\n{Colors.RESET}"
                  f"{Colors.BLUE}{Colors.BOLD}2. {Colors.RESET}"
                  f"{Colors.LIME}{Colors.BOLD}Update Product Quantity{Colors.RESET}")
            userFunctionality = ask_for_user_input(
                f"{Colors.YELLOW}{Colors.BOLD}What would you like to update for the product: "
                f"{Colors.RESET}", "int")

    #match user input to the functionality
    match (userFunctionality):
        case 0:
            #run update product name functionality
            update_product_name(userInput)
        case 1:
            #run update product price functionality
            update_product_price(userInput)
        case 2:
            #run update product quantity functionality
            update_product_quantity(userInput)

#permissions: guest, user
def add_to_cart():
    #loop until the user doesn't want to continue shopping
    while True:
        #each node will be a Product added to the cart.
        #Display all products & let user choose product they want.
        for index in range(len(productList)):
            print(f"{Colors.BLUE}{Colors.BOLD}{index}. {Colors.RESET}"
                  f"{Colors.LIME}{productList[index]}{Colors.RESET}")


        #ask the user what product to add to cart
        userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}please choose an item you want to add to cart, "
                                    f"or type -1 to exit: {Colors.RESET}", "int")
        if userInput < 0:
            return
        #check for valid input
        while userInput >= len(productList):
            print(f"{Colors.RED}{Colors.BOLD}Invalid input. Please choose one of the diplayed products, or type -1 to exit"
                  f"{Colors.RESET}")
            for index in range(len(productList)):
                print(f"{Colors.BLUE}{Colors.BOLD}{index}. {Colors.RESET}"
                      f"{Colors.LIME}{productList[index]}{Colors.RESET}")
            userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}please choose an item you want to add to cart, "
                                           f"or type -1 to exit: {Colors.RESET}", "int")
            if userInput < 0:
                return


        #find user option in productDictionary.
        for key in productDictionary:
            #store object in a temporary variable.
            tempObj = productDictionary[key]

            #check if the user input corresponds to an existing product
            if tempObj.get_name() == productList[userInput]:
                #check if the store has ran out of the product
                if tempObj.get_quantity() == 0:
                    print(f"{Colors.RED}{Colors.BOLD}Sorry, we are out of that product{Colors.RESET}")
                    break; #no need to continue looping
                else:
                    #store current user's shopping cart in temporary cart
                    tempCart = currentUser.get_shopping_cart()
                    #iterate through the shopping cart, comparing the tempObj's ID to the current ID in the cart
                    index = 0
                    #check if cart is empty. if it is, simply add new item to cart
                    if tempCart.isEmpty():
                        print(f"{Colors.YELLOW}{Colors.BOLD}adding to empty cart...{Colors.RESET}")
                        # create new product & append to the temporary cart.
                        newProduct = Product(tempObj.get_id(), tempObj.get_name(), tempObj.get_price(), 1)
                        # append object to cart
                        tempCart.addLast(newProduct)
                        tempObj.remove_quantity(1)
                        break; #no need to continue looping

                    while index < tempCart.getSize():
                        #compare the ID of the tempObj to the ID of the object in cart
                        if tempObj.get_id() == tempCart.get(index).get_id():
                            print(f"{Colors.YELLOW}{Colors.BOLD}adding to existing item...{Colors.RESET}")
                            #add 1 to quantity of the object in cart & remove 1 from the product in the dictionary
                            tempCart.get(index).add_quantity(1)
                            tempObj.remove_quantity(1)
                            break; #no need to continue looping
                        else:
                            #check if the object is last in cart. If so, we need to add a new product to the cart
                            if index == tempCart.getSize()-1:
                                print(f"{Colors.YELLOW}{Colors.BOLD}adding new item to cart...{Colors.RESET}")
                                #create new product & append to the temporary cart.
                                newProduct = Product(tempObj.get_id(), tempObj.get_name(), tempObj.get_price(), 1)
                                #append object to cart
                                tempCart.addLast(newProduct)
                                #remove 1 from product in dictionary
                                tempObj.remove_quantity(1)
                                break; #no need to continue looping

                        index += 1

#permissions: guest, user
def remove_from_cart():
    #loop until user doesn't want to remove a product
    while True:
        #remove first occurrence of an item from the cart, add 1 quantity back to the product, add action to cart history
        #create list showing products they can remove

        index = 0
        while index < currentUser.get_shopping_cart().getSize():
            print(f"{Colors.BLUE}{Colors.BOLD}{index}. {Colors.RESET}"
                  f"{Colors.LIME}{currentUser.get_shopping_cart().get(index).get_name()}{Colors.RESET}")
            index += 1

        #ask user what they want to remove
        userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}What product from cart do you want to remove?, "
                                    f"or type -1 to exit: {Colors.RESET}", "int")
        if userInput < 0:
            return
        while userInput >= currentUser.get_shopping_cart().getSize():
            print(f"{Colors.RED}{Colors.BOLD}Invalid input. Please choose one of the diplayed products, or type -1 to exit"
                  f"{Colors.RESET}")

            index = 0
            while index < currentUser.get_shopping_cart().getSize():
                print(f"{Colors.BLUE}{Colors.BOLD}{index}. {Colors.RESET}"
                      f"{Colors.LIME}{currentUser.get_shopping_cart().get(index).get_name()}{Colors.RESET}")
                index += 1
            userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}What product from cart do you want to remove?, "
                                           f"or type -1 to exit: {Colors.RESET}", "int")
            if userInput < 0:
                return

        #remove 1 quantity of product from cart & add action to history
        print(f"{Colors.YELLOW}{Colors.BOLD}removing...{Colors.RESET}")
        #add action to cart history
        currentUser.add_to_cart_history(currentUser.get_shopping_cart().get(userInput))
        #add respective quantity back to the inventory
        productDictionary[currentUser.get_shopping_cart().get(userInput).get_id()].add_quantity(1)


        currentUser.get_shopping_cart().get(userInput).remove_quantity(1)
        #if quantity of product is 0, remove product object from cart. (there's no more of that product)
        if currentUser.get_shopping_cart().get(userInput).get_quantity() == 0:
            #remove product
            currentUser.get_shopping_cart().removeAt(userInput)

#permissions: guest, user
def undo_remove_from_cart():
    #store object in variable
    addBackToCart = currentUser.get_cart_history().pop()
    #check if item has been popped from cart
    if addBackToCart != None:
        #check if the inventory is empty
        if productDictionary[addBackToCart.get_id()].get_quantity() == 0:
            print(f"{Colors.YELLOW}{Colors.BOLD}Sorry, we are out of that product{Colors.RESET}")
            return
        else:
            #remove respective quantity from product dictionary
            productDictionary[addBackToCart.get_id()].remove_quantity(1)

            print(f"{Colors.YELLOW}{Colors.BOLD}Adding back to cart{Colors.RESET}")
            #find product in current user's shopping cart and add the respective quantity back to the cart
            index = 0
            if currentUser.get_shopping_cart().getSize() == 0:
                #add item to empty cart
                newProduct = Product(addBackToCart.get_id(), addBackToCart.get_name(), addBackToCart.get_price(), 1)
                currentUser.get_shopping_cart().addLast(newProduct)
                return
            while index <= currentUser.get_shopping_cart().getSize():
                #check if the ID of the product to add match the index of the product
                if addBackToCart.get_id() == currentUser.get_shopping_cart().get(index).get_id():
                    #add back to the quantity of that product
                    currentUser.get_shopping_cart().get(index).add_quantity(1)
                    break; #no need to continue looping
                else:
                    if index == currentUser.get_shopping_cart().getSize():
                        #create new object qith respective quantity and append to the the user's shopping cart
                        newProduct = Product(addBackToCart.get_id(), addBackToCart.get_name(), addBackToCart.get_price(),
                                             1)
                        currentUser.get_shopping_cart().addLast(newProduct)
                        break; #no need to continue looping
                index += 1
    else:
        print(f"{Colors.YELLOW}{Colors.BOLD}No action in history{Colors.RESET}")

#permissions: guest, user, admin
def display_inventory():
    for key in productDictionary:
        print(f"{Colors.BLUE}{Colors.BOLD}{productDictionary[key]}{Colors.RESET}")
        print()

#permissions: guest, user
def display_cart():
    #print the shopping cart
    print(f"{Colors.BLUE}{Colors.BOLD}{currentUser.get_shopping_cart()}{Colors.RESET}")

#permissions: guest
def login():
    #get the keys of the user account dictionary
    userAccountKeys = userAccounts.keys()

    #ask user for username and password.
    userName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Username: {Colors.RESET}", "string")
    password = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Password: {Colors.RESET}", "string")
    #search for the username in the dictionary
    while userName not in userAccountKeys or password != userAccounts[userName].get_password():
        #tell user the username or password is wrong and ask for new username and password
        print(f"{Colors.RED}{Colors.BOLD}Incorrect username or password{Colors.RESET}")
        tryAgain = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Try Again (enter positive number for yes, "
                                      f"negative number for no)? {Colors.RESET}","float")
        if tryAgain < 0:
            return
        userName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Username: {Colors.RESET}", "string")
        password = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Password: {Colors.RESET}", "string")

    #declare currentUser variable global before using to bypass making it a local variable
    global currentUser
    currentUser = userAccounts[userName]

    #add guest shopping cart and cart history to current user's shopping cart and cart history
    while not guestAccount.get_shopping_cart().isEmpty():
        currentUser.add_to_shopping_cart(guestAccount.get_shopping_cart().removeFirst())
    while not guestAccount.get_cart_history().isEmpty():
        currentUser.add_to_cart_history(guestAccount.get_cart_history().pop())

#permissions: guest
def sign_up():
    #get the keys in the current userAccounts dictionary
    userAccountNames = userAccounts.keys()

    #ask the user for a username and password
    userName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Username: {Colors.RESET}", "string")
    while userName in userAccountNames:
        print(f"{Colors.RED}{Colors.BOLD}Username already taken. Please enter a different username{Colors.RESET}")
        userName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Username: {Colors.RESET}", "string")

    password = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Password: {Colors.RESET}", "string")
    checkPassword = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Re-enter Password: {Colors.RESET}", "string")

    #ask the user to enter a new password if the two passwords do not match
    while password != checkPassword:
        print(f"{Colors.RED}{Colors.BOLD}Passwords do not match. Please re-enter your password{Colors.RESET}")
        password = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Password: {Colors.RESET}", "string")
        checkPassword = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Re-enter Password: {Colors.RESET}", "string")

    #create user account
    newAccount = UserAccount(userName, password, 0, "user",
                             guestAccount.get_shopping_cart(), guestAccount.get_cart_history())
    #store account in dictionary
    userAccounts[newAccount.get_user_name()] = newAccount

    #delete guest account shopping cart and cart history
    guestAccount.set_shopping_cart(LinkedList())
    guestAccount.set_cart_history(Stack())


    #declare currentUser variable global before using to bypass making it a local variable
    global currentUser
    #set current user to new user
    currentUser = newAccount

#permissions: user, admin
def sign_out():
    #declare currentUser variable global before using to bypass making it a local variable
    global currentUser
    currentUser = guestAccount

#permissions: user
def delete_account():
    deleteString = "DELETE"
    print(f"{Colors.YELLOW}{Colors.BOLD}Are you sure you want to delete your account?{Colors.RESET}"
          f"{Colors.YELLOW}{Colors.BOLD}\nType '{Colors.RESET}"
          f"{Colors.RED}{Colors.BOLD}{deleteString}{Colors.RESET}"
          f"{Colors.YELLOW}{Colors.BOLD}' to delete your account, or type '{Colors.RESET}"
          f"{Colors.RED}{Colors.BOLD}no{Colors.RESET}"
          f"{Colors.YELLOW}{Colors.BOLD}' to exit{Colors.RESET}")
    userInput = ask_for_user_input("", "string")

    while userInput != deleteString:
        if userInput == "no":
            return
        print(f"{Colors.RED}{Colors.BOLD}invalid input. \n{Colors.RESET}"
              f"{Colors.YELLOW}{Colors.BOLD}Please enter '{Colors.RESET}"
              f"{Colors.RED}{Colors.BOLD}{deleteString}' {Colors.RESET}"
              f"{Colors.YELLOW}{Colors.BOLD}to delete your account, or type '{Colors.RESET}"
              f"{Colors.RED}{Colors.BOLD}no{Colors.RESET}"
              f"{Colors.YELLOW}{Colors.BOLD}' to exit{Colors.RESET}")
        userInput = ask_for_user_input("", "string")

    global currentUser
    userAccounts.pop(currentUser.get_user_name())
    currentUser = guestAccount

#permissions: admin
def get_user_names():
    #print the usernames, separated by lines
    for key in userAccounts:
        print(f"{Colors.BLUE}{Colors.BOLD}{key}{Colors.RESET}")

#permissions: user
def set_admin_permission():
    #if the account enters the correct admin password, set account type to admin
    userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the password, or type 'no' to exit: "
                                   f"{Colors.RESET}", "string")
    while userInput != STR_ADMIN_PASSWORD:
        if userInput == "no":
            return
        else:
            print(f"{Colors.RED}{Colors.BOLD}Incorrect password.{Colors.RESET}")
            userInput = ask_for_user_input(
                f"{Colors.BLUE}{Colors.BOLD}Please enter the password, or type '{Colors.RESET}"
                f"{Colors.CYAN}{Colors.BOLD}no{Colors.RESET}"
                f"{Colors.BLUE}{Colors.BOLD}' to exit: {Colors.RESET}"
                f"{Colors.RESET}", "string")
    #if you got this far, you get to be an admin!
    currentUser.set_account_type("admin")

#permissions: user, admin
def change_user_name():
    userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}New Username: {Colors.RESET}", "string")
    currentUser.set_user_name(userInput)

#permissions: user
def change_password():
    print("Type 'no' at any moment to return to main menu.")
    #ask user for their password, then ask for new password and to re-enter the new password
    currentPassword = currentUser.get_password()
    userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter your password: {Colors.RESET}",
                                   "string")

    while userInput != currentPassword:
        if userInput == "no":
            return
        print(f"{Colors.RED}{Colors.BOLD}Incorrect password{Colors.RESET}")
        userInput = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter your password: {Colors.RESET}",
                                       "string")

    #if user types 'no, return to main menu'
    newPassword = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}New Password: {Colors.RESET}", "string")
    if newPassword == "no":
        return
    checkPassword = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Re-enter Password: {Colors.RESET}", "string")
    if checkPassword == "no":
        return

    #ask the user to enter a new password if the two passwords do not match
    while newPassword != checkPassword:
        print(f"{Colors.RED}{Colors.BOLD}Passwords do not match. Please re-enter your password, or type 'no' to exit{Colors.RESET}")
        newPassword = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}New Password: {Colors.RESET}", "string")
        if newPassword == "no":
            return
        checkPassword = ask_for_user_input("Re-enter Password: ", "string")
        if checkPassword == "no":
            return

    currentUser.set_password(newPassword)

#permissions: guest, user
def check_account_information():
    print(f"{Colors.BLUE}{Colors.BOLD}{currentUser}{Colors.RESET}")

#permissions: user
def proceed_to_checkout():
    print("Sorry, this functionality currently does not work")
    return
#permissions: guest, user
def add_funds():
    print("Sorry, this functionality currently does not work")
    return


#use this function to get user input
def ask_for_user_input(strMessage, type):
    #store user input in a variable & check if all characters are digits
    userInput = input(strMessage)

    #print("type entered: " + type)

    match type:

        case "string":
            #print("returning a string")
            return userInput
        case "int":
            #print("returning an int")

            # replace "." in potential string with "" to better test string with isDigit() function
            # Credit for idea: https://pythonhow.com/how/check-if-a-string-is-a-float/
            testInput = userInput.replace(".", "")
            testInput = userInput.replace("-", "")
            #Check if user input is a number. if not, make them enter a valid number
            while not testInput.isdigit():
                print(f"{Colors.RED}{Colors.BOLD}Please enter a valid number{Colors.RESET}")
                userInput = input(strMessage)
                testInput = userInput.replace(".", "")
                testInput = userInput.replace("-", "")

                # check if user input is an integer. if not, that is it contains a "." in the number, repeat the function
                # for the user to enter an integer.
            if "." in userInput:
                print(f"{Colors.RED}{Colors.BOLD}Please enter an integer{Colors.RESET}")
                userInput = ask_for_user_input(strMessage, type)
            return int(userInput)
        case "float":
            #print("returning a float")

            # replace "." in potential string with "" to better test string with isDigit() function
            # Credit for idea: https://pythonhow.com/how/check-if-a-string-is-a-float/
            testInput = userInput.replace(".", "")
            testInput = testInput.replace("-", "")

            #print("testinput:" + str(testInput))

            # Check if user input is a number. if not, make them enter a valid number
            while not testInput.isdigit():
                print(f"{Colors.RED}{Colors.BOLD}Please enter a valid number{Colors.RESET}")
                userInput = input(strMessage)
                testInput = userInput.replace(".", "")
            return float(userInput)
        case __:
            raise Exception("Error: 'type' argument is invalid. Valid types:\nstring\nint\nfloat")
#initializeProgram will retrieve all data from savedData.py file to initialize the list, dictionary, shopping cart,
#and the cart history.
def display_options():
    print("\n\n\n")
    # display the current user and account type
    print(f"{Colors.CYAN}Welcome: {Colors.RESET}"
          f"{Colors.BOLD}{Colors.GREEN}{currentUser.get_user_name()}{Colors.RESET}")

    #print("current acct type: " + currentUser.get_account_type())
    #store current user's account type
    currentAccountType = currentUser.get_account_type()

    #create supported functionalities list
    supportedFunctionalities = []
    #loop through functionalities and append the functionalities to the supported functionalities list

    for index in range(len(functionalities)):
        if currentAccountType in functionalities[index].get_functionality_permissions():
            supportedFunctionalities.append(functionalities[index])


    #loop through functionalities and display options to the user
    for index in range(len(supportedFunctionalities)):
        print(f"{Colors.BLUE}{Colors.BOLD}{str(index + 1)}. {Colors.RESET}"
              f"{Colors.LIME}{supportedFunctionalities[index].get_functionality_text()}{Colors.RESET}")

    print(f"{Colors.RED}{Colors.BOLD}Default: Exit Program{Colors.RESET}")

    userInput = ask_for_user_input(f"{Colors.BLUE}Please enter your Option: {Colors.RESET}", "int")

    if userInput-1 not in range(len(supportedFunctionalities)):
        return False
    else:
        print("\n\n\n")
        #Credit for idea: ChatGPT.
        #Given Prompt: I am programming in Python. I want to call a function in my file by using a string. How can I do that?
        if (supportedFunctionalities[userInput-1].get_functionality_name() in globals() and
                callable(globals()[supportedFunctionalities[userInput-1].get_functionality_name()])):

             globals()[supportedFunctionalities[userInput-1].get_functionality_name()]()
    return True

def update_product_quantity(pID):
    #ask user for new quantity for the product
    newQuantity = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}please enter the new quantity of the product, "
                                     f"or type -1 to exit: {Colors.RESET}", "int")
    #return if value is negative
    if newQuantity < 0:
        return
    #update quantity of the product
    productDictionary[pID].set_quantity(newQuantity)

def update_product_name(pID):
    #store old product ID in variable
    oldName = productDictionary[pID].get_name()

    pName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the new product Name,or type -1 to exit: "
                               f"{Colors.RESET}", "string")
    pName = pName.lower()

    # exit if input is negative
    if pName == "-1":
        return
    # if name already exists in productlist, ask user to enter a different name. this should igore case sensitivity
    while pName in productList:
        print(f"{Colors.RED}{Colors.BOLD}name already exists. Please enter a different name{Colors.RESET}")
        pName = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the new product Name,or type -1 to exit: "
                                   f"{Colors.RESET}", "string")
        pName = pName.lower()
        # exit if input is negative
        if pName == "-1":
            return

    #update product name in dictionary and list
    productList.remove(oldName)
    productList.append(pName)
    productDictionary[pID].set_name(pName)

def update_product_price(pID):
    pPrice = ask_for_user_input(f"{Colors.BLUE}{Colors.BOLD}Please enter the new product price, or type -1 to exit: "
                                f"{Colors.RESET}", "float")
    # exit if input is negative
    if pPrice < 0:
        return
    #update product price
    productDictionary[pID].set_price(pPrice)

def initialize_program():
    #set the productDictionary from dictionary information given by savedData.py
    #read each element in the 2-d list, create the product given the information, & store that in the dictionary
    for i in range(len(dictionaryInformation)):
        list = dictionaryInformation[i]
        pID = list[0]
        pName = list[1]
        pPrice = list[2]
        pQuantity = list[3]
        #create object
        tempObj = Product(pID,pName,pPrice,pQuantity)
        #send object to dictionary
        productDictionary[pID] = tempObj

    #set the productList from listInformation given by savedData.py
    for element in listInformation:
        productList.append(element)


    #set the userAccounts dictionary from the userAccountInformation list given by SavedData.py
    #print(userAccountInformation)
    for row in userAccountInformation:
        #store info in respective variables
        UAName = row[0]
        UAPassword = row[1]
        UABalance = row[2]
        UAAccountType = row[3]


        shoppingCartObj = LinkedList()
        #loop through 2-d lists and create objects to store in linked list object
        UAShoppingCart = row[4]
        for i in UAShoppingCart:
            # store info in respective variables
            pID = i[0]
            pName = i[1]
            pPrice = i[2]
            pQuantity = i[3]

            # create temporary object
            tempShoppingCartProduct = Product(pID, pName, pPrice, pQuantity)
            shoppingCartObj.add(tempShoppingCartProduct)


        cartHistoryObj = Stack()
        #loop through the 2d lists and create objects to store in stack object
        UACartHistory = row[5]
        # set the cartHistory from cartHistoryInformation given by savedData.py
        # reverse order of cartHistoryInformation. first in is last element in list
        UACartHistory.reverse()
        for j in UACartHistory:
            # store info in respective variables
            pID = j[0]
            pName = j[1]
            pPrice = j[2]
            pQuantity = j[3]
            # create temporary object
            tempCartHistoryProduct = Product(pID, pName, pPrice, pQuantity)
            # send obejct to cartHistory
            cartHistoryObj.push(tempCartHistoryProduct)

        #create the UserAccount object
        tempObj = UserAccount(UAName,UAPassword,UABalance,UAAccountType,shoppingCartObj,cartHistoryObj)

        #send object to userAccounts dictionary
        userAccounts[UAName] = tempObj

#end program will save all user data to a python file. saved data will include the list, dictionary, shopping cart,
#and the cart history.
def end_program():
    file = open("savedData.py", "w")

    #to save an object to the file, you need to get each attribute out of the object & send the information over.
    #data will be saved in a 2-d list. each row will save the obejct information & each column will contain
    #the product ID, name, price, and quanitity in that order

    #add productDictionary information
    objectList = []

    for key in productDictionary:
        pID = productDictionary[key].get_id()
        pName = productDictionary[key].get_name()
        pPrice = productDictionary[key].get_price()
        pQuantity = productDictionary[key].get_quantity()

        objectList.append([pID,pName,pPrice,pQuantity])

    #write the dictionary information to the file
    file.write("dictionaryInformation = " + str(objectList) + "\n")

    #write product list to the file
    file.write("listInformation = " + str(productList) + "\n")

    #add user accounts information
    userAccountInformation = []

    for key in userAccounts:
        UAName = userAccounts[key].get_user_name()
        UAPass = userAccounts[key].get_password()
        UABalance = userAccounts[key].get_balance()
        UAAccountType = userAccounts[key].get_account_type()

        UAShoppingCart = []
        while not currentUser.get_shopping_cart().isEmpty():
            shoppingCartObj = currentUser.get_shopping_cart().removeLast()
            pID = shoppingCartObj.get_id()
            pName = shoppingCartObj.get_name()
            pPrice = shoppingCartObj.get_price()
            pQuantity = shoppingCartObj.get_quantity()
            UAShoppingCart.append([pID, pName, pPrice, pQuantity])

        UACartHistory = []
        while not currentUser.get_cart_history().isEmpty():
            cartHistoryObj = currentUser.get_cart_history().pop()
            pID = cartHistoryObj.get_id()
            pName = cartHistoryObj.get_name()
            pPrice = cartHistoryObj.get_price()
            pQuantity = cartHistoryObj.get_quantity()
            UACartHistory.append([pID, pName, pPrice, pQuantity])

        userAccountInformation.append([UAName,UAPass,UABalance,UAAccountType,UAShoppingCart,UACartHistory])

    file.write("userAccountInformation = " + str(userAccountInformation) + "\n")

    #close the file
    file.close()

main()