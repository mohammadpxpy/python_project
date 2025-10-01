#password
import string
import time

print("welcom😍")

while True:
    
    system = input("for sign up print << sign up >> \n for Login print << login >> \n :")
    
    if system == "sign up":
        user_name = input("<< exit >> plase Enter name: ")
        pasword = input("<< exit >> plase Enter password: ")
        point = 0
        status = ["❌","❌","❌","❌"]
        print("plase wait!")
        time.sleep(2)
        
        if user_name == "exit" or pasword == "exit":
            print("come again🤗")
            break
        
        if len(pasword) >= 8:
            point += 1
            status.insert(0,"✔")
            status.pop()
            
        number = ["0","1","2","3","4","5","6","7","8","9"]
        lambda_1 = list(map(lambda x: x in pasword,number))
        if any(lambda_1):
            point += 1
            status.insert(1,"✔")
            status.pop()
            
        list_str = list(string.ascii_uppercase)
        lambda_2 = list(map(lambda x: x in pasword,list_str))
        if any(lambda_2):
            point += 1
            status.insert(2,"✔")
            status.pop()
            
        list_special = ["@","&","/",";","#","_"]
        lambda_3 = list(map(lambda x: x in pasword,list_special))
        if any(lambda_3):
            point += 1
            status.insert(3,"✔")
            status.pop()
            
        percent = (point / 4) * 100
        if percent >= 75:
            print("well done🤖, welcome")
            print("status password: ", *status)
            with open(r"password.txt" , "a") as file:
                file.write(f"{user_name} : {pasword} \n")

        else:
            print("status password: ", *status)
            print("try again👀")
            continue


                    




                    