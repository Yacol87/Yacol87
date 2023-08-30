# https://www.practicepython.org/

# 30 In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

from urllib.request import urlopen
url = "http://norvig.com/ngrams/sowpods.txt"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
file = open("D:\down\myfile.txt" , "w")
file.write(html)
file.close()

print(html)

# #28 Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
#
# number1 = int(input("Give me first number"))
# number2 = int(input("Give me 2nd number"))
# number3 = int(input("Give me 3rd number"))
#
# print ("Your biggest number is ", max(number1,number2,number3))

#21 write some strings from user to a file
# contentUsera = input("Co chcesz dopisać do pliku ")
#
# f = open("D:\down\myfile.txt", "x")
# f.write("\n" + contentUsera)
#
# f.close()
#
# f = open("D:\down\myfile.txt", "r")
# print(f.read())


# 18 Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#
# import random
# myRandomNumber = str(random.randrange(10,99))
# randomNumberList = [x for x in myRandomNumber]
#
#
# print(randomNumberList)
#
# def bullsAndCowsGame():
#     guess = str(input("Tell me 2 digit number you thought about"))
#     guessList = [y for y in guess]
#     if guess == int(myRandomNumber):
#         print("Wow you got it, it was indeed", myRandomNumber)
#     else:
#         if guessList[0] == randomNumberList[0]:
#             print("First digit is correct")
#             if guessList[1] ==randomNumberList[1]:
#                 print("Second digit is correct as well")
#             else:
#                 print("2nd digit was not correct")
#         elif guessList[1] ==randomNumberList[1]:
#             answer = ("Only 2nd digit is correct")
#             print (answer)
#             f = open("D:\down\myfile.txt", "a")
#             f.write("\n" + answer)
#         else: print("no digits were correct")
#
#
#
# wantToPlay = input("Want to play a guessing game? Say Yes or No: ")
#
# if wantToPlay.upper() == "YES":
#     bullsAndCowsGame()
# else:
#     print("We will play next time")

# 15 ask for a string and return it in reverse order
# userString = str(input("Hello, please give me several words and I will return them "))
# userString2 = userString.split()
# userString2.reverse()
# lenght = int(len(userString2))
# x=0
#
# while (x < lenght):
#     print(userString2[x])
#     x += 1
#
#
# print ("You gave:", *userString, sep = "")

# 14a Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# listA  = []
# setA = set()
#
# def addItemsToList():
#     x = input("Give me item for your list")
#     listA.append(x)
#     wantAdd = input("Want to add more items - Yes or No")
#     if wantAdd.upper() == ("YES"):
#         addItemsToList()
#
# def removeDuplicates():
#     for y in listA:
#         if y not in setA:
#             setA.add(y)
#
# if input("Wanna create a list? Yes or No") == "Yes":
#     addItemsToList()
# else:
#     print("No list creation then, good day!")
#
# if input("Wanna remove duplicates too?") == ("Yes"):
#     removeDuplicates()
#
# print (listA)
# print (setA)


#13 Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions
# fibonnaciList = [1,1]
#
# numberOfIntegers = int(input("Hello, give me number of Fibonnaci integers to return to you: "))
# while (len(fibonnaci)< numberOfIntegers):
#     firstToAdd = (len(fibonnaci) -1)
#     secondToAdd = (len(fibonnaci) -2)
#     fibonnaci.append(fibonnaci[firstToAdd]+fibonnaci[secondToAdd])
#
# print (fibonnaci)


#12 Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# list = [2,4,6,8,10,12]
# list_new = []
#
# lenght = int(len(list))-1
#
# list_new.append(list[0])
# list_new.append(list[lenght])
#
# print (list_new)
#

#11 Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).

# number = int(input("Give me a number and I will check if it's prime one"))
# x = 1
# divisors = []
#
# while number > x:
#     if (number % x ==0):
#         divisors.append(x)
#     x += 1
#
# if len(divisors) > 1:
#     divisors.pop(0)
#     print ("Your", number," is not prime, it has these divisors", divisors)
# else:
#     print ("Your", number," is indeed prime!")


#9 Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# import random
# myRandomNumber = random.randrange(1,10)
#
# def guessingGame(x):
#     guess = int(input("I created a number between 1-9. Guess which one is it"))
#     if myRandomNumber == guess:
#         print("wow, you got it, it was indeed", guess, " . It took you this many tries: ", x)
#     elif myRandomNumber > guess:
#         print("missed, my number is higher")
#         x += 1
#         wannaPlayContinuation = input("Wanna keep trying")
#         if wannaPlayContinuation in ("Yes", "yes", "y", "YES"):
#             guessingGame(x)
#     elif myRandomNumber < guess:
#         print("missed, my number is lower")
#         x += 1
#         wannaPlayContinuation = input("Wanna keep trying")
#         if wannaPlayContinuation in ("Yes", "yes", "y", "YES"):
#             guessingGame(x)
#
# wannaPlay = input("I created a number between 1-9. Wanna play & guess which one it is?")
# if wannaPlay in ("Yes", "yes", "y","YES"):
#     guessingGame(1)
# else:
#     print("No guessing today")


#8 Make a two-player Rock-Paper-Scissors game.

# items = ["rock","paper","scissors"]
# question = ("What's your choice in  the game out of", items)
# first_item = input(question)
# print ("Ok, now 2nd player choice")
# second_item = input(question)
#
# if first_item == second_item:
#     print ("It's a tie")
# elif first_item == "paper" and second_item == "rock":
#     print ("first guy won")
# elif first_item == "rock" and second_item == "paper":
#     print ("second guy won")
# elif first_item == "paper" and second_item == "scissors":
#     print("second guy won")
# elif first_item == "rock" and second_item == "scissors":
#     print("first guy won")
# elif first_item == "scissors" and second_item == "rock":
#     print ("second guy won")
# elif first_item == "scissors" and second_item == "paper":
#     print ("first guy won")
# else:
#     print("seems you didn't choose any item out of", items)

#7 a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

#Mine, but not one line xD
# list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for x in list_a:
#     if (x % 2) !=0:
#         list_a.remove(x)
# print (list_a)

# Web solution b = [element for element in list_a if element % 2 == 0]


#6 Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# user_string = input("Hi, tell me a word, I will return it in a backward position")
# list_string = []
#
# for x in user_string:
#     list_string.append(x)
#
# list_string.reverse()
# print (list_string)


#5 Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# duplicates_list = []
#
# x = 0
# y = 0
# for x in list_a:
#     if x in list_b:
#         duplicates_list.append(x)
# print (duplicates_list)

#4 Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

# number = int(input("Hi, give me a number and I will tell you it's divisors"))
# x = 1
# divisors =[]
#
# while x < number:
#     if (number % x == 0):
#         divisors.append(x)
#     x += 1
#
# print ("These are divisors of", number)
# print (divisors)

#     print("it's odd")

#3 Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# listB = []
#
# for x in listA:
#     if x <5:
#         listB.append(x)
# print (listB)


#2 Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# number = input("Hi, give me a number and I will check if it's odd or even")
# numberInt = int(number)
# if numberInt % 2 == 0:
#     print("It's even")
# else:


# Exercise 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# urodzenie = input("Hi, can tell me the year you were born please")
# urodzenieInt = int(urodzenie)
# print ("You will retire at", urodzenieInt+65)













