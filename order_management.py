def manu():
    print("""========== ORDER MANAGER ==========
        1. Create order 
        2. Show all orders
        3. Find order by id
        4. Close order
        5. Show sales report
        0. Exit
        Choose option:"""
        )
            
      
def enter_manu():
    while True:
        try:
            numbr_manu =int(input("enter the menu 0-5 :"))
            manu_num=0
            if numbr_manu >5 or numbr_manu < 0:
                print("please enter numbers 0-5 !")
                continue
            else:
                manu_num = numbr_manu
                return manu_num
        except: ValueError("Enter a value that is not int")
        print("Please enter numbers")

   
products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]
      
def create_order(products,id_product):
    try:
        while True:
            id_product=0
            enter_id=int(input("Please enter the number a id :"))
            for id_p in products:
                if id_p["id"]==enter_id:
                    id_product ==enter_id
                    print("The product is in stock.")   
                    return id_product
                            
            else:
                print("id is not Exists")
    except:ValueError("Enter a value that is not int")



def Show_all_orders():
    pass

def find_order_by_id():
    pass

def close_order():
    pass

def show_sales_report():
    pass

def  exit():
    pass



while True:
    manu()
    menu_selection=enter_manu()

    if menu_selection==1:
        create_order(products,["id"])

    elif menu_selection==2:
        Show_all_orders()

    elif menu_selection==3:
        find_order_by_id()

    elif menu_selection==4:
        close_order()

    elif menu_selection==5:
        show_sales_report()

    elif menu_selection==0:
        exit()

        break



