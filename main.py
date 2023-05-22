#Задача 2: Найдите сумму цифр трехзначного числа.

a = input()
a = int(a)

n1 = a % 10
a = a // 10
n2 = a % 10
a = a // 10

print (a ,"+",n2,"+",n1)
print("sum of nums: " , a + n2 + n1)



