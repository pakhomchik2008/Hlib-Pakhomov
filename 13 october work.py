#q1
'''
x = lambda a : a+15
print(x(10))

z = lambda a,y : a*y
print(z(10,11))
'''
from os.path import split

#q2
'''
x = lambda a: a**2
x2 = lambda a : a**3
x3= lambda a : a**4
x4 = lambda a : a**5
z = int(input('number '))
print(x(z))
print(x2(z))
print(x3(z))
print(x4(z))
'''
#q3
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x : (x%2 == 0), numbers)
# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers) 
'''

'''
numbers = input("numbers: ").split()
numbers = [int(n) for n in numbers]

even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
result = list(even_numbers)
print('Even numbers ', result)
odd_numbers_generator = filter(lambda x : x % 2 != 0, numbers)
odd_numbers = list(odd_numbers_generator)
print('Odd numbers ', odd_numbers)
'''

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x*x, numbers))
result = list(squared_numbers)
print('Squared numbers ', result)
cubed_numbers = list(map(lambda x: x**x, numbers))
result1 = list(cubed_numbers)
print('Cubed numbers ', result1)
'''

#q5
'''
str1 = 'ahahhah'
str2= '1234'
check = lambda x : x.isdigit()
print(check(str1))
print(check(str2))
'''

#q6
'''
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 10]
intersection = set(arr1) & set(arr2)
result = list(intersection)
print(result)
'''

#q7
'''
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x : x % 2 == 0, arr1))
result = list(even_numbers)
print(len(result))

odd_numbers = list(filter(lambda x : x % 2 != 0, arr1))
result1 = list(odd_numbers)
print(len(result1))
'''




