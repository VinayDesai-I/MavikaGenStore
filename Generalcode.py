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

import PySimpleGUI as gui
import pymysql as c
cnc = c.connect(host="localhost", user= "root", passwd="1234", database="vinayproject2")

print(cnc)

cur = cnc.cursor()

def gui_propmt2():

    price2 = []
    info_table_ugetinfo = []
    info_table_aiteminfo = []
    info_table_bill = []
    info_table_billhist = []
    info_table_delbill = []
    info_table_stockadd = []
    info_table_stockupd = []
    info_table_stockdel = []
    info_table_listitems = []
    info_table_alistitems = []
    head = ['ID','Item Name','Units','Price']
    head1 = ['ID','Item Name','In-Stock(Units)','Price','Date']
    headt = ['ID','Item Name','In-Stock(Units)','Price']
    head2 = ['Customer Name','Phone No.','Address']
    head3 = ['Customer Name','Items','Total Units','Total Price','Delivery']
    price1 = 0
    Q = 0
    titems = " "
    
    # Theme
    gui.theme("DarkAmber")
    
    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout_menu = [ [gui.Text("!!Welcome To General Store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                    [gui.Image(filename = "gen.png", size = (275, 183),  expand_x = True, expand_y = True)],
                    [gui.Column([[gui.Button("User"), gui.Button("Admin")]], element_justification = "centre", expand_x = "True")]
    ]
    
    #USER LOGIN
    layout_userlogin = [ [gui.Text("User Login Window", expand_x = "True", justification = "centre")],
                         [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "username", do_not_clear = False)],
                         [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "userpassword", do_not_clear = False)],
                         [gui.Button("Enter", key = "enter_userlogin"), gui.Button("Back", key = "back_userlogin"), gui.Push(), gui.Button("Register (New User)", key = "ureg")]
    ]

    #USER REGISTRATION 
    layout_userreg = [ [gui.Text("Welcome to User Registration", expand_x = "True", justification = "centre")],
                       [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "userregname", do_not_clear = False)],
                       [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "userregpassword", do_not_clear = False)],
                       [gui.Text("Enter Address", size = (12,1)), gui.Input(key = "useraddress", do_not_clear = False)],
                       [gui.Text("Enter Phone No.", size = (12,1)), gui.Input(key = "userno", do_not_clear = False)],
                       [gui.Button("Enter", key = "enter_userreg"), gui.Button("Back", key = "back_userreg")]
    ]

    #USER MENU 
    layout_usermenu = [ [gui.Text("!!Welcome To Mavika Store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                        [gui.Image(filename = "user.png", size = (150, 220),  expand_x = True, expand_y = True)],
                        [gui.Button("List Of Items"), gui.Button("Get Information"), gui.Button("Self Check-Out"), gui.Button("Back", key = "back_usermenu")]
    ]

    #USER GET INFORMATION 
    layout_getinfo = [ [gui.Text("Welcome to Get Information", expand_x = "True", justification = "centre")],
                       [gui.Text("Enter Item ID", size = (10,1)), gui.Input(key = "uITEMID", do_not_clear = False)],
                       [gui.Button("Search", key = "search_ugetinfo")],
                       [gui.Table(values =  info_table_ugetinfo, headings = head1, key = "tableugetinfo",
                                  justification = "centre", expand_x = "True", auto_size_columns = True)],
                       [gui.Button("Back", key = "back_ugetinfo")]
    ]

    #USER LIST of ITEMS 
    layout_listitems = [ [gui.Text("Welcome to List of Items", expand_x = "True", justification = "centre")],
                         [gui.Table(values =  info_table_listitems, headings = head1, key = "tableitems",
                                    justification = "centre", expand_x = "True", auto_size_columns = True)],
                         [gui.Button("Back", key = "back_listitems")]
    ]

    #USER SELF CHECKOUT 
    layout_selfcheckout = [ [gui.Text("Welcome to Self Check-Out", expand_x = "True", justification = "centre")],
                            [gui.Text("Enter ID", size = (16,1)), gui.Input(key = "id", do_not_clear = False, justification = "left", expand_x = "True")],
                            [gui.Text("Enter Quantity (Units)", size = (16,1)), gui.Input(key = "qty", do_not_clear = False, justification = "left")],
                            [gui.Button("Add")],
                            [gui.Table(values =  info_table_bill, headings = head, key = "tablebill",
                                       justification = "centre", expand_x = "True", auto_size_columns = True)],
                            [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
                            [gui.Button("Back", key = "back_selfcheckout"), gui.Button("Save", key = "savebill_selfcheckout"), gui.Button("Save-Place Delivery", key = "savedelivery_selfcheckout")],
                            [gui.Text("Change Address \n(OPTIONAL)", size = (16,2)), gui.Input(key = "delivery_change", do_not_clear = False, justification = "left")]
    ]

    #ADMIN LOGIN
    layout_adminlogin = [ [gui.Text("Admin Login", expand_x = "True", justification = "centre")],
                          [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "admname", do_not_clear = False)],
                          [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "admpassword", do_not_clear = False)],
                          [gui.Button("Enter", key = "enter_adminlogin"), gui.Button("Back", key = "back_adminlogin"), gui.Push(), gui.Button("Register (New User)", key = "areg")]
    ]
    
    #ADMIN REGISTRATION 
    layout_adminreg = [ [gui.Text("Admin Registration", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "admregname", do_not_clear = False)],
                        [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "admregpassword", do_not_clear = False)],
                        [gui.Text("Enter Code", size = (12,1)), gui.Input(key = "admregsec", do_not_clear = False)],
                        [gui.Button("Enter", key = "enter_admreg"), gui.Button("Back", key = "back_admreg")]
    ]

    #ADMIN MENU
    layout_adminmenu = [ [gui.Table(values =  info_table_alistitems, headings = head1, key = "tableitems1",
                                    justification = "centre", expand_x = "True", auto_size_columns = True)],
                         [gui.Column([[gui.Button("Item Information"), gui.Button("Restock Items"), gui.Button("Delivery"), gui.Button("Bills"), gui.Button("Back", key = "back_admmenu")]], element_justification = "centre", expand_x = "True")]
    ]
    
    #ITEM INFORMATION 
    layout_iteminfo = [ [gui.Text("Item Information", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (10,1)), gui.Input(key = "aITEMID", do_not_clear = False)],
                        [gui.Button("Search", key = "search_aiteminfo")],
                        [gui.Table(values =  info_table_aiteminfo, headings = head1, key = "tableaiteminfo",
                                   justification = "centre", auto_size_columns = True)],
                        [gui.Button("Back", key = "back_aiteminfo")]
    ]

    #RESTOCK
    layout_stockadd = [ [gui.Text("Add Stock (Item)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter New Item ID", size = (18,1)), gui.Input(key = "ADDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Item Name", size = (18,1)), gui.Input(key = "ADDITEMNAME", do_not_clear = False)],
                        [gui.Text("Enter New InStock(Units)", size = (18,1)), gui.Input(key = "ADDSTOCK", do_not_clear = False)],
                        [gui.Text("Enter Item Price(Rupees)", size = (18,1)), gui.Input(key = "ADDPRICE", do_not_clear = False)],
                        [gui.Text("Enter Item Manuf. Date", size = (18,1)), gui.Input(key = "ADDDATE", do_not_clear = False)],
                        [gui.Table(values =  info_table_stockadd, headings = head1, key = "tablestockadd",
                                   justification = "centre", expand_x = "True", auto_size_columns = True)],
                        [gui.Text("The Following Details Have Been Added", size = (30,1), key = "add", visible = False)],
                        [gui.Button("Add", key = "add_stock"), gui.Button("Back", key = "back_stockadd")]
    ]

    layout_stockupd = [ [gui.Text("Update Stock (Price)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (19,1)), gui.Input(key = "UPDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Quantity(Units)", size = (19,1)), gui.Input(key = "UPDQTY", do_not_clear = False)],
                        [gui.Text("Enter New Price(Rupees)", size = (19,1)), gui.Input(key = "UPDPRICE", do_not_clear = False)],
                        [gui.Table(values =  info_table_stockupd, headings = headt, key = "tablestockupd",
                                   justification = "centre", expand_x = "True", auto_size_columns = True, expand_y = "True")],
                        [gui.Text("The Following Details Have Been Updated", size = (20,1), key = "upd", visible = False)],
                        [gui.Button("Update", key = "upd_stock"), gui.Button("Back", key = "back_stockupd")]
    ]

    layout_stockdel = [ [gui.Text("Welcome to Stock (DELETION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID to DELETE", size = (19,1)), gui.Input(key = "DELITEMID", do_not_clear = False)],
                        [gui.Table(values =  info_table_stockdel, headings = head1, key = "tablestockdel",
                                   justification = "centre", expand_x = "True", auto_size_columns = True, expand_y = "True")],
                        [gui.Text("The Following Details Have Been Deleted", size = (20,1), key = "del", visible = False)],
                        [gui.Button("Delete", key = "del_stock"), gui.Button("Back", key = "back_stockdel")]
    ]

    #tab
    layout_tabrestock = [ [gui.TabGroup([[gui.Tab("ADD", layout_stockadd), 
                                                      gui.Tab("UPDATE", layout_stockupd),
                                                      gui.Tab("DELETE", layout_stockdel)]], tab_location = "centertop")]
    ]

    #DELIVERY
    layout_delivery = [ [gui.Text("Delivery", expand_x = "True", justification = "centre")],
                        [gui.Table(values =  info_table_delbill, headings = head2, key = "tabledel",
                                   justification = "centre", expand_x = "True", auto_size_columns = True)],
                        [gui.Text("+--If Delivery Made--+", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Customer's Name", size = (17,1)), gui.Input(key = "custname", do_not_clear = False)],
                        [gui.Push(), gui.Button("Delivery Made", key = "done_delivery")],
                        [gui.Button("Back", key = "back_delivery")]
    ]

    #BILLS
    layout_billhistory = [ [gui.Text("Bill History", expand_x = "True", justification = "centre")],
                           [gui.Table(values =  info_table_billhist, headings = head3, key = "tablebillhist",
                                      justification = "centre", expand_x = "True", auto_size_columns = True)],
                           [gui.Button("Back", key = "back_bill")] 
    ]

    #MAIN LAYOUT
    layout = [ [gui.Column(layout_menu, key = "l_menu"),
                gui.Column(layout_userlogin, key = "l_ulogin", visible = False),
                gui.Column(layout_userreg, key = "l_ureg", visible = False),
                gui.Column(layout_usermenu, key = "l_umenu", visible = False),      
                gui.Column(layout_getinfo, key = "l_getinfo", visible = False),
                gui.Column(layout_listitems, key = "l_listitems", visible = False),
                gui.Column(layout_selfcheckout, key = "l_scheckout", visible = False),
                gui.Column(layout_adminlogin, key = "l_alogin", visible = False),
                gui.Column(layout_adminreg, key = "l_areg", visible = False),
                gui.Column(layout_adminmenu, key = "l_amenu", visible = False),
                gui.Column(layout_iteminfo, key = "l_iteminfo", visible = False),
                gui.Column(layout_tabrestock, key = "l_restock", visible = False),
                gui.Column(layout_delivery, key = "l_delivery", visible = False),
                gui.Column(layout_billhistory, key = "l_billhist", visible = False)]
    ]

   # WINDOW
    window = gui.Window("Mavika Store", layout, resizable = True)

    #while-event loop
    while True:
    
        #ESTABLISHING
        event, values = window.read()

        #START
        if event in (gui.WIN_CLOSED, "Exit"):
            break

        # user
        if event == "User":
            window["l_ulogin"].update(visible = True)
            window["l_menu"].update(visible = False)
        
        if event == "back_userlogin":
            window["l_menu"].update(visible = True)
            window["l_ulogin"].update(visible = False)

        # User login
        if event == "enter_userlogin":

            data1 = " "
            cur.execute("SELECT * FROM USER")
            itemn3 = cur.fetchall()
            for i in itemn3:
                data1 = data1 + str(i)
                
            NAME1 = values["username"]
            PASSWD = values["userpassword"]
            
            if NAME1 in data1 and PASSWD in data1:
                 window["l_umenu"].update(visible = True)
                 window["l_ulogin"].update(visible = False)
            else:
                gui.Popup("INVALID CREDENTIALS")
        
        if event == "back_userlogin":
            window["l_menu"].update(visible = True)
            window["l_ulogin"].update(visible = False)

        if event == "back_usermenu":
            window["l_menu"].update(visible = True)
            window["l_umenu"].update(visible = False)

        # New User 
        if event == "ureg":
            window["l_ureg"].update(visible = True)
            window["l_ulogin"].update(visible = False)

        if event == "enter_userreg":
            # Creating User
            name = values["userregname"]
            pd = values["userregpassword"]
            no = int(values["userno"])
            addr = values["useraddress"]
            query = "INSERT INTO USER VALUES ('{}', '{}', {}, '{}')".format(name, pd, no, addr)
            cur.execute(query)
            cnc.commit()
            gui.Popup("Welcome To Our Store")

        if event == "back_userreg":
            window["l_ulogin"].update(visible = True)
            window["l_ureg"].update(visible = False)
        #user end
            
        # Get Info starts
        if event == "Get Information":
            window["l_getinfo"].update(visible = True)
            window["l_umenu"].update(visible = False)

        if event == "search_ugetinfo" and values["uITEMID"] == '':
            gui.Popup("Please Enter Item ID")

        if event == "search_ugetinfo" and values["uITEMID"] != '':

            gi = int(values["uITEMID"])
            cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(gi))
            itemn2 = cur.fetchone()
            info_table_ugetinfo.append([itemn2[0], itemn2[1], itemn2[2], itemn2[3], itemn2[4]])
            window["tableugetinfo"].update(values = info_table_ugetinfo)

        if event == "back_ugetinfo":
            window["l_umenu"].update(visible = True)
            window["l_getinfo"].update(visible = False)
            info_table_ugetinfo.clear()
            window["tableugetinfo"].update(values = info_table_ugetinfo)
        # Get Info ends
        
        #List of Items
        if event == "List Of Items":
            window["l_listitems"].update(visible = True)
            window["l_umenu"].update(visible = False)

            cur.execute("SELECT * FROM ITEMS")
            itemn1 = cur.fetchall()
            for i in itemn1:
                info_table_listitems.append([i[0], i[1], i[2], i[3], i[4]])
            window["tableitems"].update(values = info_table_listitems)
            
        if event == "back_listitems":
             window["l_umenu"].update(visible = True)
             window["l_listitems"].update(visible = False)
             info_table_listitems.clear()
             window["tableitems"].update(values = info_table_listitems)
             
        #List of Items end
        
        # Selfcheckout
        if event == "Self Check-Out":
            window["l_scheckout"].update(visible = True)
            window["l_umenu"].update(visible = False)

        if event == "back_selfcheckout":
             window["l_umenu"].update(visible = True)
             window["l_scheckout"].update(visible = False)
             info_table_bill.clear()
             window["tablebill"].update(values = info_table_bill)


        #==make bill==
        if event == "Add" and values["id"] == '' and values["qty"] == '':
            gui.Popup("Please Enter ID and QUANTITY")

        if event == "Add" and values["id"] != '' and values["qty"] != '':
            
            i = int(values["id"])
            q = int(values["qty"])
            cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(i))
            item = cur.fetchone()
            uq = int(item[2])
            price1 = int(values["qty"])*int(item[3])
            info_table_bill.append([i, item[1], q, price1])
            price2.append(price1)
            window["tablebill"].update(values = info_table_bill)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)

            query2 = 'UPDATE ITEMS set STOCK_QTY = {} - {} where ITEM_ID = {}'.format(uq, q, values["id"])
            cur.execute(query2)
            cnc.commit()
            print(uq-q)

            Q = Q + q
            titems = titems + item[1] + ","

        #++save bill++
        if event == "savebill_selfcheckout":

            n = "No"
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}')".format(NAME1, titems, Q, price, n))
            cnc.commit()
  
            gui.Popup("Bill Saved Successfully")

        # ===delivery placing===
        if event == "savedelivery_selfcheckout" and values["delivery_change"] == '':

            cur.execute("SELECT user_number, user_address FROM USER WHERE user_name = '{}'".format(NAME1))
            item_deli = cur.fetchone()
            cur.execute("INSERT INTO DELIVERY VALUES ('{}', {}, '{}')".format(NAME1, item_deli[0], item_deli[1]))
            cnc.commit()

            y = "Yes"
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}')".format(NAME1, titems, Q, price, y))
            cnc.commit()
            
            gui.Popup("Bill Saved and Delivery Placed Successfully")

        if event == "savedelivery_selfcheckout" and values["delivery_change"] != '':

            cur.execute("SELECT user_number FROM USER WHERE user_name = '{}'".format(NAME1))
            item_deli1 = cur.fetchone()
            cur.execute("INSERT INTO DELIVERY VALUES ('{}', {}, '{}')".format(NAME1, item_deli1[0], values["delivery_change"]))
            cnc.commit()

            y = "Yes"
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}')".format(NAME1, titems, Q, price, y))
            cnc.commit()
            
            gui.Popup("Bill Saved and New Delivery Placed Successfully")
        #^selfcheckout^ end

        # admin
        if event == "Admin":
            window["l_alogin"].update(visible = True)
            window["l_menu"].update(visible = False)

        if event == "back_adminlogin":
            window["l_menu"].update(visible = True)
            window["l_alogin"].update(visible = False)
        
        # Admin login
        if event == "enter_adminlogin":

            data2 = " "
            cur.execute("SELECT * FROM ADMINS")
            itemn4 = cur.fetchall()
            for i in itemn4:
                data2 = data2 + str(i)

            if values["admname"] in data2 and values["admpassword"] in data2:

                 cur.execute("SELECT * FROM ITEMS")
                 item1 = cur.fetchall()
                 for i  in item1:
                    info_table_alistitems.append([i[0], i[1], i[2], i[3], i[4]])
                 window["tableitems1"].update(values = info_table_alistitems)

                 window["l_amenu"].update(visible = True)
                 window["l_alogin"].update(visible = False)

            else:
                gui.Popup("INVALID CREDENTIALS")
        
        # New User
        if event == "areg":
            window["l_areg"].update(visible = True)
            window["l_alogin"].update(visible = False)

        if event == "enter_admreg" and int(values["admregsec"]) == 2244:
            # Creating User
            name2 = values["admregname"]
            pd1 = values["admregpassword"]
            cur.execute("INSERT INTO ADMINS VALUES ('{}', '{}')".format(name2, pd1))
            cnc.commit()
            gui.Popup("Welcome To Mavika")
        
        if event == "back_admreg":
            window["l_alogin"].update(visible = True)
            window["l_areg"].update(visible = False)

        if event == "back_admmenu":
            window["l_menu"].update(visible = True)
            window["l_amenu"].update(visible = False)
            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)

        #admin end

         # Item Info starts
        if event == "Item Information":
            window["l_iteminfo"].update(visible = True)
            window["l_amenu"].update(visible = False)

        if event == "search_aiteminfo" and values["aITEMID"] == '':
            gui.Popup("Did Not Enter Item ID")

        if event == "search_aiteminfo" and values["aITEMID"] != '':
            
            gi1 = int(values["aITEMID"])
            cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(gi1))
            item = cur.fetchone()
            info_table_aiteminfo.append([item[0], item[1], item[2], item[3], item[4]])
            window["tableaiteminfo"].update(values = info_table_aiteminfo)

        if event == "back_aiteminfo":
            window["l_amenu"].update(visible = True)
            window["l_iteminfo"].update(visible = False)
            info_table_aiteminfo.clear()
            window["tableaiteminfo"].update(values = info_table_aiteminfo)
        # Item Info ends
        
        #Restock
        if event == "Restock Items":
            window["l_restock"].update(visible = True)
            window["l_amenu"].update(visible = False)
            info_table_alistitems.clear()
            
        if event == "add_stock" and (values["ADDITEMID"], values["ADDITEMNAME"], values["ADDSTOCK"], values["ADDPRICE"], values["ADDDATE"]) != ('','','','',''):

            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)
            
            addid =  int(values["ADDITEMID"])
            addname = values["ADDITEMNAME"]
            addinst = int(values["ADDSTOCK"])
            addprice = int(values["ADDPRICE"])
            adddate = values["ADDDATE"]
            cur.execute("INSERT INTO ITEMS VALUES ({}, '{}', {}, {}, '{}' )".format(addid, addname, addprice, addinst, adddate))
            cnc.commit()
            info_table_stockadd.append([addid, addname, addprice, addinst, adddate])
            window["tablestockadd"].update(values = info_table_stockadd)
            window["add"].update(visible = True)
            
            cur.execute("SELECT * FROM ITEMS")
            item2 = cur.fetchall()
            for i  in item2:
                info_table_alistitems.append([i[0], i[1], i[2], i[3], i[4]])
            window["tableitems1"].update(values = info_table_alistitems)

        if event == "add_stock" and (values["ADDITEMID"], values["ADDITEMNAME"], values["ADDSTOCK"], values["ADDPRICE"], values["ADDDATE"]) == ('','','','',''):
            gui.Popup("Please Enter the Above Values")
        
        if event == "back_stockadd":
            window["l_amenu"].update(visible = True)
            window["l_restock"].update(visible = False)
            info_table_stockadd.clear()
            window["tablestockadd"].update(values = info_table_stockadd)

            cur.execute("SELECT * FROM ITEMS")
            item2 = cur.fetchall()
            for i  in item2:
                info_table_alistitems.append([i[0], i[1], i[2], i[3], i[4]])
            window["tableitems1"].update(values = info_table_alistitems)

        if event == "upd_stock" and (values["UPDITEMID"], values["UPDQTY"], values["UPDPRICE"]) != ('','',''):

            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)

            updid = int(values["UPDITEMID"])
            updqty = int(values["UPDQTY"])
            updprice = int(values["UPDPRICE"])
            cur.execute("UPDATE ITEMS set STOCK_QTY = {}, ITEM_PRICE = {} where ITEM_ID = {}".format(updqty, updprice, values["UPDITEMID"]))
            cnc.commit()
            info_table_stockupd.append([updid, updqty, updprice])
            window["tablestockupd"].update(values = info_table_stockupd)
            window["upd"].update(visible = True)

        if event == "upd_stock" and (values["UPDITEMID"], values["UPDQTY"], values["UPDPRICE"]) == ('','',''):
            gui.Popup("Please Enter the Above Values")
            
        if event == "back_stockupd":
            window["l_amenu"].update(visible = True)
            window["l_restock"].update(visible = False)
            info_table_stockupd.clear()
            window["tablestockupd"].update(values = info_table_stockupd)

            cur.execute("SELECT * FROM ITEMS")
            item3 = cur.fetchall()
            for i  in item3:
                info_table_alistitems.append([i[0], i[1], i[2], i[3], i[4]])
            window["tableitems1"].update(values = info_table_alistitems)

        if event == "del_stock" and values["DELITEMID"] != '':

            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)

            d = int(values["DELITEMID"])
            cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(d))
            item9 = cur.fetchone()
            info_table_stockdel.append([item9[0], item9[1], item9[2], item9[3], item9[4]])
            window["tablestockdel"].update(values = info_table_stockdel)
            
            cur.execute("DELETE FROM ITEMS WHERE ITEM_ID =  {}".format(d))
            cnc.commit()
            window["del"].update(visible = True)

        if event == "del_stock" and values["DELITEMID"] == '':
            gui.Popup("Please Enter the Above Values")

        if event == "back_stockdel":
            window["l_amenu"].update(visible = True)
            window["l_restock"].update(visible = False)
            info_table_stockdel.clear()
            window["tablestockdel"].update(values = info_table_stockdel)

            cur.execute("SELECT * FROM ITEMS")
            item4 = cur.fetchall()
            for i  in item4:
                info_table_alistitems.append([i[0], i[1], i[2], i[3], i[4]])
            window["tableitems1"].update(values = info_table_alistitems)
        # restock end

        #delivery
        if event == "Delivery":
            window["l_delivery"].update(visible = True)
            window["l_amenu"].update(visible = False)

            cur.execute("SELECT * FROM DELIVERY")
            item6 = cur.fetchall()
            for i  in item6:
                info_table_delbill.append([i[0], i[1], i[2]])
            window["tabledel"].update(values = info_table_delbill)

        if event == "done_delivery" and values["custname"] != '':
            namedel = values["custname"]
            cur.execute("DELETE FROM DELIVERY WHERE user_name = '{}'".format(namedel))
            cnc.commit()

            info_table_delbill.clear()
            window["tabledel"].update(values = info_table_delbill)
            cur.execute("SELECT * FROM DELIVERY")
            item6 = cur.fetchall()
            for i  in item6:
                info_table_delbill.append([i[0], i[1], i[2]])
            window["tabledel"].update(values = info_table_delbill)

        if event == "done_delivery" and values["custname"] == '':
            gui.Popup("Please Enter Customer's Name")
        
        if event == "back_delivery":
            window["l_amenu"].update(visible = True)
            window["l_delivery"].update(visible = False)
            info_table_delbill.clear()
            window["tabledel"].update(values = info_table_delbill)
        # Delivery end

        # Bill history
        if event == "Bills":
             window["l_billhist"].update(visible = True)
             window["l_amenu"].update(visible = False)
             
             cur.execute("SELECT * FROM BILLS")
             item7 = cur.fetchall()
             for i  in item7:
                info_table_billhist.append([i[0], i[1], i[2], i[3], i[4]])
             window["tablebillhist"].update(values = info_table_billhist)

        if event == "back_bill":
            window["l_amenu"].update(visible = True)
            window["l_billhist"].update(visible = False)
        #bill history end

    window.close()
gui_propmt2()

