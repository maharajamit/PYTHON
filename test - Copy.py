price=int(input("enter the price of donut:rs."))
quantity=int(input("enter the no.of donuts:"))
amount=price*quantity
if amount>1000:
    print("ya a discount of 10% is applicable")
    discount=amount*10/100
    amount=amount-discount
else:
    print("a discount of 5% i applicable")
    discount=amount*5/100
    amount=amount-discount

print("your total amount is :rs." ,amount)


