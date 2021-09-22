original_price=int(input("enter the price:"))
rate_of_discount= 0.10
discount=original_price*rate_of_discount
if original_price>=1000:
    print("you will get a 10% discount on the original price",discount)
    print("average bill",original_price-discount)
else:
    print("there will be no discount on the original price",original_price)
