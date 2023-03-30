#Задача 30:  Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def ArithmeticProgress (elem, diff, num):
    progressArray = []
    for i in range (num):
        progressArray.append(elem+i*diff)
    return progressArray
element1 = int(input("Input the first element of your array  "))
number = int(input("Input the number of elements   "))
difference = int(input("Input the difference between the elements  "))
result = ArithmeticProgress (element1, difference, number)
print (result)


