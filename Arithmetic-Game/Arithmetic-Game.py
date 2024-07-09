life = 3

print("\nYour life is : " + str(life))
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

pick = int(input("\nChoose arithmetic operation : "))
firstNum = int(input("\nEnter 1st number : "))
secondNum = int(input("Enter 2nd number : "))

if pick == 1:
    finalAnswer = firstNum + secondNum
    operation = "+"
elif pick == 2:
    finalAnswer = firstNum - secondNum
    operation = "-"
elif pick == 3:
    finalAnswer = firstNum * secondNum
    operation = "*"
elif pick == 4:
    finalAnswer = firstNum / secondNum
    operation = "/"

print(str(firstNum) + " " + operation + " " + str(secondNum))

while(True):
    Ans = float(input("\nEnter Your Answer : "))
    if finalAnswer == Ans:
        print("\nYou won!\n")
        break
    else:
        life = life - 1
        print("\nYour answer is wrong! please try again")
        print("Your life is : " + str(life))
        if life == 0:
            print("\nGame Over!!!\n")
            break