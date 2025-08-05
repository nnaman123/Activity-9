#check if entered number is a amstrong number or not
#take input from user
num = int(input("Enter a number: "))
#initialize sum and temp variable
sum = 0

temp = num
#find the sum of cubes of digits
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:

#display result
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")