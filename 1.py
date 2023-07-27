from random import randint as intr  


value = intr(1,199)
found = False

while not found:
    answer = int(input("please enter a number between 1 and 199: "))
    if answer == value:
     break
    elif answer < value:
       print("the number you enter is smaller than actual value")
    elif answer > value:
       print("the number you enter is grater than actual value")
print(f"well done the number is {value}")