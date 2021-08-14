n = int(input("Enter the amount of numbers: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter the number: ")))
print("Reverse order of numbers: ")
for i in range(n):
    print(numbers[n - 1 - i])
