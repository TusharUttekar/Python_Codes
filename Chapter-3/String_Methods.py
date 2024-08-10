#String methods and exercise using builtin functions

var_string = input("Enter the string : ")
print(f"The user input is {var_string}")

var_local = "Hello to the  python programmer"
print(var_local.find("  "))
print(var_local.replace(" ","  ").replace("programmer","user").find("python"))