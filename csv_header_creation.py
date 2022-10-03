import csv

headers = ["Platform", "Password"]

with open('passwords.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)