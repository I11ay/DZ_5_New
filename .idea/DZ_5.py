
a = int(input())
b = int(input())
c = int(input())
if a > 10 and a % 3 == 0 and b > 10 and b % 3 == 0 and c > 10:
    print('Yes')
else:
    print('No')

a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(f'max: {a}')
elif b > a and b > c:
    print(f'max: {b}')
elif c > a and c > b:
    print(f'max: {c}')
else:
    print('Вы ввели равные значения')

number = int(input())
first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10
reversed_number = third_digit * 100 + second_digit * 10 + first_digit
print(reversed_number)
