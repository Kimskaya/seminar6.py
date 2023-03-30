''' в списке хранятся числа. Нужно выбрать только чётные числа и составить пары. Число плюс его квадрат
data = [1,2,3,4,5,6,7,8]
res = list ()
for i in data:
    if i%2==0:
        res.append((i,i**2))
print (res)'''

def select (func, collect):
    return [func(x) for x in collect]
def where (finc, collect):
    return [x for x in collect if f(x)]
data = [1,2,3,4,5,6,7,8]
res = select (int , data)
print (res)
res = where (lambda x: x %2==0, res)
print (res)
res = where list (select(lambda x : (x, x**2), res))

list_1 = [x for x in range (1,20)]
print (list_1)
list_1 = list (map(lambda x: x+10, list_1))
