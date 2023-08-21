# Завдання 1
# У списку цілих, заповненому випадковими числами обчислити:
import random
print(random.randint(-5, 5))
Nums_syze = 5
numbers = []
for i in range (Nums_syze):
    numbers.append(random.randint(-10, 10))
numbers.sort()
print(numbers)
# Суму негативних чисел:
numbers.sort()

res = 0
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        res += numbers[i]
    else:
        break
    i += 1
print (f"Sum of negative numbers: {res}")
# Суму парних чисел:

result = list()

for i in range(len(numbers)):

   if numbers[i] % 2 == 0:

       result.append(numbers[i])

   else:

       continue
s = (sum(result))
print (f"Sum of even numbers: {s}")
# Суму непарних чисел:
result = list()

for i in range(len(numbers)):

   if numbers[i] % 2 != 0:

       result.append(numbers[i])

   else:

       continue
p = (sum(result))
print (f"Sum of odd numbers: {p}")
# Добуток елементів з кратними індексами 3:
product = 1
for item in numbers:
    if item % 3 == 0:
        product *= item

print (f"Product of elements divisible by 3: {product}")
# Добуток елементів між мінімальним та максимальним елементом:
def prod(arr):
    p = 1
    for a in arr:
        p *= a
    return p

mi, ma = 0, 0
for i in range(len(numbers)):
    if numbers[i] > numbers[ma]:
        ma = i
    if numbers[i] < numbers[mi]:
        mi = i
a, b = min(ma, mi), max(ma, mi)
print(f"Product of elements between minimum and maximum:", prod(numbers[a + 1:b]))

# Суму елементів, що знаходяться між першим та останнім позитивними елементами:
def fun():

    for i, v in enumerate(numbers):
        if v > 0:
            break
    for j, v in enumerate(reversed(numbers)):
        if v > 0:
            j = len(numbers) - j - 1
            break
    return sum(numbers[i + 1:j])


print("The sum of elements between the first and last positive elements:",fun())



# Завдання 2
# Є список цілих, заповнений випадковими числами.
print(random.randint(-5, 5))
amount_of_elements = 5
Initial_list = []
for i in range (amount_of_elements):
    Initial_list.append(random.randint(-10, 10))
print(f"Source List: {Initial_list}")
# На підставі даних цього масиву потрібно:
# Створити список цілих, що містить лише парні числа з першого списку:
even_list = [i for i in Initial_list if not i%2]
print(f"List of even: {even_list}")

# Створити список цілих, що містить лише непарні числа з першого списку:
odd_list = [i for i in Initial_list if i%2]
print(f"List of odd: {odd_list}")

# Створити список цілих, що містить лише негативні числа з першого списку:
negative_list = [i for i in Initial_list if i < 0]
print(f"Negative list: {negative_list}")

# Створити список цілих, що містить лише позитивні числа з першого списку:
positive_list = [i for i in Initial_list if i >= 0]
print(f"Positive list: {positive_list}")