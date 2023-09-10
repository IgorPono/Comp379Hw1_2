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

correctPredictions = 0
incorrectPredictions = 0
totalPredictions = 0
# numProcessed = 0

def calcSurvival(arr):
    global totalPredictions
    global correctPredictions
    global incorrectPredictions
    totalPredictions += 1
    sum = 0
    for i in range(arr.size):
        #if(i == 1):
        #    survived = arr[i]
        #    #print('this is survived ' + str(arr[i]))
        if(i == 2):
            pClass = arr[i]
            if pClass == 3:
                sum += 0.1
            elif pClass == 2:
                sum -= 0.7
            else:
                sum -= 0.1
            #print('this is pClass ' + str(arr[i]))
        if(i == 4):
            sex = arr[i]
            #print('this is sex ' + str(arr[i]))
            if sex == 'male':
                sum -= 0.2
            else:
                sum += 0.8
        if(i == 5):
            age = arr[i]
            #print('this is age ' + str(age))
            if age > 10:
                sum += 0.05
            elif age > 10 and age < 20:
                sum += 0.1
            elif age > 20 and age < 30:
                sum -= 0.4
            elif age > 30 and age < 40:
                sum += 0.5
            else:
                sum -= 0.05
    if arr[1] == 1:
        if sum >= 0:
            # correctPredictions+=1
            # print("successfully predicted survival")
            correctPredictions += 1
        else:
            incorrectPredictions += 1
            # print("individual survived, prediction says they did not")
    else: #arr[1] == 0
        if sum < 0:
            # print("successfully predicted failure to survive")
            correctPredictions += 1
        else:
            incorrectPredictions += 1
            # print("individual did not survive, prediction says they did")
    print(correctPredictions/totalPredictions)
    #print(sum)

train = pd.read_csv('train.csv')
for i in range(len(train)):
#print(len(train))
#for i in range(0, 100):
    calcSurvival(train.iloc[i].values)
    # calcSurvival(train.iloc[i].to_numpy)
    # print(train.iloc[i])
    # print()

