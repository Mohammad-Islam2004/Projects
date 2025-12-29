# HISTORY GENERATING CALCULATOR

HISTORY_FILE = "10_project\\2_history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print('No history found..!')
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared...')

def save_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format (num operator num), e.g., 2 + 2')
        return
    num1 = float(parts[0])
    opr = parts[1]
    num2 = float(parts[2])

    if opr == '+':
         result = num1 + num2
    elif opr == '-':
        result = num1 - num2
    elif opr == '*':
        result = num1 * num2
    elif opr == '/':
        if num2 == 0:
            print('Number cannot be divided by zero.')
            return
        result = num1 / num2
    else :
        print('Invalid operator..!')
        return

    if int(result) == result:
        result = int(result)
    print("Result :", result)
    save_history(user_input, result)

def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input('Enter calculation(+,-,*,/) or commands(history, clear or save) = ')
        if user_input == 'exit':
            print('Goodbye')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else :
            calculator(user_input)

main()