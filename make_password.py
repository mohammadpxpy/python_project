import string
import random
import time
import pyperclip

str_list_upper = list(string.ascii_uppercase)
str_list_lower = list(string.ascii_lowercase)
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
other_list = ["!", "@", "#", "&", "$", "(", ")"]

ascii_list = list(string.punctuation)

while True:
    user = input("for start click < Enter >")
    
    try:
        if len(user) == 0:
            len_password_user = int(input("Number of characters in the password (( 7 <=  number <= 10 )): "))
            len_passsword = len_password_user
            
            if len_passsword < 7 or len_passsword > 10:
                print("choise true number")
                continue

        loading = "LOADING.."
        for i in range(len(loading)):
            print(loading[i], end=" ")
            time.sleep(0.5)
            
        
        str_upper = random.choice(str_list_upper)
        str_lower = random.choice(str_list_lower)
        choise_number_list = random.choice(number_list)
        choise_other_list = random.choice(other_list)
        
        list_pas = []
        list_pas.append(str_lower)
        list_pas.append(str_upper)
        list_pas.append(choise_number_list)
        list_pas.append(choise_other_list)
        list_pas.append(str_upper)
        list_pas.append(choise_number_list)
        list_pas.append(choise_other_list)
        list_pas.append(str_upper)
        list_pas.append(choise_other_list)
        list_pas.append(str_lower)
        
        result = list_pas[:len_passsword]
        result = "".join(result)
        print("\n",result)
    
    except ValueError:
        print("plase enter just number")
        continue
    
    try_again = input("<< exit >> for try again print << again >> \n for copy print << copy >> \n :")
    if try_again == "again":
        continue
    
    if try_again == "copy":
        pyperclip.copy(result)
        print("copy✔")
        break
    
    if try_again == "exit":
        print("god bay🌹")
        break
    
    
    
    