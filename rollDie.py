import random

numDie = int(input("How many die would you like to roll? "))
rolls = []
sum = 0
for die in range(numDie):
    dieValue = random.randrange(1, 7)
    rolls.append(dieValue)
    sum += dieValue
print(rolls)
print("Sum: " + str(sum))