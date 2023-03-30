#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint
def CheckValue (myArray, minI, maxI):
    for i in range (len(myArray)):
        if minI<=myArray[i]<=maxI:
           print (f"Element index is ",i)

arrLen = int(input("Input array length   "))
myArr = []
for j in range (arrLen):
    myArr.append(randint(0,10))
print (*myArr)
minValue= int(input("Input the minimum value   "))
maxValue = int(input("Input the maximum value  "))
result= []
result= CheckValue (myArr, minValue, maxValue)




