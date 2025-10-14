
while True:
        start = input("for start click << Enter >>")
        name_commodity = input("Product name: ")
        price = int(input("Price of Product💲: "))
        discount = int(input("Product discount💱: "))
        
    
        if discount == 0:
            price_discount = (price * discount / 100)
            price_with_discount = price
        else:
            price_discount = (price * discount / 100)
            price_with_discount = price - price_discount
            
        
        with open("Store.txt", "a") as file:
            file.write(f"name Product : {name_commodity}\n price : {price}$\n discount : {discount}%\n price_discount : {price_discount}$\n price with discount : {price_with_discount}$\n")
        
        masage = input("for Continue click << enter >> \n for Bookkeeping print << + >> ➗\n  for lave print << exit >>\n: ").replace(" ", "").lower()
        
    
        if masage == "exit":
            print("god bay😘")
            break
        
        if len(masage) == 0:
            continue
        
        
        elif masage == "+":
            
            num1 = int(input("enter number: "))
            op = input("<< + , - , * , / >> :").replace(" ","")
            num2 = int(input("enter number: "))
            result = 0
            
            if op == "+":
                result = num1 + num2
                print(result)
            elif op == "-":
                result = num1 - num2
                print(result)
            elif op == "*":
                result = num1 * num2
                print(result)
            elif op == "/":
                result = num1 / num2
                print(result)

            mas = input("for Continue click << enter >> ")
            if len(mas) == 0:
                continue
        
        
