
print("""

 **    Welcome to the Snakes Cafe!   **
 **     Please see our menu below.   **
 **
 ** To quit at any time, type "quit" **
**************************************
 Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************  

""")

menu = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
orders =[] 

while True:
    yourPicks =str(input('>'))
    
    if yourPicks in menu:
        orders.append(yourPicks)
        counts =orders.count(yourPicks)

        print(f"**{counts} orders of {yourPicks} has been added to your list")
        print('would you like to counte order or type exit to quit')
    elif yourPicks =='quit':
        print('please wait for your order to get ready for you')
        break
    else:
        print(f'**am sorry but we dont have {yourPicks} in the menu')
