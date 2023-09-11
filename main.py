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
highestAcc = 0
highestAccWeight = 0
# numProcessed = 0
pClass3Weight = -1
pClass2Weight = 0
pClass1Weight = 0
maleWeight = 0
femaleWeight = 0
ageLess10Weight = 0
age10to20Weight = 0
age20to30Weight = 0
age30to40Weight = 0
age40to50Weight = 0
age50to60Weight = 0
age60AboveWeight = 0

def calcSurvival(arr):
    global totalPredictions, correctPredictions, incorrectPredictions, highestAcc
    global pClas3Weight, pClass2Weight, pClass1Weight
    global maleWeight, femaleWeight
    global ageLess10Weight, age20to30Weight, age30to40Weight, age40to50Weight, age50to60Weight,  age60AboveWeight
    totalPredictions += 1
    sum = 0
    for i in range(arr.size):
        #if(i == 1):
        #    survived = arr[i]
        #    #print('this is survived ' + str(arr[i]))
        if(i == 2):
            pClass = arr[i]
            if pClass == 3:
                sum += pClass3Weight
            elif pClass == 2:
                sum += pClass2Weight
            else:
                sum += pClass1Weight
            #print('this is pClass ' + str(arr[i]))
        if(i == 4):
            sex = arr[i]
            #print('this is sex ' + str(arr[i]))
            if sex == 'male':
                sum += maleWeight
            else:
                sum += femaleWeight
        if(i == 5):
            age = arr[i]
            #print('this is age ' + str(age))
            if age > 10:
                sum += ageLess10Weight
            elif age > 10 and age < 20:
                sum += age10to20Weight
            elif age > 20 and age < 30:
                sum += age20to30Weight
            elif age > 30 and age < 40:
                sum += age30to40Weight
            elif age > 40 and age < 50:
                sum += age40to50Weight
            elif age > 50 and age < 60:
                sum += age50to60Weight
            else:
                sum += age60AboveWeight
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
    #print(correctPredictions/totalPredictions)

train = pd.read_csv('train.csv')

for i in range(0, 200):
    correctPredictions = 0
    incorrectPredictions = 0
    totalPredictions = 0
    for j in range(len(train)):
        #print(totalPrediction)
        calcSurvival(train.iloc[j].values)
        #print(pClass3Weight)
    #print('about to calculate accuracy')
    #print(correctPredictions, totalPrediction)
    #print("weight: " + str(pClass3Weight))
    #print("acc: " + str(correctPredictions/totalPredictions))
    if highestAcc < (correctPredictions/totalPredictions):
        highestAcc = correctPredictions/totalPredictions
        highestAccWeight = pClass3Weight
        #print(highestAccWeight)
        #print(highestAcc)
    # highestAcc = max(highestAcc, correctPredictions/totalPredictions)
    pClass3Weight += 0.01
print()
print(highestAcc)
print(highestAccWeight)

#for i in range(len(train)):
#print(len(train))
#for i in range(0, 100):
#    calcSurvival(train.iloc[i].values)
    # calcSurvival(train.iloc[i].to_numpy)
    # print(train.iloc[i])
    # print()

