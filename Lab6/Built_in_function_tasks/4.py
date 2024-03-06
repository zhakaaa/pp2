import time
import math

number = int(input())
milli = int(input())
seconds = milli/ 1000
time.sleep(seconds)
print(f"Square root of {number} after {milli} is {math.sqrt(number)} ")