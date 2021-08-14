number = int(input("Enter a number Mani: "))
c = number % 10
number = number // 10
b = number % 10
number = number // 10
a = number % 10
inverse = c * 100 + b * 10 + a

print("Your inverse number is ", inverse)
