# Exercise 11
# Your solution comes here

s = int(input())

bills_500 = s // 500
s %= 500
bills_100 = s // 100
s %= 100
bills_10 = s // 10
s %= 10
bills_5 = s // 5
s %= 5
bills_1 = s

print(f"{bills_500} (500) {bills_100} (100) {bills_10} (10) {bills_5} (5) {bills_1} (1)")

# "//" = floor division (Divides and returns the integer value of the quotient, ignoring the remainder))
# "%" = modulo (returns the remainder of dividing)
# "f"" = format string