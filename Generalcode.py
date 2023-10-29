import PySimpleGUI as gui
import time 
import mysql.connector as c
cnc = c.connect(user= "root", host="localhost", password="password", database="project")
if cnc.is_connected():
    print("Connected to DB")
cur = cnc.cursor()


def gui_propmt2():

    #MAIN THINGS
    # data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    cur.execute("SELECT * FROM ITEMTEST ORDER BY ID;")
    data = cur.fetchall()   
    
    price2 = []
    infotablegetinfo = []
    infotablebill = []
    infotablestockadd = []
    infotablestockupd = []
    infotablestockdel = []
    infotablelistitems = []
    head = ['ID','Product Name','Quantity','Price']
    price1 = 0

    # Theme
    gui.theme("DarkAmber")

    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout_menu = [ [gui.Text("!!Welcome To Mavika store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                    [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                    [gui.Button("Get Information"), gui.Button("List all Items"), gui.Button("BILL"), gui.Button("Admin Login"), gui.Button("Exit")]
    ]


    #GET INFORMATION 
    layout_getinfo = [ [gui.Text("Welcome to Get Information", expand_x = "True", justification = "centre")],
                       [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ITEMID", do_not_clear = False)],
                       [gui.Text("Enter Item Name", size = (12,1)), gui.Input(key = "ITEMNAME", do_not_clear = False)],
                       [gui.Button("Search")],
                       [gui.Table(values =  infotablegetinfo, headings = head, key = "infotablegetinfo", justification = "centre")],
                       [gui.Button("Back", key = "back_getinfo")]
    ]
   
    #ADMIN LOGIN
    layout_adminlogin = [ [gui.Text("Welcome to Admin Login", expand_x = "True", justification = "centre")],
                          [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "NAME", do_not_clear = False)],
                          [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "PASSWORD", do_not_clear = False)],
                          [gui.Button("Enter"), gui.Button("Back", key = "back_login")]
    ]

    #UNDER ADMIN LOGIN - "ADMIN CHANGES"
    layout_admin = [ [gui.Text("Welcome to Admin Updation", expand_x = "True", justification = "centre")],
                     [gui.Text("Select your Choice (Admin Changes)")],[gui.Listbox(values = ['New Admin', 'Update Admin', 'Delete Admin'], key = "adminupdation", select_mode = "single"],
                     [gui.Text("Select your Choice (Stock Changes)")],[gui.Listbox(values = ['Add', 'Update', 'Delete'], key = "stockchanges", select_mode = "single"],
                     [gui.Button("Back", key = "back_admin")]
    ]
    
    #UNDER ADMIN LOGIN - "admin CHANGES"
    #UNDER admin CHANGES - "ADD" "UPDATE" "DELETE" separate
    layout_adminnew = [ [gui.Text("Welcome to Admin (ADD)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ADDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Quantity", size = (12,1)), gui.Input(key = "ADDQTY", do_not_clear = False)],
                        [gui.Table(values =  infotablestockadd, headings = head, key = "tablestockadd", justification = "centre")],
                        [gui.Button("Change", key = "add_stock")], [gui.Button("Back", key = "back_stockadd")]
    ]

    layout_adminupd = [ [gui.Text("Welcome to Admin (UPDATION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "UPDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Prize", size = (12,1)), gui.Input(key = "UPDPRIZE", do_not_clear = False)],
                        [gui.Table(values =  infotablestockupd, headings = head, key = "tablestockupd", justification = "centre")],
                        [gui.Button("Change", key = "upd_stock")], [gui.Button("Back", key = "back_stockupd")]
    ]

    layout_admindel = [ [gui.Text("Welcome to Admin (DELETION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID to Delete", size = (12,1)), gui.Input(key = "DELITEMID", do_not_clear = False)],
                        [gui.Table(values =  infotablestockdel, headings = head, key = "tablestockdel", justification = "centre")],
                        [gui.Button("Change", key = "del_stock")], [gui.Button("Back", key = "back_stockdel")]
    ]
    

    #UNDER ADMIN LOGIN - "STOCK CHANGES"
    #UNDER STOCK CHANGES - "ADD" "UPDATE" "DELETE" separate
    layout_stockadd = [ [gui.Text("Welcome to Stock (ADD)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ADDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Quantity", size = (12,1)), gui.Input(key = "ADDQTY", do_not_clear = False)],
                        [gui.Table(values =  infotablestockadd, headings = head, key = "tablestockadd", justification = "centre")],
                        [gui.Button("Change", key = "add_stock")], [gui.Button("Back", key = "back_stockadd")]
    ]

    layout_stockupd = [ [gui.Text("Welcome to Stock (UPDATION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "UPDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Prize", size = (12,1)), gui.Input(key = "UPDPRIZE", do_not_clear = False)],
                        [gui.Table(values =  infotablestockupd, headings = head, key = "tablestockupd", justification = "centre")],
                        [gui.Button("Change", key = "upd_stock")], [gui.Button("Back", key = "back_stockupd")]
    ]

    layout_stockdel = [ [gui.Text("Welcome to Stock (DELETION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID to Delete", size = (12,1)), gui.Input(key = "DELITEMID", do_not_clear = False)],
                        [gui.Table(values =  infotablestockdel, headings = head, key = "tablestockdel", justification = "centre")],
                        [gui.Button("Change", key = "del_stock")], [gui.Button("Back", key = "back_stockdel")]
    ]

  
    #MAKE BILL
    layout_BILL = [ [gui.Text("Welcome to BILL", expand_x = "True", justification = "centre")],
                    [gui.Button("Previous Bills", key = "prevbill")], [gui.Button("Make Bill", key = "make_bill")],
                    [gui.Button("Back", key = "back_bill")]
    ]

    #UNDER BILL =PREV BILLS=
    layout_prevbill = [ [gui.Text("Welcome to Previous Bills", expand_x = "True", justification = "centre")],
                        [gui.Button("Back", key = "back_prevbill")]
    ]
    #UNDER BILL ==MAKE BILL==
    layout_makebill = [ [gui.Text("Welcome to Make Bill", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False, justification = "left")],
                        [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False, justification = "left")],
                        [gui.Button("Add")],
                        [gui.Table(values =  infotablebill, headings = head, key = "tablebill", justification = "centre")],
                        [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
                        [gui.Button("Back", key = "back_makebill")] 
    ]      

    #LIST ALL ITEMS 
    layout_listitems = [ [gui.Text("Welcome to All Items", expand_x = "True", justification = "centre")],
                         [gui.Table(values =  infotablelistitems, headings = head, key = "tableitems", justification = "centre")],
                         [gui.Button("Back", key = "back_allitems")]
    ]

    #MAIN LAYOUT
    layout = [ [gui.Column(layout_menu, key = "l_menu"),
                gui.Column(layout_getinfo, key = "l_getinfo", visible = False),
                gui.Column(layout_adminlogin, key = "l_adminlogin", visible = False),
                gui.Column(layout_admin, key = "l_admin", visible = False),
                gui.Column(layout_adminnew, key = "l_adminnew", visible = False),
                gui.Column(layout_adminupd, key = "l_adminupd", visible = False),
                gui.Column(layout_admindel, key = "l_admindel", visible = False),
                gui.Column(layout_stockadd, key = "l_stockadd", visible = False),
                gui.Column(layout_stockupd, key = "l_stockupd", visible = False),
                gui.Column(layout_stockdel, key = "l_stockdel", visible = False),
                gui.Column(layout_bill, key = "l_bill", visible = False),
                gui.Column(layout_prevbill, key = "l_prevbill", visible = False),
                gui.Column(layout_makebill, key = "l_makebill", visible = False),
                gui.Column(layout_listitems, key = "l_listitems", visible = False)]
    ]

    # WINDOW
    window = gui.Window("Mavika Store", layout, resizable = True)


    #while-event loop
    while True:
        event, values = window.read()

        if event in (gui.WIN_CLOSED, "Exit"):
            break

        
        # Get Info starts
        if event == "Get Information":
            window["l_getinfo"].update(visible = True)
            window["l_menu"].update(visible = False)


        if event == "Search" and values["ITEMID"] == '' and values["ITEMNAME"] == '':
            gui.Popup("Please Enter ID and NAME")


        if event == "Search" and values["ITEMID"] != '' and values["ITEMNAME"] != '':
            gi = values["ITEMID"]
            cur.execute(f"SELECT * FROM ITEMTEST WHERE VALUE = {gi}")
            item = cur.fetchone()
            infotablegetinfo.append([item[0], item[1],item[2],item[3]])
            window["tablegetinfo"].update(values = infotablegetinfo)

        if event == "back_getinfo":
            window["l_menu"].update(visible = True)
            window["l_getinfo"].update(visible = False)
        # Get Info ends
        

        
        # Admin start
        if event == "Admin Login":
            window["l_adminlogin"].update(visible = True)
            window["l_menu"].update(visible = False)
       
        if event == "back_login":
            window["l_menu"].update(visible = True)
            window["l_adminlogin"].update(visible = False)

        #==(FOR ENTRY)==
        if event == "Enter":
            name = ["vinay", "kalpit", "mathew"]
            password = ["ayo", "akhila123", "yo"]
            if values["NAME"] in name and values["PASSWORD"] in password:
                 window["l_admin"].update(visible = True)
                 window["l_adminlogin"].update(visible = False)
                
            else:
                 gui.Popup("YOU'RE NOT AUTHORISED PERSONNEl!!!")
        
        if event == "back_admin":
            window["l_menu"].update(visible = True)
            window["l_admin"].update(visible = False)

        # =admin changes =
        if values["stockchanges"] == "Add":
            window["l_stockadd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            ad = values["ADDITEMID"]
            cur.execute(f"UPDATE TABLE ITEMTEST VALUES {ad}")
            item = cur.fetchone()
            infotablestockadd.append([item[0], item[1],item[2],item[3]])
            window["tablestockadd"].update(values = infotablestockadd)

        if event == "back_stockadd":
            window["l_stock"].update(visible = True)
            window["l_stockadd"].update(visible = False)

        if values["stockchanges"] == "Update":
            window["l_stockupd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            upd = values["UPDITEMID"]
            cur.execute(f"UPDATE TABLE ITEMTEST WHERE VALUE = {upd}")
            item = cur.fetchone()
            infotablestockupd.append([item[0], item[1],item[2],item[3]])
            window["tablestockupd"].update(values = infotablestockupd)

        if event == "back_stockupd":
            window["l_stock"].update(visible = True)
            window["l_stockupd"].update(visible = False)

        if values["stockchanges"] == "Delete":
            window["l_stockdel"].update(visible = True)
            window["l_stock"].update(visible = False)

            d = values["DELITEMID"]
            cur.execute(f"DELETE FROM TABLE ITEMTEST VALUES {d}")
            item = cur.fetchone()
            infotablestockdel.append([item[0], item[1],item[2],item[3]])
            window["tablestockdel"].update(values = infotablestockdel)

        if event == "back_stockdel":
            window["l_stock"].update(visible = True)
            window["l_stockdel"].update(visible = False)
            
        #==stock changes==
        if values["stockchanges"] == "Add":
            window["l_stockadd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            ad = values["ADDITEMID"]
            cur.execute(f"UPDATE TABLE ITEMTEST VALUES {ad}")
            item = cur.fetchone()
            infotablestockadd.append([item[0], item[1],item[2],item[3]])
            window["tablestockadd"].update(values = infotablestockadd)

        if event == "back_stockadd":
            window["l_stock"].update(visible = True)
            window["l_stockadd"].update(visible = False)

        if values["stockchanges"] == "Update":
            window["l_stockupd"].update(visible = True)
            window["l_stock"].update(visible = False)
            
            upd = values["UPDITEMID"]
            cur.execute(f"UPDATE TABLE ITEMTEST WHERE VALUE = {upd}")
            item = cur.fetchone()
            infotablestockupd.append([item[0], item[1],item[2],item[3]])
            window["tablestockupd"].update(values = infotablestockupd)

        if event == "back_stockupd":
            window["l_stock"].update(visible = True)
            window["l_stockupd"].update(visible = False)

        if values["stockchanges"] == "Delete":
            window["l_stockdel"].update(visible = True)
            window["l_stock"].update(visible = False)

            d = values["DELITEMID"]
            cur.execute(f"DELETE FROM TABLE ITEMTEST VALUES {d}")
            item = cur.fetchone()
            infotablestockdel.append([item[0], item[1],item[2],item[3]])
            window["tablestockdel"].update(values = infotablestockdel)

        if event == "back_stockdel":
            window["l_stock"].update(visible = True)
            window["l_stockdel"].update(visible = False)
        # Admin end



        # Bill
        if event == "BILL":
            window["l_bill"].update(visible = True)
            window["l_menu"].update(visible = False)

        if event == "back_bill":
             window["l_menu"].update(visible = True)
             window["l_bill"].update(visible = False)

        #=prev bills=
        if event == "prev_bill":
            window["l_prevbills"].update(visible = True)
            window["l_bill"].update(visible = False)
            
        # some sql code which'll show prev bills... in what way 
        # will it show..?.. 
        
        if event == "back_prevbill":
             window["l_bill"].update(visible = True)
             window["l_prevbill"].update(visible = False)
            

        #==make bill==
        if event == "make_bill":
            window["l_makebill"].update(visible = True)
            window["l_bill"].update(visible = False)
            
        if event == "back_makebill":
             window["l_bill"].update(visible = True)
             window["l_makebill"].update(visible = False)
            
             
        if event == "Add" and values["ID"] == '' and values["QTY"] == '':
            gui.Popup("Please Enter ID and QUANTITY")


        if event == "Add" and values["ID"] != '' and values["QTY"] != '':
            
            # data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            i = values["ID"];
            cur.execute(f"SELECT * FROM ITEMTEST WHERE ID={i}")
            item = cur.fetchone()
            price1 = int(values["QTY"])*int(item[2])
            infotablebill.append([i, item[1],values["QTY"],price1])
            price2.append(price1)
            window["tablebill"].update(values = infotablebill)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)
        #^Bill^ end

        

        #List all Items starts
        if event == "List all Items":
            window["l_listitems"].update(visible = True)
            window["l_menu"].update(visible = False)

            cur.execute(f"SELECT * FROM ITEMTEST")
            item = cur.fetchone()
            infotablelistitems.append([item[0], item[1],item[2],item[3]])
            window["tableitems"].update(values = infotableitems)
            #sql backend code?
        
            
        if event == "back_allitems":
             window["l_menu"].update(visible = True)
             window["l_listitems"].update(visible = False)
        #Items end
    
    window.close()
gui_prompt2()
