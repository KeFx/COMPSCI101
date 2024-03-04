import math

total_seconds = int(input("Enter the total number of seconds: "))
hours = total_seconds // 3600
remainder_after_hours = (total_seconds % 3600)
minutes = remainder_after_hours // 60
seconds = remainder_after_hours % 60

print(total_seconds, "second(s) is equal to", hours,"hour(s),", minutes, "minute(s), and", seconds, "second(s).")