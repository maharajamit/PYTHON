price=200
qty=15
amount=price*qty

if amount>5000:
    print("this is yours")
    amount=price*qty

else:
    if amount>500:
        print("this is not for you")
        amount=price*qty

        print("your total payable amount is:",amount)
        
