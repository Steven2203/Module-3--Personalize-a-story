#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Create your custom story inserting custom input values.
# Author:      Steven
# Created:     22-05-2022
# Copyright:   (c) Steven 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##I created a function that accepts user input then prints out the results.

givenName = (str)
surName = (str)
myAge = (int)
visitedPlace = (str)
servedFood = (str)

def customStory(givenName,surName,myAge,visitedPlace,servedFood):
    givenName = input("Enter your given name")
    surName = input("Enter your surname")
    visitedPlace = input("Describe a place you have visited")
    myAge = int(input("Enter your age"))
    if myAge <= 0:
     notValid = "This is not a valid number"
     return(myAge)
    else:
        servedFood = str(input("Describe the food you ate that day"))
        custStory = ("My name is "+givenName+" "+surName+" and i am "+str(myAge)+" years old and "+"i went to "+visitedPlace+" and i ate "+servedFood)
        print(custStory)
customStory(givenName,surName,myAge,visitedPlace,servedFood)


