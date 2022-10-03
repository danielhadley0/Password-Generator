import random
import csv
from sre_parse import SPECIAL_CHARS


#Collecting data from the user
print("Please enter the name of the platform.")
platformName = input()

print("Please enter the desired length of your password.")
passwordLength = int(input())


#Initializing the password variable as well as creating a string containing all letters of the alphabet
password = ""
letters = "abcdefghijklmnopqrstuvwxyz"


#Logic creating the password
for a in range(0,passwordLength):
    numOrChar = random.randint(1,2)
    #If the random number chosen is 2, then add a random number to the password
    if numOrChar == 2:
        password += str(random.randint(0,9))
    else:
        #If the number is 1, then the program must determine whether or not the next item (a)
        #is a letter or special character
        letterOrSpecial = random.randint(1,2)
        #If the second random number is 1, then the program adds a random special character to the password
        if letterOrSpecial == 1:
            password += SPECIAL_CHARS[random.randint(0,len(SPECIAL_CHARS)-1)]
        else: 
            #If the program reaches this line, then it is determined that the next character is a letter
            #Now the program uses the same logic as above to determine if the letter is capital or lowercase
            selectedLetter = letters[random.randint(0,len(letters)-1)]
            capOrLower = random.randint(1,2)
            if capOrLower == 1:
                password += selectedLetter.upper()
            else:
                password += selectedLetter


#Writing the data to a csv file
newData = [platformName, password]

with open('passwords.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(newData)