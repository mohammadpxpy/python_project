import datetime

while True:
    user = input(" for to calculate  live print << live >>\n for brithday print << BTH >>\n :").lower().replace(" ","")

    if user == "live":
        yaer = int(input("yaer brithday:"))
        month = int(input("month brithday:"))
        day = int(input("day brithday:"))
        
        datetime_now = datetime.datetime.now()
        live_user = datetime.datetime(yaer, month, day)
        
        finish = datetime_now - live_user
        print("your alive => ", finish)
        continue
    
    elif user == "bth":
        month = int(input("month: "))
        day = int(input("day: "))
        
        datetime_now = datetime.datetime.now()
        bth = datetime.datetime(2025, month, day)
        
        finish = datetime_now - bth
        print("remainder => ", finish)
        continue
