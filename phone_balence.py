phone_balence=int(input())
if phone_balence>=0:
    if phone_balence <=30:
        print("you need recharge immediately")
    elif phone_balence>30 and phone_balence<=60:
        print("you need to recharge soon")
    elif phone_balence>60 and phone_balence<=100:
        print("you can recharge when you are want")
    elif phone_balence>=100:
        print("you can no need to recharge")
    else:
        print(phone_balence)
else:
    print("Invalid Amount")
