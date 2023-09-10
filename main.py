import numpy as np
import pandas as pd
#0 passangerID
#1 Survived
#2 Pclass
#3 Name
#4 Sex
#5 Age
#6 SibSp
#7 Parch
#8 Ticket
#9 Fare
#10 Cabin
#11 Embarked

accuracy = 0
numProcessed = 0

def calcSurvival(arr):
    sum = 0
    for i in range(arr.size):
        if(i == 1):
            survived = arr[i]
            #print('this is survived ' + str(arr[i]))
        if(i == 2):
            pClass = arr[i]
            #print('this is pClass ' + str(arr[i]))
        if(i == 4):
            sex = arr[i]
            #print('this is sex ' + str(arr[i]))
        if(i == 5):
            age = arr[i]
            #print('this is age ' + str(age))
            if(age > 20):
                sum -= 0.4
    if arr[1] == 1:
        if sum >= 0:
            print("successfully predicted survival")
        else:
            print("individual survived, prediction says they did not")
    else: #arr[1] == 0
        if sum < 0:
            print("successfully predicted failure to survive")
        else:
            print("individual did not survive, prediction says they did")

    #print(sum)

train = pd.read_csv('train.csv')
#for i in range(len(train)):
#print(len(train))
for i in range(0, 5):
    calcSurvival(train.iloc[i].values)
    # calcSurvival(train.iloc[i].to_numpy)
    # print(train.iloc[i])
    # print()

