price=105.50
qty=36
amount=price*qty

if amount>10000:
	print("yes 10% discount is applicable")
	discount=amount*10/100
	amount=amount-discount
else:
        if amount>5000:
                print("discount of 5% is applicable")
                discount=amount*5/100
                amount=amount-discount
        else:
                if amount>2000:
                        print("discount of 2% is applicable")
                        discount=amount*2/100
                        amount=amount-discount

                else:
                        if amount>1000:
                        print("No discount is applicable")
                        discount=amount*/100
                        amount=amount-discount
        
print("your total payable amount is :Rs",amount)
