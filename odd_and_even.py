def is_even(number):
    return number %2 == 0
def is_odd(number):
    return not is_even(number)
num = input("Please enter a sequence of numbers")


int_list = []
for n in num:
    if n != " ":
        int_list.append(int(n))
print(int_list)

for n in int_list:
    if is_odd(n):
        print(n)