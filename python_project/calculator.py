print("calculator")

def calculator():
    print("calculator")
    print("(+ , - , * , / )")
    
    num1 = float(input(" ENTER number: "))
    op = input("<< + ,  _  , * , / >> :")
    num2 = float(input(" ENTER number: "))
    
    if op == "+" :
        result = num1 + num2
    elif op == "-" :
        result = num1 - num2
    elif op == "*" :
        result = num1 * num2
    elif op == "/" :
        if num2 != 0 :
            result = num1 / num2
        else :
            result = "not true"
    else:
        result = "not true"
        
    print(f" => {result}")







calculator()