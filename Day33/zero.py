sum = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    sum += num;

print("Sum of entered numbers:", sum)