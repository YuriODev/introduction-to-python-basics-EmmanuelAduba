# Exercise 7
# Your solution comes here

number = int(input("Enter a four-digit number: "))

sum = number // 1000 + (number // 100) % 10 + (number // 10) % 10 + number % 10
print (sum)