import PySimpleGUI as gui
from datetime import date
import pymysql as c
cnc = c.connect(host="localhost", user= "root", passwd="1234", database="vinayproject2")

print(cnc)

cur = cnc.cursor()

def gui_propmt2():
    # MAIN THINGS
    info_table_ugetinfo = []
    info_table_aiteminfo = []
    info_table_bill = []
    info_table_billhist = []
    info_table_umybill = []
    info_table_delbill = []
    info_table_stockadd = []
    info_table_stockupd = []
    info_table_stockdel = []
    info_table_listitems = []
    info_table_listitems2 = []
    info_table_alistitems = []
    head = ['ID','Item Name','Units','Price']
    head1 = ['ID','Item Name','In-Stock(Units)','Price','Manu. Date']
    head2 = ['Customer Name','Phone No.','Address']
    head3 = ['Customer Name','Items','Total Units','Total Price','Delivery', 'Bill Date']
    lid = []
    lqty = []
    luq = []
    price2 = []
    price1 = 0
    Q = 0
    titems = " "
    
    # THEME
    gui.theme("DarkAmber")
    
    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout_menu = [ [gui.Text("!!Welcome To General Store!!", size = (20, 1), font = ("Cooper Black", 20),
                              expand_x = True, justification = "centre")],
                    [gui.Image(filename = "gen.png", size = (275, 183),  expand_x = True, expand_y = True)],
                    [gui.Column([[gui.Button("User"), gui.Button("Admin")]], element_justification = "centre",
                                expand_x = "True", expand_y = "True")]
    ]
    
    #USER LOGIN
    layout_userlogin = [ [gui.Column([[gui.Text("User Login Window", expand_x = "True", justification = "centre")],
                         [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "username", do_not_clear = False)],
                         [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "userpassword", do_not_clear = False)],
                         [gui.Button("Enter", key = "enter_userlogin"), gui.Button("Back", key = "back_userlogin"), gui.Push(), gui.Button("Register (New User)", key = "ureg")]]
                                     , element_justification = "centre", expand_x = "True", expand_y = "True")]
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

    #USER BILLS
    layout_mybill = [ [gui.Text("Welcome to My Bills", expand_x = "True", justification = "centre")],
                      [gui.Table(values =  info_table_umybill, headings = head3, key = "tableumybill",
                                    justification = "centre", expand_x = "True", auto_size_columns = True)],
                      [gui.Button("Back", key = "back_umybill")]
        
    ]

    #tab
    layout_tabgimb = [ [gui.TabGroup([[gui.Tab("My Bills", layout_mybill),
                                       gui.Tab("Item Information", layout_getinfo)]], tab_location = "centertop")]
    ]

    #USER LIST of ITEMS 
    layout_listitems = [ [gui.Text("Welcome to List of Items", expand_x = "True", justification = "centre")],
                         [gui.Table(values =  info_table_listitems, headings = head1, key = "tableitems",
                                    justification = "centre", expand_x = "True", auto_size_columns = True)],
                         [gui.Button("Back", key = "back_listitems")]
    ]

    #USER SELF CHECK-OUT 
    layout_selfcheckout = [ [gui.Text("Welcome to Self Check-Out", expand_x = "True", justification = "centre")],
                            [gui.Text("Enter ID", size = (16,1)), gui.Input(key = "id", do_not_clear = False, justification = "left", expand_x = "True")],
                            [gui.Text("Enter Quantity (Units)", size = (16,1)), gui.Input(key = "qty", do_not_clear = False, justification = "left", expand_x = "True")],
                            [gui.Button("Add to Bill"), gui.Text("All the Items, to Help You out!", expand_x = "True", justification = "centre")],
                            [gui.Table(values =  info_table_listitems2, headings = head1, key = "tableitems2",
                                    justification = "centre", expand_x = "True", auto_size_columns = True)],
                            [gui.Table(values =  info_table_bill, headings = head, key = "tablebill",
                                       justification = "centre", expand_x = "True", auto_size_columns = True)],
                            [gui.Text("Total Price:", size = (10,1)), gui.Text("₹"), gui.Text(" ", size = (10,1), key = "p", font = ("Courier", 15))],
                            [gui.Button("Save", key = "savebill_selfcheckout"), gui.Button("Save-Place Delivery", key = "savedelivery_selfcheckout"), gui.Push(), gui.Button("Back", key = "back_selfcheckout")],
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
    #ADD ITEMS
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

    #UPDATE ITEMS
    layout_stockupd = [ [gui.Text("Update Stock (Price)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID", size = (19,1)), gui.Input(key = "UPDITEMID", do_not_clear = False)],
                        [gui.Text("Enter New Quantity(Units)", size = (19,1)), gui.Input(key = "UPDQTY", do_not_clear = False)],
                        [gui.Text("Enter New Price(Rupees)", size = (19,1)), gui.Input(key = "UPDPRICE", do_not_clear = False)],
                        [gui.Table(values =  info_table_stockupd, headings = head1, key = "tablestockupd",
                                   justification = "centre", expand_x = "True", auto_size_columns = True, expand_y = "True")],
                        [gui.Text("The Following Details Have Been Updated", size = (20,1), key = "upd", visible = False)],
                        [gui.Button("Update", key = "upd_stock"), gui.Button("Back", key = "back_stockupd")]
    ]

    #DELETE ITEM
    layout_stockdel = [ [gui.Text("Welcome to Stock (DELETION)", expand_x = "True", justification = "centre")],
                        [gui.Text("Enter Item ID to DELETE", size = (19,1)), gui.Input(key = "DELITEMID", do_not_clear = False)],
                        [gui.Table(values =  info_table_stockdel, headings = head1, key = "tablestockdel",
                                   justification = "centre", expand_x = "True", expand_y = "True", auto_size_columns = True)],
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
    layout = [ [gui.Column(layout_menu, key = "l_menu", justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_userlogin, key = "l_ulogin", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_userreg, key = "l_ureg", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_usermenu, key = "l_umenu", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),  
                gui.Column(layout_tabgimb, key = "l_getinfomb", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_listitems, key = "l_listitems", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_selfcheckout, key = "l_scheckout", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_adminlogin, key = "l_alogin", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_adminreg, key = "l_areg", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_adminmenu, key = "l_amenu", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_iteminfo, key = "l_iteminfo", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_tabrestock, key = "l_restock", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_delivery, key = "l_delivery", visible = False, justification = "centre", expand_x = "True", expand_y = "True"),
                gui.Column(layout_billhistory, key = "l_billhist", visible = False, justification = "centre", expand_x = "True", expand_y = "True")]
    ]

   # WINDOW
    window = gui.Window("PyFresh Walk-In Store", layout, finalize = True, element_justification = "centre")

   # functions
    def upd_stock(x):
        for i in rangelen((x)):
                query2 = 'UPDATE ITEMS set STOCK_QTY = {} - {} where ITEM_ID = {}'.format(luq[i], lqty[i], lid[i])
                cur.execute(query2)
                cnc.commit()
            
    def list_items_table(x,k):
        cur.execute("SELECT * FROM ITEMS")
        itemn11 = cur.fetchall()
        for i in itemn11:
            x.append([i[0], i[1], i[2], i[3], i[4]])
        window["k"].update(values = x)

   # WHILE-EVENT-LOOP
    while True:
    
        #ESTABLISHING
        event, values = window.read()

        if event in (gui.WIN_CLOSED, "Exit"):
            break

        # --User Start--
        if event == "User":
            window["l_ulogin"].update(visible = True)
            window["l_menu"].update(visible = False)
        
        if event == "back_userlogin":
            window["l_menu"].update(visible = True)
            window["l_ulogin"].update(visible = False)

        # User Login
        if event == "enter_userlogin"  and values["username"] == '' and values["userpassword"] == '':
            gui.Popup("You've Not Filled The Login Credentials")

        if event == "enter_userlogin" and values["username"] != '' and values["userpassword"] != '':

            data1 = ""
            cur.execute("SELECT * FROM USER")
            itemn3 = cur.fetchall()
            for i in itemn3:
                data1 = data1 + str(i)
            print(data1)
            NAME1 = values["username"]
            PASSWD = values["userpassword"]
            
            if NAME1 in data1 and PASSWD in data1:
                 window["l_umenu"].update(visible = True)
                 window["l_ulogin"].update(visible = False)
            else:
                gui.Popup("Details Not Found In Database")
        
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
        # --User End--
            
        # --Get Info Start--
        if event == "Get Information":
            window["l_getinfomb"].update(visible = True)
            window["l_umenu"].update(visible = False)

        if event == "search_ugetinfo" and values["uITEMID"] == '':
            gui.Popup("Please Enter Item ID")

        if event == "search_ugetinfo" and values["uITEMID"] != '':

            gi = int(values["uITEMID"])

            datagi = ""
            cur.execute("SELECT * FROM ITEMS")
            itemn15 = cur.fetchall()
            for i in itemn15:
                datagi = datagi + str(i)
            print(datagi)
            
            if gi in datagi:
                 cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(gi))    
                 itemn2 = cur.fetchone()
                 info_table_ugetinfo.append([itemn2[0], itemn2[1], itemn2[2], itemn2[3], itemn2[4]])
                 window["tableugetinfo"].update(values = info_table_ugetinfo)
            else:
                gui.Popup("Entered Item ID Not Found")

        if event == "search_umybill" and values["uDATE"] == '':
            gui.Popup("Please Enter A Date")

        if event == "search_umybill" and values["uDATE"] != '':
            
            d = values["uDATE"]
            datad = ""
            cur.execute("SELECT * FROM BILLS")
            itemn16 = cur.fetchall()
            for i in itemn16:
                datad = datad + str(i)
            print(datad)
            
            if d in datad:
                 cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(gi))    
                 itemn2 = cur.fetchone()
                 info_table_umybill.append([itemn21[0], itemn21[1], itemn21[2], itemn21[3], itemn21[4]], itemn21[5])
                 window["tableumybill"].update(values = info_table_umybill)
            else:
                gui.Popup("Entered Date Not Found")
            
        if event == "back_ugetinfo":
            window["l_umenu"].update(visible = True)
            window["l_getinfomb"].update(visible = False)
            info_table_ugetinfo.clear()
            window["tableugetinfo"].update(values = info_table_ugetinfo)

        if event == "back_umybill":
            window["l_umenu"].update(visible = True)
            window["l_getinfomb"].update(visible = False)
            info_table_umybill.clear()
            window["tableumybill"].update(values = info_table_umybill)
        # --Get Info End--
        
        # --List of Items Start--
        if event == "List Of Items":
            window["l_listitems"].update(visible = True)
            window["l_umenu"].update(visible = False)

            list_items_table(info_table_listitems,tableitems):

        if event == "back_listitems":
             window["l_umenu"].update(visible = True)
             window["l_listitems"].update(visible = False)
             info_table_listitems.clear()
             window["tableitems"].update(values = info_table_listitems)
        # --List of Items End--
        
        # --Self checkout Start--
        if event == "Self Check-Out":
            window["l_scheckout"].update(visible = True)
            window["l_umenu"].update(visible = False)

            list_items_table(info_table_listitems2, tableitems2)

        if event == "back_selfcheckout":
            window["l_umenu"].update(visible = True)
            window["l_scheckout"].update(visible = False)
            info_table_bill.clear()
            window["tablebill"].update(values = info_table_bill)
             
            info_table_listitems2.clear()
            window["tableitems2"].update(values = info_table_listitems2)
            
            lid.clear()
            lqty.clear()
            luq.clear()

        # Make Bill
        if event == "Add to Bill" and values["id"] == '' and values["qty"] == '':
            gui.Popup("Please Enter ID and QUANTITY")

        if event == "Add to Bill" and values["id"] != '' and values["qty"] != '':
            
            i = int(values["id"])
            q = int(values["qty"])
            lid.append(values["id"])
            lqty.append(int(values["qty"]))
            cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(i))
            item = cur.fetchone()
            uq = int(item[2])
            luq.append(int(item[2]))
            price1 = int(values["qty"])*int(item[3])
            info_table_bill.append([i, item[1], q, price1])
            price2.append(price1)
            window["tablebill"].update(values = info_table_bill)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)

            Q = Q + q
            titems = titems + item[1] + ","
            
        # Save Bill
        if event == "savebill_selfcheckout":

            n = "No"
            today = date.today()
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}', '{}')".format(NAME1, titems, Q, price, today, n))
            cnc.commit()

            upd_stock(lid)
            
            info_table_listitems2.clear()
            list_items_table(info_table_listitems2, tableitems2)
  
            gui.Popup("Bill Saved Successfully")

        # Delivery Placing
        if event == "savedelivery_selfcheckout" and values["delivery_change"] == '':

            cur.execute("SELECT user_number, user_address FROM USER WHERE user_name = '{}'".format(NAME1))
            item_deli = cur.fetchone()
            cur.execute("INSERT INTO DELIVERY VALUES ('{}', {}, '{}')".format(NAME1, item_deli[0], item_deli[1]))
            cnc.commit()

            y = "Yes"
            today = date.today()
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}', '{}')".format(NAME1, titems, Q, price, today, y))
            cnc.commit()

            upd_stock(lid)

            info_table_listitems2.clear()
            list_items_table(info_table_listitems2, tableitems2)
            
            gui.Popup("Bill Saved and Delivery Placed Successfully")

        if event == "savedelivery_selfcheckout" and values["delivery_change"] != '':

            cur.execute("SELECT user_number FROM USER WHERE user_name = '{}'".format(NAME1))
            item_deli1 = cur.fetchone()
            cur.execute("INSERT INTO DELIVERY VALUES ('{}', {}, '{}')".format(NAME1, item_deli1[0], values["delivery_change"]))
            cnc.commit()

            y = "Yes"
            today = date.today()
            cur.execute("INSERT INTO BILLS VALUES ('{}', '{}', {}, {}, '{}', '{}')".format(NAME1, titems, Q, price, today, y))
            cnc.commit()

            upd_stock(lid)

            info_table_listitems2.clear()
            list_items_table(info_table_listitems2, tableitems2)
            
            gui.Popup("Bill Saved and New Delivery Placed Successfully")
        # --Self Checkout End--

        # --Admin Start--
        if event == "Admin":
            window["l_alogin"].update(visible = True)
            window["l_menu"].update(visible = False)

        if event == "back_adminlogin":
            window["l_menu"].update(visible = True)
            window["l_alogin"].update(visible = False)
        
        # Admin Login
        if event == "enter_adminlogin" and values["admname"] == '' and values["admpassword"] == '':
            gui.Popup("Fill The Login Credentials")
            
        if event == "enter_adminlogin"  and values["admname"] != '' and values["admpassword"] != '':

            data2 = ""
            cur.execute("SELECT * FROM ADMINS")
            itemn4 = cur.fetchall()
            for i in itemn4:
                data2 = data2 + str(i)
           
            if values["admname"] in data2 and values["admpassword"] in data2:
                
                list_items_table(info_table_alistitems, tableitems1)
    
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
            gui.Popup("Welcome To PyFresh")
        
        if event == "back_admreg":
            window["l_alogin"].update(visible = True)
            window["l_areg"].update(visible = False)

        if event == "back_admmenu":
            window["l_menu"].update(visible = True)
            window["l_amenu"].update(visible = False)
            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)
        # --Admin End--

        # --Item Info Starts--
        if event == "Item Information":
            window["l_iteminfo"].update(visible = True)
            window["l_amenu"].update(visible = False)

        if event == "search_aiteminfo" and values["aITEMID"] == '':
            gui.Popup("Did Not Enter Item ID")

        if event == "search_aiteminfo" and values["aITEMID"] != '':
            
            while values["aITEMID"] not in info_table_aiteminfo:
                gi1 = int(values["aITEMID"])
                cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID = {}".format(gi1))
                item = cur.fetchone()
                info_table_aiteminfo.append([item[0], item[1], item[2], item[3], item[4]])
                window["tableaiteminfo"].update(values = info_table_aiteminfo)
            else:
                gui.Popup("The Entered ID's Information is Already Displayed")
                
        if event == "back_aiteminfo":
            window["l_amenu"].update(visible = True)
            window["l_iteminfo"].update(visible = False)
            info_table_aiteminfo.clear()
            window["tableaiteminfo"].update(values = info_table_aiteminfo)
        # --Item Info Ends--
        
        # --Restock Start--
        if event == "Restock Items":
            window["l_restock"].update(visible = True)
            window["l_amenu"].update(visible = False)
            info_table_alistitems.clear()
            window["tableitems1"].update(values = info_table_alistitems)
            
        if event == "add_stock" and (values["ADDITEMID"], values["ADDITEMNAME"], values["ADDSTOCK"], values["ADDPRICE"], values["ADDDATE"]) != ('','','','',''):
            
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

        if event == "add_stock" and (values["ADDITEMID"], values["ADDITEMNAME"], values["ADDSTOCK"], values["ADDPRICE"], values["ADDDATE"]) == ('','','','',''):
            gui.Popup("Please Enter the Above Values")
        
        if event == "back_stockadd":
            window["l_amenu"].update(visible = True)
            window["l_restock"].update(visible = False)
            info_table_stockadd.clear()
            window["tablestockadd"].update(values = info_table_stockadd)

            list_items_table(info_table_alistitems, tableitems1)
            
        if event == "upd_stock" and (values["UPDITEMID"], values["UPDQTY"], values["UPDPRICE"]) != ('','',''):

            updid = int(values["UPDITEMID"])
            updqty = int(values["UPDQTY"])
            updprice = int(values["UPDPRICE"])
            cur.execute("UPDATE ITEMS set STOCK_QTY = {}, ITEM_PRICE = {} where ITEM_ID = {}".format(updqty, updprice, values["UPDITEMID"]))
            cnc.commit()
            
            cur.execute(“SELECT * FROM ITEMS WHERE ITEM_ID = {}”.format(updid))
            item99 = cur.fetchone()
            info_table_stockupd.append([item99[0], item99[1], item99[2], item99[3], item99[4]])
            window["tablestockupd"].update(values = info_table_stockupd)
            window["upd"].update(visible = True)

        if event == "upd_stock" and (values["UPDITEMID"], values["UPDQTY"], values["UPDPRICE"]) == ('','',''):
            gui.Popup("Please Enter the Above Values")
            
        if event == "back_stockupd":
            window["l_amenu"].update(visible = True)
            window["l_restock"].update(visible = False)
            info_table_stockupd.clear()
            window["tablestockupd"].update(values = info_table_stockupd)

            list_items_table(info_table_alistitems, tableitems1)

        if event == "del_stock" and values["DELITEMID"] != '':

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

            list_items_table(info_table_alistitems, tableitems1)
        # --Restock End--

        # --Delivery Start--
        if event == "Delivery":
            window["l_delivery"].update(visible = True)
            window["l_amenu"].update(visible = False)

            list_items_table(info_table_delbill, tabledel)

        if event == "done_delivery" and values["custname"] != '':
            
            namedel = values["custname"]
            cur.execute("DELETE FROM DELIVERY WHERE user_name = '{}'".format(namedel))
            cnc.commit()

            info_table_delbill.clear()
            window["tabledel"].update(values = info_table_delbill)

            list_items_table(info_table_delbill, tabledel)

        if event == "done_delivery" and values["custname"] == '':
            gui.Popup("Please Enter Customer's Name")
        
        if event == "back_delivery":
            window["l_amenu"].update(visible = True)
            window["l_delivery"].update(visible = False)
            info_table_delbill.clear()
            window["tabledel"].update(values = info_table_delbill)
        # --Delivery End--

        # --Bill History Start--
        if event == "Bills":
             window["l_billhist"].update(visible = True)
             window["l_amenu"].update(visible = False)
             
            list_items_table(info_table_billhist, tablebillhist)

        if event == "back_bill":
            window["l_amenu"].update(visible = True)
            window["l_billhist"].update(visible = False)
        # --Bill History End--

    window.close()
gui_propmt2()
