# Test file that acts as a four function calculator so I can use it to test the packages stuff


def four_function(op1, op2, chosen):
    answer = 0
    if chosen == 1:
        answer = op1 + op2   
    elif chosen == 2:
        answer = op1 - op2 
    elif chosen == 3:
        answer = op1 * op2
    elif chosen == 4:
        answer = op1 / op2
    else:
        return 0
    return answer


def main():
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. End Program")
    chosen = input("Select one of the above options: ")
    if 1 <= chosen < 5:
        operand1 = int(input("Enter operand 1: "))
        operand2 = int(input("Enter operand 2: "))
        answer = four_function(operand1, operand2, chosen)
        print(f"The answer is: {answer}")
    else:
        print("Program ending....")
    
if __name__ == "__main__":
    main()
