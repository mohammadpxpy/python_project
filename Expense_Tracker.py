print("💲Expense Tracker💲")

start = input("for staet click ENTER")
if len(start) == 0:
    while True:
        run = input(" for add print << add >> \n for bookkeeping print << calculator >> \n << exit >> \n") 
        if run == "add":
            history = input("enter history: ")
            list_Expense = []
            
            while True:
                expense = input("<< exit >> Expense Tracker and Description: ")
                list_Expense.append(expense)
                if expense == "exit":
                    break
            with open("Expense_Tracker.txt", "a") as file:
                file.write(f"{history}\n Expense : {" - ".join(list_Expense[:-1])} \n")
            print("✔")
        if run == "calculator":
            def calculator():
                num1 = float(input("enter number: "))
                op = input("<< +,-,*,/ >>: ")
                num2 = float(input("enter number: "))
                
                result = None
                
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("😶")
                else:
                    print("🤐")

                print(f" => {result}")
                with open(r"C:\Users\pc\Desktop\project\Expense_Tracker.txt", "a") as file:
                    file.write(f"bookkeeping => {result} \n")
                
            calculator()
            
        elif run == "exit":
            print("god bay ☹ \n come again👀")
            break