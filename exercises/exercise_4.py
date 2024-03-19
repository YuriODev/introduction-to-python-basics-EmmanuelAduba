# Exercise 4
# Your solution comes here

n = int(input())

d1 = n // 1000
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10

difference = abs((d1 - d4) + (d2 - d3))

print(max(1 - difference, 0))