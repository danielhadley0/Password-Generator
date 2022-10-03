import random
import csv
from sre_parse import SPECIAL_CHARS

print("Please enter the name of the platform.")
platformName = input()

print("Please enter the desired length of your password.")
passwordLength = int(input())



password = ""
letters = "abcdefghijklmnopqrstuvwxyz"

for a in range(0,passwordLength):
    numOrChar = random.randint(1,2)
    if numOrChar == 2:
        password += str(random.randint(0,9))
    else:
        letterOrSpecial = random.randint(1,2)
        if letterOrSpecial == 1:
            password += SPECIAL_CHARS[random.randint(0,len(SPECIAL_CHARS)-1)]
        else: 
            selectedLetter = letters[random.randint(0,len(letters)-1)]
            capOrLower = random.randint(1,2)
            if capOrLower == 1:
                password += selectedLetter.upper()
            else:
                password += selectedLetter


newData = [platformName, password]

with open('passwords.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(newData)






print(password)