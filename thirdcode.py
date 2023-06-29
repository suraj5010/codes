def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a positive integer: "))

while num <= 0:
    print("Invalid input! Please enter a positive integer.")
    num = int(input("Enter a positive integer: "))
result = sum_of_digits(num)
print("Sum of digits:", result)
