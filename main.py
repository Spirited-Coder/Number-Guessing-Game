import math
import random

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

x = random.randint(lower, upper)

chances = round(math.log(upper - lower + 1, 2))
print("\n\tYou've only", chances, "chances to guess the integer!\n")

count = 0

while count < chances:
    num = int(input("Enter a number between {} and {}: ".format(lower, upper)))

    if num == x:
        print("\nCongratulations! You have guessed correctly in {} tries".format(count + 1))
        break

    elif num < x:
        print("\nYou have guessed too low")

    else:
        print("\nYou have guessed too high")

    count += 1

if count >= chances:
    print("\nThe number is", x)
    print("\tBetter Luck Next time!")