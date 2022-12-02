import csv
import time
filename = open('/home/chityanj/wayup/titanic.csv')
file = csv.DictReader(filename)

count = 0
for row in file:
    if row['Cabin'] == '':
        count += 1
    if row['PassengerId'] == '':
        count += 1
    if row['Survived'] == '':
        count += 1
    if row['Pclass'] == '':
        count += 1
    if row['Name'] == '':
        count += 1
    if row['Age'] == '':
        count += 1
    if row['Fare'] == '':
        count += 1
    if row['SibSp'] == '':
        count += 1
    if row['Sex'] == '':
        count += 1
    if row['Parch'] == '':
        count += 1
    if row['Ticket'] == '':
        count += 1
    if row['Embarked'] == '':
        count += 1
print(f'The number of Empty Columns is: {count}')

filename = open('/home/chityanj/wayup/titanic.csv')
file = csv.DictReader(filename)

AvgAge = []
for row in file:
    if row['Survived'] == '1':
        if row['Age'] != '':
            AvgAge.append(float(row['Age']))
print(f'Average Age of people who survived: {sum(AvgAge)/len(AvgAge)}')

