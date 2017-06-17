import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

result = ''

if len(temps) == 0:
    print("0")
else:
    temps2 = temps.split()
    result = temps2[0]

    for temp in temps2:
        if abs(int(temp)) < abs(int(result)):
            result = temp
        elif abs(int(temp)) == abs(int(result)):
            result = max(int(temp), int(result)) 

print result
