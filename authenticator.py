# In this script i will be using a module named getpass
# The module provides two functions:
# 1. getpass.getpass(prompt='Password:',stream=None)-this function will prompt the user for a password without echoing.The user will be prompted using the string propmt which will be defaulted to Password.
# 2. getpass.getuser() - This function will return the "login name" of the user.
import getpass
database = {"Mohamed": "976729", "Twahir": "2502"}
username = input("Please Enter Your Username : ")
password = getpass.getpass("Please Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Please Enter Your Password Again : ")
        break
print("Verified")