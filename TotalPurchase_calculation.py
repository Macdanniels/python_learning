#Total Purchase calculation
tax = 7/100
price1 = float(input('Price of item 1:    '))
price2 = float(input('Price of item 2:    '))
price3 = float(input('Price of item 3:    '))
price4 = float(input('Price of item 4:    '))
price5 = float(input('Price of item 5:    '))
price6 = float(input('Price of item 6:    '))
subtotal = (price1+price2+price3+price4+price5+price6)
#displays the subtotal of the sale
#the amount of sales tax, and the total. 
#Assume the sales tax is 7 percent
print('tax on item 1 price is: ', tax * price1)
print('tax on item 2 price is: ', tax * price2)
print('tax on item 3 price is: ', tax * price3)
print('tax on item 4 price is: ', tax * price4)
print('tax on item 5 price is: ', tax * price5)
print('tax on item 6 price is: ', tax * price6)
tprice1=((tax*price1)+price1)
tprice2=((tax*price2)+price2)
tprice3=((tax*price3)+price3)
tprice4=((tax*price4)+price4)
tprice5=((tax*price5)+price5)
tprice6=((tax*price6)+price6)

#total sales

total =(tprice1+tprice2+tprice3+tprice4+tprice5+tprice6)

totalsale_on_tax = ((tax*price1)+(tax*price2)+(tax*price3)+(tax*price4)+(tax*price5)+(tax*price6))
print('The total tax of each item ', totalsale_on_tax)
print('Total prices of the 6 items', subtotal)
print('Total Sale of the 6 items', total)




