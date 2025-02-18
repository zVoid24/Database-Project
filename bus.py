import mysql.connector
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk
from customtkinter import CTkImage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib import colors


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

connection = mysql.connector.connect(
    host='',
    database='',
    user='',
    password='',
    port=11132,
    ssl_ca=r"certificate.pem",  
    ssl_disabled=False  
)

def update_timestamp():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp_label.configure(text=f"Timestamp: {now}")
    timestamp_label.after(1000, update_timestamp)

def reset_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def validate_non_empty_fields(*fields):
    for field in fields:
        if isinstance(field, customtkinter.CTkTextbox):
            content = field.get("1.0", "end-1c").strip()
        else:
            content = field.get().strip()
        if not content:
            return False
    return True

def login():
    username = admin_user.get()
    password = admin_pass.get()
    if not validate_non_empty_fields(admin_user, admin_pass):
        messagebox.showerror("Invalid Input", "Please enter both username and password.")
        return
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM admin WHERE admin_user = SHA2(%s,256) AND admin_pass = SHA2(%s,256)"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Login Successful", "You are logged in!")
            
            for widget in frame.winfo_children():
                widget.destroy()
            show_dashboard()  
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database connection error: {err}")

def proceed():
    cursor = connection.cursor()
    passenger_id_value = passenger_id.get()  
    amount_value = amount.get()
    if not validate_non_empty_fields(passenger_id, amount):
        messagebox.showerror("Invalid Input", "Please enter both Passenger ID and amount.")
        return
    if not amount_value.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
        return
    try:
        if not amount_value.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
            return
        if int(amount_value)>=20:
            query = "UPDATE passenger SET passenger_balance = passenger_balance + %s WHERE passenger_id = %s"
            cursor.execute(query, (amount_value, passenger_id_value))
            connection.commit()
            messagebox.showinfo("Recharge Successful", "Passenger balance updated successfully.")
            for widget in frame.winfo_children():
                widget.destroy()  
            recharge()  
        else:
            messagebox.showerror("Error","You can't recharge less then 20/= BDT")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database update error: {err}")
    finally:
        cursor.close() 

def recharge():
    for widget in frame.winfo_children():
        widget.destroy()
    l = customtkinter.CTkLabel(master=frame,text="Recharge Panel",font=("Roboto",24))
    l.pack(pady=12,padx=10)
    global passenger_id
    passenger_id=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Passenger unique ID",width=200)
    passenger_id.pack(pady=12,padx=10)
    global amount
    amount=customtkinter.CTkEntry(master=frame,placeholder_text="Enter the amount",width=200)
    amount.pack(pady=12,padx=10)
    recharge_button=customtkinter.CTkButton(master=frame,text="Proceed",font=("Roboto",24),command=proceed)
    recharge_button.pack(pady=20)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=show_dashboard)
    back_btn.place(x=10, y=10)

def register_passenger():
    for widget in frame.winfo_children():
        widget.destroy()
    l=customtkinter.CTkLabel(master=frame,text="Register Passenger",font=("Roboto",24))
    l.pack(pady=12,padx=10)
    global name 
    name = customtkinter.CTkEntry(master=frame,placeholder_text="Passenger Name",width=200)
    name.pack(pady=12,padx=10)
    global nid
    nid = customtkinter.CTkEntry(master=frame,placeholder_text="Passenger NID",width=200)
    nid.pack(pady=12,padx=10)
    global student
    student = customtkinter.CTkCheckBox(master=frame, text="Is passenger a Student?")
    student.pack()
    add_button=customtkinter.CTkButton(master=frame,text="Proceed",font=("Roboto",24),command=add_passenger)
    add_button.pack(pady=12,padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=show_dashboard)
    back_btn.place(x=10, y=10)

def add_passenger():
    cursor = connection.cursor()
    passenger_name = name.get()  
    passenger_nid = nid.get()
    st=student.get()
    if not validate_non_empty_fields(name, nid):
        messagebox.showerror("Invalid Input", "Please enter both Passenger Name and NID.")
        return
    try:
        query = "INSERT INTO passenger(passenger_name,passenger_nid,student,passenger_balance) VALUES(%s,%s,%s,%s)"
        cursor.execute(query, (passenger_name, passenger_nid,st,200))
        connection.commit()
        messagebox.showinfo("Register Successful", "Passenger information updated successfully.")
        for widget in frame.winfo_children():
            widget.destroy()  
        register_passenger()  
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database update error: {err}")
    finally:
        cursor.close() 

def add_bus():
    for widget in frame.winfo_children():
        widget.destroy()
    l = customtkinter.CTkLabel(master=frame,text="Add Bus to Database",font=("Roboto",24))
    l.pack(pady=12,padx=10)
    global bus_name
    bus_name=customtkinter.CTkEntry(master=frame,placeholder_text="Enter Bus Name",width=200)
    bus_name.pack(pady=12,padx=10)
    global bu_id
    bu_id=customtkinter.CTkEntry(master=frame,placeholder_text="Route ID",width=200)
    bu_id.pack(pady=12,padx=10)
    global bus_stopage_number
    bus_stopage_number=customtkinter.CTkEntry(master=frame,placeholder_text="Stopage Number",width=200)
    bus_stopage_number.pack(pady=12,padx=10)
    bus_add = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 24), command=add_bus_stopage)
    bus_add.pack(pady=12,padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=show_dashboard)
    back_btn.place(x=10, y=10)

def add_bus_stopage():
    bus_n = bus_name.get()  
    bus_s = bus_stopage_number.get()
    global buss_id
    buss_id=(bu_id.get())
    if not validate_non_empty_fields(bus_name, bus_stopage_number):
        messagebox.showerror("Invalid Input", "Please enter both Bus Name and Stoppage Number.")
        return
    if not bus_s.isdigit() or not bus_n:
        messagebox.showerror("Invalid Input", "Please enter a valid Bus Name and Stoppage Number.")
        return
    bus_s = int(bus_s) 
    for widget in frame.winfo_children():
        widget.destroy()
    global stopages 
    stopages = []
    abs_l=customtkinter.CTkLabel(master=frame,text="Add Stoppages",font=("Roboto",24))
    abs_l.pack(pady=12,padx=10)
    for i in range(bus_s):
        stopage = customtkinter.CTkEntry(master=frame, placeholder_text=f"Enter Stoppage no: {i + 1}", width=200)
        stopage.pack(pady=12, padx=10)
        stopages.append(stopage) 
    proceed_button = customtkinter.CTkButton(master=frame, text="Add Stoppages", font=("Roboto", 24), command=lambda: add_stopages(bus_n))
    proceed_button.pack(pady=20)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=add_bus)
    back_btn.place(x=10, y=10)

def add_stopages(bus_n): 
    busss_id = buss_id  
    stopages_values = []  
    if not stopages:
        messagebox.showerror("Error", "No stoppages entered.")
        return
    for stopage in stopages:
        stopages_values.append(stopage.get()) 
    s_n = len(stopages_values)
    if any(not stopage.strip() for stopage in stopages_values):
        messagebox.showerror("Invalid Input", "Please enter all stoppage names.")
        return
    cursor = connection.cursor()
    stopage_columns = ", ".join([f"stopage{i+1}" for i in range(s_n)])
    stopage_values = ", ".join([f"'{stopage}'" for stopage in stopages_values])
    query = f"INSERT INTO bus(bus_name, {stopage_columns}) VALUES ('{bus_n}', {stopage_values})"
    query2 = f"SELECT bus_id FROM bus WHERE bus_name='{bus_n}'"
    try:
        cursor.execute(query)
        cursor.execute(query2)
        bussss_id = cursor.fetchone()
        if bussss_id is None:
            messagebox.showerror("Error", "Bus not found.")
            return
        query3 = f"INSERT INTO busroute(bus_id, route_id) VALUES({bussss_id[0]}, '{busss_id}')"
        cursor.execute(query3)
        connection.commit()
        messagebox.showinfo("Success", "Bus and stoppages added successfully.")
        add_bus()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()

def see_complain():
    cursor = connection.cursor()
    query = "SELECT * FROM complain"
    try:
        cursor.execute(query)
        res = cursor.fetchall()  
        reset_frame()  
        c_l = customtkinter.CTkLabel(master=frame, text="Complaints\n_______________", font=("Roboto", 20))
        c_l.pack(pady=12, padx=10)     
        if not res:
            no_data_label = customtkinter.CTkLabel(
                master=frame,
                text="No complaints found.",
                font=("Roboto", 20)
            )
            no_data_label.pack(padx=12, pady=10)
        else:
            tree = ttk.Treeview(frame, columns=("Complain ID", "Passenger ID", "Bus ID", "Description"), show="headings", height=10)
            tree.heading("Complain ID", text="Complain ID")
            tree.heading("Passenger ID", text="Passenger ID")
            tree.heading("Bus ID", text="Bus ID")
            tree.heading("Description", text="Description")
            tree.column("Complain ID", width=120, anchor='center')
            tree.column("Passenger ID", width=120, anchor='center')
            tree.column("Bus ID", width=120, anchor='center')
            tree.column("Description", width=300, anchor='center')  
            tree.pack(pady=20, padx=20)
            for result in res:
                truncated_description = result[3][:50] + "..." if len(result[3]) > 50 else result[3]
                tree.insert("", "end", values=(result[0], result[1], result[2], truncated_description))
            tree.bind("<Double-1>", lambda event: on_complaint_row_click(tree, res))
        back_btn = customtkinter.CTkButton(
            master=frame,
            text="Back",
            font=("Roboto", 14),
            width=50,
            command=show_dashboard 
        )
        back_btn.place(x=10, y=10)     
    except Exception as e:
        messagebox.showerror(f"An error occurred: {e}")
        
def on_complaint_row_click(tree, res):
    selected_item = tree.selection() 
    if selected_item:
        index = tree.index(selected_item)
        complaint_details = res[index]
        show_complaint_details(complaint_details)

def show_complaint_details(complaint):
    reset_frame()
    complain_id, passenger_id, bus_id, full_description = complaint
    customtkinter.CTkLabel(master=frame, text=f"Complain ID: {complain_id}", font=("Roboto", 16)).pack(pady=10)
    customtkinter.CTkLabel(master=frame, text=f"Passenger ID: {passenger_id}", font=("Roboto", 16)).pack(pady=10)
    customtkinter.CTkLabel(master=frame, text=f"Bus ID: {bus_id}", font=("Roboto", 16)).pack(pady=10)
    customtkinter.CTkLabel(master=frame, text="Description:", font=("Roboto", 16)).pack(pady=5)
    description_label = customtkinter.CTkLabel(master=frame, text=full_description, font=("Roboto", 14), wraplength=500, justify="left")
    description_label.pack(pady=10, padx=20)
    close_btn = customtkinter.CTkButton(master=frame, text="Close", command=see_complain)
    close_btn.pack(pady=20)

def route_data():
    global stopage
    stopage = []
    for st in stopages:
        stopage.append(st.get().strip())      
    n = len(stopage)
    if n == 0:
        messagebox.showerror("Input Error", "No stoppages entered.")
        return   
    s = ""
    for i in range(n):
        if i == n - 1:
            s += f"{stopage[i]} INT NOT NULL" 
        else:
            s += f"{stopage[i]} INT NOT NULL,\n"
    query = f"""
    CREATE TABLE {route_i} (
        route_id VARCHAR(30) NOT NULL,
        {s},
        PRIMARY KEY(route_id)
    );
    """
    cursor=connection.cursor()
    for i in range(n):
        cursor.execute(f"""SELECT * FROM stoppages WHERE stoppage_name='{stopage[i]}'""")
        x=cursor.fetchone()
        if x is None:
            cursor.execute(f"""INSERT INTO stoppages(stoppage_name) VALUES('{stopage[i]}')""")
    connection.commit()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Register Successful", "Route information updated successfully.")
    except mysql.connector.Error as db_error:
        messagebox.showerror("Database Error", f"Failed to create table: {db_error}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    finally:
        reset_frame()
        show_dashboard()


def route_proceed():
    global stopages, route_i
    try:
        r_n = int(route_number.get().strip())  
        route_i = str(route_id.get().strip())      
        if r_n <= 0:
            raise ValueError("The number of stoppages must be a positive integer.") 
        stopages = []
        reset_frame()
        for i in range(r_n):
            stopage = customtkinter.CTkEntry(master=frame, placeholder_text=f"Enter Stopage no: {i + 1}", width=200)
            stopage.pack(pady=12, padx=10)
            stopages.append(stopage)  
        proceed_button = customtkinter.CTkButton(master=frame, text="Add Stopages", font=("Roboto", 18), command=route_data)
        proceed_button.pack(pady=20)
        back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=add_route)
        back_btn.place(x=10, y=10)
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def add_route():
    reset_frame()
    lar = customtkinter.CTkLabel(master=frame, text="Add Route", font=("Roboto", 18))
    lar.pack(pady=12, padx=10)
    global route_number
    route_number = customtkinter.CTkEntry(master=frame, placeholder_text="Stopage Number", width=200)
    route_number.pack(pady=12, padx=10)
    global route_id
    route_id = customtkinter.CTkEntry(master=frame, placeholder_text="Route Unique Id", width=200)
    route_id.pack(pady=12, padx=10)
    route_route = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 18), command=route_proceed)
    route_route.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=show_dashboard)
    back_btn.place(x=10, y=10)

def show_dashboard():
    reset_frame()
    label = customtkinter.CTkLabel(master=frame, text="Welcome to Admin Dashboard", font=("Roboto", 18))
    label.pack(padx=12, pady=10)
    button = customtkinter.CTkButton(master=frame,text="Recharge",font=("Roboto",18),command=recharge)
    button.pack(pady=20)
    button2 = customtkinter.CTkButton(master=frame,text="Register Passenger",font=("Roboto",18),command=register_passenger)
    button2.pack(pady=20)
    button3 = customtkinter.CTkButton(master=frame,text="Add Bus",font=("Roboto",18),command=add_bus)
    button3.pack(pady=20)
    button4 = customtkinter.CTkButton(master=frame,text="See Complain",font=("Roboto",18),command=see_complain)
    button4.pack(pady=20)
    button5 = customtkinter.CTkButton(master=frame,text="Add Route",font=("Roboto",18),command=add_route)
    button5.pack(pady=20)
    back_btn = customtkinter.CTkButton(master=frame, text="Sign Out", font=("Roboto", 18),  command=admin)
    back_btn.pack(pady=20)

def admin():
    reset_frame()
    label = customtkinter.CTkLabel(master=frame, text="Admin Login Panel", font=("Roboto", 24))
    label.pack(padx=12, pady=10)
    start_label = customtkinter.CTkLabel(master=frame, text="Username", font=("Roboto", 18))
    start_label.pack(pady=10)
    global admin_user
    admin_user = customtkinter.CTkEntry(master=frame, placeholder_text="Username", width=200)
    admin_user.pack(padx=12, pady=10)
    start_label = customtkinter.CTkLabel(master=frame, text="Password", font=("Roboto", 18))
    start_label.pack(pady=10)
    global admin_pass
    admin_pass = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*", width=200)
    admin_pass.pack(padx=12, pady=10)
    check_box = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    check_box.pack()
    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=main_screen)
    back_btn.place(x=10, y=10)

def ticket_buy():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stoppages")
    x = cursor.fetchall()  
    stoppage = []  
    for s in x:
        stoppage.append(s[0])  
    cursor.close()
    reset_frame()
    l2 = customtkinter.CTkLabel(master=frame, text="Buy Ticket", font=("Roboto", 20))
    l2.pack(padx=10, pady=12) 
    global timestamp_label
    timestamp_label = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 14))
    timestamp_label.pack(pady=5)
    update_timestamp()  
    global start
    start_label = customtkinter.CTkLabel(master=frame, text="Your Location", font=("Roboto", 20))
    start_label.pack(pady=12, padx=10)
    start = customtkinter.CTkOptionMenu(frame, values=stoppage)  
    start.pack(pady=12, padx=10)
    global end
    end_label = customtkinter.CTkLabel(master=frame, text="Destination", font=("Roboto", 20))
    end_label.pack(pady=12, padx=10)
    end = customtkinter.CTkOptionMenu(frame, values=stoppage) 
    end.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=main_screen)
    back_btn.place(x=10, y=10)
    btn = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 14), width=50, command=ticket_proceed)
    btn.pack(padx=10, pady=12)

def ticket_proceed():
    global start_stop
    global end_stop
    start_stop = start.get().strip()
    end_stop = end.get().strip()
    if not validate_non_empty_fields(start, end):
        messagebox.showerror("Invalid Input", "Please enter both starting and ending stoppages.")
        return
    cursor = connection.cursor()
    query = """
    SELECT bus_name FROM bus 
    WHERE 
    (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
     stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    AND
    (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
     stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    """
    params = [start_stop] * 10 + [end_stop] * 10
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        for widget in frame.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame):
                widget.destroy()
        global results_frame
        results_frame = customtkinter.CTkFrame(master=frame)
        results_frame.pack(pady=20, padx=20)
        if results:
            for bus in results:
                bus_label = customtkinter.CTkButton(
                    master=results_frame,
                    text=f"{bus[0]}",
                    font=("Roboto", 18),
                    command=lambda b=bus[0]: purchase_ticket(b) 
                )
                bus_label.pack(pady=10, padx=12)
        else:
            messagebox.showinfo("No Buses Found", "No buses found for the given stoppages.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database query error: {err}")
    finally:
        cursor.close()

def purchase_ticket(bus_name):
    global st
    st=start_stop
    global en
    en=end_stop
    try:
        global b_id
        b_id=bus_name
        cursor = connection.cursor()
        cursor.execute("SELECT bus_id FROM bus WHERE bus_name = %s", (bus_name,))
        bus_id = cursor.fetchone()
        if not bus_id:
            messagebox.showerror("Error", "Bus not found.")
            return
        cursor.execute("SELECT route_id FROM busroute WHERE bus_id = %s", (bus_id[0],))
        route_id = cursor.fetchone()
        if not route_id:
            messagebox.showerror("Error", "Route not found.")
            return
        route_table = f"{route_id[0]}" 
        query = f"""
            SELECT `{start_stop}`, `{end_stop}` FROM {route_table}
            WHERE 1 LIMIT 1
        """
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            start_distance, end_distance = result 
            if start_distance is None or end_distance is None:
                messagebox.showerror("Error", "Unable to find distances for the specified stops.")
                return
            distance = abs(end_distance - start_distance) 
            global ticket_price 
            ticket_price = distance * 2
            ticket_price=max(ticket_price,10)
            ticket_price2=ticket_price/2
            ticket_price2=max(ticket_price2,10)
            reset_frame()  
            pt_l=customtkinter.CTkLabel(master=frame,text="Fair\n______",font=("Roboto",24))
            pt_l.pack(padx=10,pady=10)
            price_label=customtkinter.CTkLabel(master=frame,text=f"Regular: {ticket_price}/= BDT",font=("Roboto",20))
            price_label.pack(padx=10,pady=12)
            price_label2=customtkinter.CTkLabel(master=frame,text=f"Student: {ticket_price2}/= BDT",font=("Roboto",20))
            price_label2.pack(padx=10,pady=12)
            price_button=customtkinter.CTkButton(master=frame,text="Buy",font=("Roboto",20),command=confirm)
            price_button.pack(pady=12,padx=10)
            back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=ticket_buy)
            back_btn.place(x=10, y=10)
            return ticket_price
        else:
            messagebox.showerror("Error", "Unable to calculate distance. No result from query.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()

def confirm():
    global st1
    st1=st
    global en1
    en1=en
    global tk_price
    tk_price = ticket_price 
    global b_idd
    b_idd=b_id
    reset_frame()
    global s_en 
    c_p=customtkinter.CTkLabel(master=frame,text="Confirm Your Ticket",font=("Roboto",24))
    c_p.pack(padx=12,pady=10)
    s_en = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Your Unique Passenger ID", width=200)
    s_en.pack(pady=12, padx=10)
    b_t = customtkinter.CTkButton(master=frame, text="Buy", font=("Roboto", 20), command=purchase)
    b_t.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=ticket_buy)
    back_btn.place(x=10, y=10)

def purchase():
    cursor = None
    try:
        b_iddd = b_idd
        tk_p = tk_price
        p_i = int(s_en.get())  
        cursor = connection.cursor()
        cursor.execute("SELECT bus_id FROM bus WHERE bus_name = %s", (b_iddd,))
        b_idh = cursor.fetchone()
        cursor.execute("SELECT student FROM passenger WHERE passenger_id = %s", (p_i,))
        s = cursor.fetchone()
        stt = f"Ticket Price: {tk_p}" 

        if s is None:
            messagebox.showerror("Error", "Passenger ID not found.")
            return
        if s[0] == 1:
            tk_p /= 2
            tk_p = max(tk_p, 10)
            stt = f"Ticket Price: {tk_p} (Halfed Because of Student)"
        tk_p = max(tk_p, 10)
        cursor.execute("SELECT passenger_balance FROM passenger WHERE passenger_id = %s", (p_i,))
        balance = cursor.fetchone()
        if balance is None or balance[0] < tk_p:
            messagebox.showerror("Error", "Insufficient balance.")
            return
        cursor.execute("UPDATE passenger SET passenger_balance = passenger_balance - %s WHERE passenger_id = %s", (tk_p, p_i))
        current_time = datetime.now()
        cursor.execute("""INSERT INTO trans(passenger_id, bus_id, amount, transaction_time)
                          VALUES( %s, %s, %s, %s)""",
                       ( p_i, b_idh[0], tk_p, current_time))
        x=0
        cursor.execute("""INSERT INTO tickets(passenger_id,bus_id,st,en,amount,check_ticket,transaction_time) VALUES(%s, %s, %s, %s, %s,%s,%s)""",
                       (p_i, b_idh[0],st1,en1, tk_p,x, current_time))
        cursor.execute("SELECT LAST_INSERT_ID()")
        ticket_id = cursor.fetchone()[0]
        connection.commit()
        if ticket_id:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=15,
                border=4,
            )
            qr.add_data(ticket_id)
            qr.make(fit=True)
            qr_image = qr.make_image(fill="black", back_color="white")
            qr_image_path = "qr_code_temp.png"
            qr_image.save(qr_image_path)
            qr_pil_image = Image.open(qr_image_path)
            qr_ctk_image = CTkImage(light_image=qr_pil_image, size=(300, 300))
            global qr_label
            if 'qr_label' not in globals() or qr_label.winfo_exists() == 0:
                qr_label = customtkinter.CTkLabel(master=frame, text="")
                qr_label.pack(padx=10, pady=50)

            qr_label.configure(image=qr_ctk_image)
            qr_label.image = qr_ctk_image  
            c = canvas.Canvas("example_with_qr.pdf", pagesize=letter)
            width, height = letter
            c.setFillColor(colors.red) 
            c.setFont("Helvetica-Bold", 14) 
            c.drawString(100, height - 100, "Ticket Confirmation")
            c.setFillColor(colors.black)  
            c.setFont("Helvetica", 12)  
            c.drawString(100, height - 120, f"Ticket ID: {ticket_id}")
            c.setFillColor(colors.black)  
            c.drawString(100, height - 140, f"Passenger ID: {p_i}")
            c.setFillColor(colors.black)  
            c.drawString(100, height - 160, f"Bus ID: {b_idh[0]}")
            c.setFillColor(colors.black)  
            c.drawString(100, height - 180, f"From: {st1}")
            c.setFillColor(colors.black)  
            c.drawString(100, height - 200, f"To: {en1}")
            c.drawImage(qr_image_path, 150, height - 310, width=100, height=100)
            c.save()
        status_label = customtkinter.CTkLabel(master=frame, text=f"Ticket purchased successfully. {stt}. Remaining balance: {balance[0] - tk_p}")
        status_label.pack(padx=10, pady=50)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Passenger ID.")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        if cursor is not None:
            if cursor._executed:
                cursor.fetchall()  
            cursor.close()

def balance():
    cursor = connection.cursor()
    if 'id_entry' in globals() and validate_non_empty_fields(id_entry):
        idd = int(id_entry.get())
        try:
            reset_frame()
            query = "SELECT passenger_id,passenger_name,passenger_balance FROM passenger WHERE passenger_id = %s"
            cursor.execute(query, (idd,))
            Balance = cursor.fetchall()
            if Balance:  
                tree = ttk.Treeview(frame, columns=("Passenger ID", "Passenger Name", "Balance"), show="headings", height=10)
                tree.heading("Passenger ID", text="Passenger ID")
                tree.heading("Passenger Name", text="Passenger Name")
                tree.heading("Balance", text="Balance")
                tree.column("Passenger ID", width=120, anchor='center')
                tree.column("Passenger Name", width=100, anchor='center')
                tree.column("Balance", width=120, anchor='center')
                tree.pack(pady=50, padx=20, anchor='center')
                for balances in Balance:
                    tree.insert("", "end", values=balances)
                back_btn = customtkinter.CTkButton(master=frame, text="Back", width=50, font=("Roboto", 14), command=show_balance)
                back_btn.place(x=10, y=10)
            else:
                messagebox.showerror("Error", "No passenger found with this ID.")
                show_balance()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database query error: {err}")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid ID.")
    cursor.close()

def show_balance():
    reset_frame()
    l2=customtkinter.CTkLabel(master=frame,text="Check Balance",font=("Roboto",20))
    l2.pack(padx=10,pady=12)
    global id_entry
    id_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your ID", width=200)
    id_entry.pack(pady=12, padx=10)
    btn = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 14), width=50, command=balance)
    btn.pack(padx=10, pady=12)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=main_screen)
    back_btn.place(x=10, y=10)

def complain():
    reset_frame()
    l2=customtkinter.CTkLabel(master=frame,text="Register Your Complain",font=("Roboto",20))
    l2.pack(padx=10,pady=12)
    global b_i
    b_i=customtkinter.CTkEntry(master=frame,placeholder_text="Enter Bus ID",width=200)
    b_i.pack(pady=12,padx=10)
    global c_i
    c_i=customtkinter.CTkEntry(master=frame,placeholder_text="Enter Your Passenger ID",width=200)
    c_i.pack(pady=12,padx=10)
    global d_i
    d_i = customtkinter.CTkTextbox(master=frame, width=200, height=200)
    d_i.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=main_screen)
    back_btn.place(x=10, y=10)
    btn = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 14), width=50, command=complain_proceed)
    btn.pack(padx=10, pady=12)

def complain_proceed():
    c_d = d_i.get("1.0", "end-1c").strip()  
    cursor = connection.cursor()
    if not validate_non_empty_fields(b_i, c_i, d_i):
        messagebox.showerror("Invalid Input", "Please enter Information Correctly.")
        return
    try:
        b_id = int(b_i.get().strip()) 
        p_id = int(c_i.get().strip())   
    except ValueError:
        messagebox.showerror("Invalid Input", "Bus ID and Passenger ID must be integers.")
        return
    query = "INSERT INTO complain(passenger_id, bus_id, description) VALUES (%s, %s, %s)"
    query2=f"SELECT * FROM trans WHERE passenger_id={p_id} AND bus_id={b_id}"
    try:
        cursor.execute(query2)
        valid = cursor.fetchall()
        if valid:
            cursor.execute(query, (p_id, b_id, c_d))
        else:
            messagebox.showerror("Error","You have never travelled from this bus.")
            return
        connection.commit()
        messagebox.showinfo("Register Successful", "Complain information updated successfully.")
        for widget in frame.winfo_children():
            widget.destroy()
        complain()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database update error: {err}")
    finally:
        cursor.close()

def search_buses():
    start_stop = start_entry.get().strip()
    end_stop = end_entry.get().strip()
    if not validate_non_empty_fields(start_entry, end_entry):
        messagebox.showerror("Invalid Input", "Please enter both starting and ending stopages.")
        return

    cursor = connection.cursor()
    query = """SELECT bus_name FROM bus WHERE 
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    AND
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    """

    query2 = """SELECT bus_name FROM bus WHERE 
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    OR
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    """

    query3 = """SELECT bus_name, stopage1, stopage2, stopage3, stopage4, stopage5, stopage6, 
                        stopage7, stopage8, stopage9, stopage10 FROM bus WHERE 
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    OR
        (stopage1 = %s OR stopage2 = %s OR stopage3 = %s OR stopage4 = %s OR stopage5 = %s OR
         stopage6 = %s OR stopage7 = %s OR stopage8 = %s OR stopage9 = %s OR stopage10 = %s)
    """

    params = [start_stop] * 10 + [end_stop] * 10
    params2 = [start_stop] * 10 + [end_stop] * 10

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()

        for widget in results_frame.winfo_children():
            widget.destroy()

        if results:
            for bus in results:
                bus_label = customtkinter.CTkLabel(master=results_frame, text=f"{bus[0]}\n____________________", font=("Roboto", 18))
                bus_label.pack(pady=20, padx=20)
        else:
            error_label=customtkinter.CTkLabel(master=results_frame, text=f"No buses found.\nSuggestions:\n", font=("Roboto", 18))
            error_label.pack(pady=20, padx=20)
            cursor.execute(query3, params2)
            results = cursor.fetchall()

            if results:
                for bus in results:
                    bus_name = bus[0]
                    stopages = [stop for stop in bus[1:] if stop]  
                    stopages_text = ">> ".join(stopages)
                    bus_label = customtkinter.CTkLabel(
                        master=results_frame,
                        text=f"Bus: {bus_name}\nStops: {stopages_text}\n____________________",
                        font=("Roboto", 18),
                        wraplength=500, 
                        justify="left"
                    )
                    bus_label.pack(pady=20, padx=20)
            else:
                messagebox.showerror("Error","No buses found")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database query error: {err}")
    finally:
        cursor.close()


def bus_search():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stoppages")
    x = cursor.fetchall()  
    stoppage = []  
    for s in x:
        stoppage.append(s[0])  
    cursor.close()
    reset_frame()
    search_label = customtkinter.CTkLabel(master=frame,text="Search Bus",font=("Roboto",24))
    search_label.pack(pady=10)
    global start_entry
    start_label = customtkinter.CTkLabel(master=frame,text="Starting Stopage",font=("Roboto",18))
    start_label.pack(pady=10)
    start_entry = customtkinter.CTkOptionMenu(frame, values=stoppage)
    start_entry.pack(pady=5)
    global end_entry
    end_label = customtkinter.CTkLabel(master=frame, text="Ending Stopage:", font=("Roboto", 18))
    end_label.pack(pady=10)
    end_entry = customtkinter.CTkOptionMenu(frame, values=stoppage)
    end_entry.pack(pady=5)
    search_button = customtkinter.CTkButton(master=frame, text="Search Buses", command=search_buses)
    search_button.pack(pady=20)
    global results_frame
    results_frame = customtkinter.CTkFrame(master=frame)
    results_frame.pack(pady=20,padx=20)
    back_btn = customtkinter.CTkButton(master=frame, text="Back",width=50, font=("Roboto", 14), command=main_screen)
    back_btn.place(x=10, y=10)

def transactions():
    reset_frame()
    t_l = customtkinter.CTkLabel(master=frame, text="See Transactions", font=("Roboto", 24))
    t_l.pack(pady=12, padx=10)
    global pa_id
    pa_id = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Unique Passenger ID", width=200)
    pa_id.pack(pady=12, padx=10)
    tn_btn = customtkinter.CTkButton(master=frame, text="Proceed", font=("Roboto", 20), command=transaction_proceed)
    tn_btn.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", width=50, font=("Roboto", 14), command=main_screen)
    back_btn.place(x=10, y=10)

def transaction_proceed():
    try:
        ps_id = int(pa_id.get()) 
        reset_frame()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM trans WHERE passenger_id = %s", (ps_id,))
        trans = cursor.fetchall()  
        if trans:  
            tree = ttk.Treeview(frame, columns=("Transaction ID", "Date", "Passenger ID","Bus ID", "Amount"), show="headings", height=10)
            tree.heading("Transaction ID", text="Transaction ID")
            tree.heading("Date", text="Date")
            tree.heading("Passenger ID", text="Passenger ID")
            tree.heading("Bus ID", text="Bus ID")
            tree.heading("Amount", text="Amount")
            tree.column("Transaction ID", width=120, anchor='center')
            tree.column("Date", width=100, anchor='center')
            tree.column("Passenger ID", width=120, anchor='center')
            tree.column("Bus ID", width=120, anchor='center')
            tree.column("Amount", width=100, anchor='center')
            tree.pack(pady=50, padx=20, anchor='center')
            for transaction in trans:
                tree.insert("", "end", values=transaction)
            back_btn = customtkinter.CTkButton(master=frame, text="Back", width=50, font=("Roboto", 14), command=transactions)
            back_btn.place(x=10, y=10)        
        else:
            no_trans_label = customtkinter.CTkLabel(master=frame, text="No transactions found for this ID.", font=("Roboto", 18))
            no_trans_label.pack(pady=20, padx=20)
            back_btn = customtkinter.CTkButton(master=frame, text="Back", width=50, font=("Roboto", 14), command=transactions)
            back_btn.place(x=10, y=10)
    except ValueError:
        error_label = customtkinter.CTkLabel(master=frame, text="Please enter a valid Passenger ID.", font=("Roboto", 18))
        error_label.pack(pady=20, padx=20)
        transaction()
    except mysql.connector.Error as err:
        error_label = customtkinter.CTkLabel(master=frame, text=f"Database error: {err}", font=("Roboto", 18))
        error_label.pack(pady=20, padx=20)
        transactions()
    finally:
        cursor.close()
 
def user():
    reset_frame()
    label = customtkinter.CTkLabel(master=frame,text="Passenger Portal",font=("Roboto",18))
    label.pack()
    bus_search_button = customtkinter.CTkButton(master=frame, text="Search Buses", command=bus_search)
    bus_search_button.pack(pady=12, padx=10)
    buy_ticket = customtkinter.CTkButton(master=frame,text="Buy Ticket",command=ticket_buy)
    buy_ticket.pack(pady=12,padx=10)
    see_balance = customtkinter.CTkButton(master=frame,text="See Balance",command=show_balance)
    see_balance.pack(pady=12,padx=10)
    trans = customtkinter.CTkButton(master=frame,text="Transactions",command=transactions)
    trans.pack(pady=12,padx=10)
    complain1 = customtkinter.CTkButton(master=frame,text="Complain",command=complain)
    complain1.pack(pady=12,padx=10)

def helper_login():
    reset_frame()
    start_label1 = customtkinter.CTkLabel(master=frame, text="Bus Number", font=("Roboto", 18))
    start_label1.pack(pady=10)
    global bus_no
    bus_no = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Bus Number", width=200)
    bus_no.pack(padx=12, pady=10)
    start_label = customtkinter.CTkLabel(master=frame, text="Password", font=("Roboto", 18))
    start_label.pack(pady=10)
    global helper_pass
    helper_pass = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Password", show="*", width=200)
    helper_pass.pack(padx=12, pady=10)
    check_box = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    check_box.pack()
    button = customtkinter.CTkButton(master=frame, text="Login", command=helper_login2)
    button.pack(pady=12, padx=10)
    back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=main_screen)
    back_btn.place(x=10, y=10)

def helper_login2():
    global b_n
    b_n=bus_no.get()
    global h_p
    h_p=helper_pass.get()
    if not validate_non_empty_fields(bus_no, helper_pass):
        messagebox.showerror("Invalid Input", "Please enter both username and password.")
        return
    
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM helper WHERE bus_no = %s AND helper_pass = SHA2(%s,512)"
        cursor.execute(query, (b_n, h_p))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Login Successful", "You are logged in!")
            for widget in frame.winfo_children():
                widget.destroy()
            show_dashboard()  
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database connection error: {err}")
    finally:
        helper_dashboard()


def helper_dashboard():
    reset_frame()
    global b_n2
    b_n2=b_n
    global h_p2
    h_p2=h_p
    label = customtkinter.CTkLabel(master=frame,text="Validate Ticket",font=("Roboto",18))
    label.pack()
    global qr
    qr=customtkinter.CTkEntry(master=frame,placeholder_text="Scan QR Code")
    qr.pack(padx=10,pady=12)
    check = customtkinter.CTkButton(master=frame,text="Check Ticket",command=check_ticket)
    check.pack(padx=10,pady=12)

def check_ticket():
    cursor = connection.cursor()
    try:
        ticket_id = int(qr.get())  
        cursor.execute("SELECT bus_id, check_ticket FROM tickets WHERE ticket_id=%s", (ticket_id,))
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror("Error", "Ticket ID not found.")
            helper_dashboard() 
            return  
        bus_id, check_status = result
        cursor.execute("SELECT bus_id FROM helper WHERE bus_no=%s", (b_n,))
        result3 = cursor.fetchone()
        reset_frame()
        if check_status == 1:
            messagebox.showerror("Used Ticket", "This ticket is already used.")
            helper_dashboard() 
            return  
        if result3 is None or result3[0] != bus_id:
            messagebox.showerror("Error", "The bus number does not match.")
            helper_dashboard()
            return  
        cursor.execute("SELECT * FROM tickets WHERE ticket_id=%s", (ticket_id,))
        result4 = cursor.fetchone()
        if result4 is None:
            messagebox.showerror("Error", "Ticket details could not be fetched.")
            helper_dashboard()
            return  
        label = customtkinter.CTkLabel(master=frame, text=f"Ticket id: {ticket_id}", font=("Roboto", 18))
        label.pack(padx=10, pady=12)
        label1 = customtkinter.CTkLabel(master=frame, text=f"Passenger id: {result4[1]}", font=("Roboto", 18))
        label1.pack(padx=10, pady=12)
        label2 = customtkinter.CTkLabel(master=frame, text=f"From: {result4[3]}", font=("Roboto", 18))
        label2.pack(padx=10, pady=12)
        label3 = customtkinter.CTkLabel(master=frame, text=f"To: {result4[4]}", font=("Roboto", 18))
        label3.pack(padx=10, pady=12)
        cursor.execute("UPDATE tickets SET check_ticket=1 WHERE ticket_id=%s", (ticket_id,))
        connection.commit() 
        back_btn = customtkinter.CTkButton(master=frame, text="Back", font=("Roboto", 14), width=50, command=helper_dashboard)
        back_btn.place(x=10, y=10)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid ticket ID.")
        helper_dashboard()  
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")
        helper_dashboard() 
    finally:
        cursor.close()

def main_screen():
    reset_frame()
    label = customtkinter.CTkLabel(master=frame, text="Bus Management System", font=("Roboto", 24))
    label.pack(pady=20)
    user()
    user_button = customtkinter.CTkButton(master=frame, text="Admin Login", command=admin)
    user_button.pack(padx=10,pady=12)
    helper_button = customtkinter.CTkButton(master=frame, text="Helper",command=helper_login)
    helper_button.pack(padx=10,pady=12)
    
root = customtkinter.CTk()
root.configure(bg_color='red')
root.geometry("500x500")
root.minsize(900,500)
root.maxsize(1000,800)
root.title("Local Bus Management System")
root.iconbitmap("bus.ico")
frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(padx=12, pady=10, fill="both", expand=True)
qr_label = customtkinter.CTkLabel(master=frame,text="")
qr_label.pack(pady=20)
main_screen()
root.mainloop()