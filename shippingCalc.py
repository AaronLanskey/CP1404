""""A shipping company requires a small program that would allow them to quickly work out total shipping charge
for a number of items, each with different prices.
The program allows the user to enter the number of items and the shipping cost for each different item.
Then the program computes and displays the total shipping cost.
If the total shipping cost is over $100, then a 10% discount is applied to the total shipping cost before the
amount is displayed on the screen."""""

number_items = 0
total_price = 0
while number_items >= 0:
    number_items = int(input("How many items are being shipped?:   "))
    print("Number of items", number_items)

    for i in range(1, number_items+1):
        price = int(input("Price of Item {}:   ".format(i)))
        total_price += price
    if total_price >= 100:
        total_price -= total_price * 0.1
        print("Total Price is:    ", total_price)
    else:
        print("Total Price is:    ", total_price)
