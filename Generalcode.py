import PySimpleGUI as gui
import mysql.connector as c
cnc = c.connect(user= "root", host="localhost", password="password", database="project")
if cnc.is_connected():
    print("Connected to DB")
cur = cnc.cursor()


def gui_propmt2():

    #MAIN THINGS
    #from PIL import Image
    # data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    cur.execute("SELECT * FROM ITEMTEST ORDER BY ID;")
    data = cur.fetchall()   
    #supdation = ['Add', 'Update', 'Delete']
    price2 = []
    infotable = []
    head = ['ID','Product Name','Quantity','Price']
    price1 = 0
    
    gui.theme("DarkAmber")

    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout_menu = [ [gui.Text("!!Welcome To Mavika store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                    [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                    [gui.Button("Get Information"), gui.Button("List all Items"), gui.Button("Make BILL"), gui.Button("Admin Login"), gui.Button("Exit")]
    ]


    #GET INFORMATION 
    layout_getinfo = [ [gui.Text("Welcome to Get Information", expand_x = "True", justification = "centre")],
                       [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ITEMID", do_not_clear = False)],
                       [gui.Text("Enter Item Name", size = (12,1)), gui.Input(key = "ITEMNAME", do_not_clear = False)],
                       [gui.Button("Search")],
                       [gui.Table(values =  data, headings = head, key = "infotable", justification = "centre")],
                       [gui.Button("Back", key = "back_getinfo")]
    ]

   
    #ADMIN LOGIN
    layout_adminlogin = [ [gui.Text("Welcome to Admin Login", expand_x = "True", justification = "centre")],
                          [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "NAME", do_not_clear = False)],
                          [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "PASSWORD", do_not_clear = False)],
                          [gui.Button("Enter"), gui.Button("Back", key = "back_login")]
    ]

   
    #UNDER ADMIN LOGIN - "STOCK UPDATION"
    layout_stock = [ [gui.Text("Welcome to Stock Updation", expand_x = "True", justification = "centre")],
                     [gui.Text("Select your Choice")],[gui.Listbox(values = ['Add', 'Update', 'Delete'], key = "stockupdation", select_mode = "single"],
                     [gui.Button("Back", key = "back_stock")]
   ]


    #UNDER STOCK UPDATION - "ADD" "UPDATE" "DELETE" separate
    layout_stockadd = [
        
    ]

    layout_stockupd = [
        
    ]

    layout_stockdel = [
        
    ]

  
    #MAKE BILL
    layout_bill = [ [gui.Text("Welcome to Bill", expand_x = "True", justification = "centre")],
                    [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False, justification = "left")],
                    [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False, justification = "left")],
                    [gui.Button("Add")],
                    [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
                    [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
                    [gui.Button("Back", key = "back_bill")] 
    ]      

    #LIST ALL ITEMS 
    layout_listitems = [ [gui.Text("Welcome to All Items", expand_x = "True", justification = "centre")],
                         [gui.Table(values =  data, headings = head, key = "tableitems", justification = "centre")],
                         [gui.Button("Back", key = "back_allitems")]
    ]

    #MAIN LAYOUT
    layout = [ [gui.Column(layout_menu, key = "l_menu"),
                gui.Column(layout_getinfo, key = "l_getinfo", visible = False),
                gui.Column(layout_adminlogin, key = "l_adminlogin", visible = False),
                gui.Column(layout_stock, key = "l_stock", visible = False),
                gui.Column(layout_stockadd, key = "l_stockadd", visible = False),
                gui.Column(layout_stockupd, key = "l_stockupd", visible = False),
                gui.Column(layout_stockdel, key = "l_stockdel", visible = False),
                gui.Column(layout_bill, key = "l_bill", visible = False),
                gui.Column(layout_listitems, key = "l_listitems", visible = False)]
    ]

    # WINDOW
    window = gui.Window("Mavika Store", layout, resizable = True)


    #while-event loop
    while True:
        event, values = window.read()

        if event in (gui.WIN_CLOSED, "Exit"):
            break
       
        #Get Info starts
        if event == "Get Information":
            window["l_getinfo"].update(visible = True)
            window["l_menu"].update(visible = False)


        if event == "Search" and values["ITEMID"] == '' and values["ITEMNAME"] == '':
            gui.Popup("Please Enter ID and NAME")


        if event == "Search" and values["ITEMID"] != '' and values["ITEMNAME"] != '':
            # mathew's code from make bILL
            print("")


        if event == "back_getinfo":
            window["l_menu"].update(visible = True)
            window["l_getinfo"].update(visible = False)
        
        #Get Info ends
        

        # Admin start
        if event == "Admin Login":
            window["l_adminlogin"].update(visible = True)
            window["l_menu"].update(visible = False)
        if event == "back_login":
            window["l_menu"].update(visible = True)
            window["l_adminlogin"].update(visible = False)

        #stock updation (FOR ENTRY)
        if event == "Enter":
            name = ["vinay", "kalpit", "mathew"]
            password = ["ayo", "akhila123", "yo"]
            if values["NAME"] in name and values["PASSWORD"] in password:
                window["l_stock"].update(visible = True)
                window["l_adminlogin"].update(visible = False)
                
            else:
                gui.Popup("YOU'RE NOT AUTHORISED PERSONNEl!!!")

        #stock updation
        if values["stockupdation"] == "Add":
            window["l_stockadd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            #mathews sql backend

        if event == "back_stockadd":
            window["l_stock"].update(visible = True)
            window["l_stockadd"].update(visible = False)
            pass

        if values["stockupdation"] == "Update":
            window["l_stockupd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            #mathews sql backend

        if event == "back_stockupd":
            window["l_stock"].update(visible = True)
            window["l_stockupd"].update(visible = False)
            pass

        if values["stockupdation"] == "Delete":
            window["l_stockdel"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            #mathews sql backend

        if event == "back_stockdel":
            window["l_stock"].update(visible = True)
            window["l_stockdel"].update(visible = False)
            pass

        
        if event == "back_stock":
            window["l_menu"].update(visible = True)
            window["l_stock"].update(visible = False)
        # Admin end



        # Bill
        if event == "Make BILL":
            window["l_bill"].update(visible = True)
            window["l_menu"].update(visible = False)

        if event == "back_bill":
             window["l_menu"].update(visible = True)
             window["l_bill"].update(visible = False)

             
        if event == "Add" and values["ID"] == '' and values["QTY"] == '':
            gui.Popup("Please Enter ID and QUANTITY")


        if event == "Add" and values["ID"] != '' and values["QTY"] != '':

            #** mathews code from school make bill** change the below
            # data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            i = values["ID"];
            cur.execute(f"SELECT * FROM ITEMTEST WHERE ID={i}")
            item = cur.fetchone()
            price1 = int(values["QTY"])*int(item[2])
            infotable.append([i, item[1],values["QTY"],price1])
            price2.append(price1)
            window["tablebill"].update(values = infotable)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)
        #^Bill^ end


        #Items starts
        if event == "List all Items":
            window["l_listitems"].update(visible = True)
            window["l_menu"].update(visible = False)

            cur.execute(f"SELECT * FROM ITEMTEST")
            item = cur.fetchone()
            infotable.append([item[0], item[1],item[2],item[3]])
            window["tableitems"].update(values = infotable)
            #sql backend code?
        
            
        if event == "back_allitems":
             window["l_menu"].update(visible = True)
             window["l_listitems"].update(visible = False)
        #Items end
    window.close()
gui_prompt2()
