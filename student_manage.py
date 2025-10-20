
mathematics = []
experimental_sciences = []
humanities = []
mathematics.sort()
experimental_sciences.sort()
humanities.sort()


while True:
    try:
        
        print("mathematics = A")
        print("experimental sciences = B")
        print("humanities = C")
        field = input("<<exit>> Enter field (A,B,C): ").upper().replace(" ","")
        
        if field == "EXIT":
            print("God Bay😘")
            break
        
        
    except TypeError:
        print("Please answer carefully")
        continue
    
    try:
        if field == "A":
            name_student = input("<<exit>> Enter student name: ").title()
            base_student = int(input("(10,11,12): "))
            gpa = input("student GPA: ")
            
            mathematics.append(name_student)
            show_list = input("for show student clik Enter < for skip print s >")
            if len(show_list) == 0:
                print(*mathematics, sep=" - ")
            
            if base_student == 10:
                with open("mathematics_10.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 11:
                with open("mathematics_11.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 12:
                with open("mathematics_12.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if name_student == "Exit":
                print("God Bay😘")
                break
    
    except TypeError:
        print("Please answer carefully")
        continue
    
    try:
        if field == "B":
            name_student = input("<<exit>> Enter student name: ").title()
            base_student = int(input("(10,11,12): "))
            gpa = input("student GPA: ")
            
            experimental_sciences.append(name_student)
            show_list = input("for show student clik Enter < for skip print s >")
            if len(show_list) == 0:
                print(*experimental_sciences, sep=" - ")
                
            if base_student == 10:
                with open("experimental_sciences_10.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 11:
                with open("experimental_sciences_11.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 12:
                with open("experimental_sciences_12.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if name_student == "Exit":
                print("God Bay😘")
                break
            
    except TypeError:
        print("Please answer carefully")
        continue
    
    try:
        if field == "C":
            name_student = input("<<exit>> Enter student name: ").title()
            base_student = int(input("(10,11,12): "))
            gpa = input("student GPA: ")
            
            humanities.append(name_student)
            show_list = input("for show student clik Enter < for skip print s >")
            if len(show_list) == 0:
                print(*humanities, sep=" - ")
                
            if base_student == 10:
                with open("humanities_10.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 11:
                with open("humanities_11.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if base_student == 12:
                with open("humanities_12.txt", "a") as file:
                    file.write(f"name : {name_student}\n GPA : {gpa}\n")
                    
            if name_student == "Exit":
                print("God Bay😘")
                break
                    
    except TypeError:
        print("Please answer carefully")
        continue