price=100
qty=500
amount=price*qty
if amount<1000:
    print("this yours:")
    amount=price*qty
elif amount>5000:
    print("no this very costly")
    amount=price*qty

else:
    print("you got this at:",amount)
