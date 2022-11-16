import sqlite3 as sql  # Tickets Management
from csv import reader, writer  # User-Database
from os import listdir  # File Management
from random import choice, randint, randrange  # Randomised Simulation
from time import ctime, sleep  # Simulation
from tkinter import (GROOVE, Button, Entry, Label, StringVar,  # Visualization
                     Tk, Toplevel, messagebox)

__doc__ = """This is a module, created to honor the people working round the clock at the Air Traffic Control (ATC) tower, monitoring all flight activities and making air travel safe and worry free in today's contemporary world. Among the most important professions in the world, they also constitute fair percent of GDP to our country by facilitating air travel which in turn facilitates tourism, accomodating large number of tourists. This module has been created by us, who aspire in being a great coder in the near future and this project is a stepping stone to them in lieu with their great future. We are the students of Grade XII of Shalom Hills Int'l School, Gurgaon and we are driven towards our interest in coding due to our CS teacher Ms. Sarika Aneja, PGT in CS.
- Rohan Kurup (XII-B) & Bhavya Dhoot (XII-A)"""

wroval = "Please choose a valid option!" #Wrong value

###############################################################################################
###### File-read/write (Custom Functions) #####################################################
###############################################################################################
def logs(): #Initiate txt file if does not exist
    global a
    timestamper=ctime().replace(':','-')
    a = f"ATC_Logs {timestamper}.txt"
    while True:
        try:
            global f
            f = open(a, "r+")
            f.write(timestamper+'\n\n'); break
        except:
            with open(a, "w") as f: pass
logs()
def w_print(st): #write
    global f
    for line in st.split("\n"):
        print(line)
        f.write((line+'\n'))
def s_print(st): #slow
    global f
    for line in st.split('\n'):
        sleep(0.3)
        print(line)
        f.write((line+'\n'))
def w_input(st):
    global f
    print(st.strip(), end=""); inp = input()
    f.write(st.strip()+(inp+"\n"))
    return inp

###############################################################################################
########## SQL (Passenger's List Generator) ###################################################
###############################################################################################
def ticket(flight):
    opt = w_input(f"Do you want the passanger list for {flight} (y/n): ").lower()
    if opt or opt == "":
        flight = "F"+flight
        con = sql.connect(database="rohan.db")
        cur = con.cursor()
        try:
            c = 'CREATE TABLE '+flight+'(SNO TEXT(3),NAME TEXT(20), SEX TEXT(1), AGE TEXT(3),PASSPORT TEXT(15), RESERVATION TEXT(15))'
            cur.execute(c)
        except:
            c = 'DELETE FROM ' +flight
            cur.execute(c)
        for a in range(1, randint(80, 201)):  # s.no=no. of passengers
            b = randint(1, 2)
            if b == 1: b = chr(70)
            else: b = chr(77)
            if b == chr(70):  # name for girl
                namelst = ['Aadhya', 'Aanya', 'Aarna', 'Advika', 'Bhavna', 'Binita', 'Brinda', 'Chakrika', 'Chara', 'Chhaya', 'Daksha', 'Darika', 'Dhriti', 'Ekaja', 'Ekiya', 'Ela', 'Eshana', 'Eshika', 'Estaa', 'Falak', 'Forum', 'Gayathri', 'Geetika', 'Gulika', 'Hemal', 'Hemangini', 'Hiral', 'Idika', 'Ishani', 'Jeevika', 'Jiera', 'Kalki', 'Kashvi', 'Krisha', 'Laasya', 'Lekha', 'Maira', 'Mihika', 'Nyra', 'Oishi', 'Oorvi', 'Pihu', 'Prisha', 'Rabhya', 'Ridhi', 'Saira', 'Shravya', 'Turvi', 'Vrinda', 'Yashica']
                n2 = randint(0, 49) 
                name = namelst[n2] #random no for index
            else:  # name for boy
                namelst = ['Aakav', 'Aakesh', 'Aarav', 'Advik', 'Chaitanya', 'Chandran', 'Darpan', 'Darsh', 'Ekansh', 'Evak', 'Girik', 'Hemang', 'Hredhaan', 'Inesh', 'Ishaan', 'Jairaj', 'Jihan', 'Lekh', 'Lohit', 'Manbir', 'Mayan', 'Meet', 'Nihal', 'Nishit', 'Onkar', 'Onveer', 'Oviyan', 'Parijat', 'Pranit', 'Pranjal', 'Raghav', 'Rayaan', 'Reyansh', 'Ronit', 'Samaksh', 'Samesh', 'Sanat', 'Sanket', 'Tejas', 'Trijal', 'Tuhin', 'Udarsh', 'Umang', 'Vaidik', 'Vedant', 'Viraj', 'Yagnesh', 'Yash', 'Yatin', 'Yumraj']
                n2 = randint(0, 49)
                name = namelst[n2]
            age2 = str(randint(0, 80))
            g = randint(65, 90)
            hijklmn = str(randint(1000000, 9999999)) #Unpacking [Efficiency go BRRRRrrrr... ;)]
            o = randint(65, 90)
            pqrs = str(randint(1000, 9999))
            t = randint(65, 90)
            uv = str(randint(10, 99))
            pp = chr(g)+hijklmn+chr(o)+pqrs+chr(t)+uv  # random-passports
            g1 = randint(65, 90)
            hijklmn1 = str(randint(1000000, 9999999))
            o1 = randint(65, 90)
            pqrs1 = str(randint(1000, 9999))
            t1 = randint(65, 90)
            uv1 = str(randint(10, 99))
            pp1 = chr(g1)+hijklmn1+chr(o1)+pqrs1+chr(t1)+uv1  # random-reservations
            
            qwe2 = "INSERT INTO "+flight+' VALUES' + \
                '('+str(a)+',"'+name+'","'+b+'",'+age2+',"'+pp+'","'+pp1+'")'
            cur.execute(qwe2)
            con.commit()
        qwe3 = 'SELECT * FROM '+flight
        cur.execute(qwe3)
        qwe4 = cur.fetchall()
        if opt == 'y':
            print('*'*117)
            print("%5s" % "S.no", "%20s" % "Name", "%10s" % "Sex", "%15s" % "Age", '%30s' % 'Passport Number', '%30s' % 'Reservation Number') #txt formatting
        f.write('*'*117+'\n')
        a1 = ("%5s" % "S.no", "%20s" % "Name", "%10s" % "Sex", "%15s" % "Age", '%30s' % 'Passport Number', '%30s' % 'Reservation Number')
        f.writelines(a1); f.write("\n")
        f.write('*'*117+'\n')
        if opt == "y":
            print('*'*117+'\n')
        
        for i in qwe4:
            if opt == "y":
                print("%5s" % i[0], "%20s" % i[1], "%10s" % i[2], "%15s" % i[3], "%30s" % i[4], "%30s" % i[5])
            a2 = ("%5s" % i[0], "%20s" % i[1], "%10s" % i[2], "%15s" % i[3], "%30s" % i[4], "%30s" % i[5])
            f.writelines(a2); f.write("\n")
            if opt == "y":
                print('-'*117)
            f.write('-'*117+'\n')
            
###^#^#^#^ SQL (Passenger's List Generator) ^#^#^#^############################################

###############################################################################################
########## MAIN-PROGRAM (Terminal Phase) ######################################################
###############################################################################################

trips = {
        "Delhi - Jaipur"    :   ["SG2956", 'DHC-8', 'SpiceJet'],
        "Delhi - Goa"       :   ["UK847", 'A321', 'Vistara'],
        "Delhi - Nagpur"    :   ["6E6022", 'A320-271N', 'IndiGo'],
        "Delhi - Dubai"     :   ["EK9219", 'B777-F1H', 'Emirates'],
        "Delhi - Bengaluru" :   ["6E2188", 'A321-251NX', 'IndiGo'],
        "Delhi - Mumbai"    :   ["6E2138", 'A321-271NX', 'IndiGo'],
        "Delhi - Pune"      :   ["UK997", 'B737-8AL', 'Vistara'], #7

        "Jaipur - Delhi"    :   ["6E2175", 'A320-271N', 'IndiGo'],
        "Goa - Delhi"       :   ["I5779", 'A320-214', 'AirAsia'],
        "Nagpur - Delhi"    :   ["6E6022", 'A320-271N', 'IndiGo'],
        "Dubai - Delhi"     :   ["6E23", 'A320-251N', 'IndiGo'],
        "Bengaluru - Delhi" :   ["AI803", 'A321', 'Air India'],
        "Mumbai - Delhi"    :   ["AI605", 'A321', 'Air India'],
        "Pune - Delhi"      :   ["G8171", 'A320-271N', 'Go First'], #7

        "Jaipur - Haldwani" :   ["G8-142", '32A', 'Go First'],
        "Punjab - Lucknow"  :   ["AI0971", 'A320', 'Air India'],
        "Dubai - Goa"      :   ["AI2341", 'A320', 'Air India'],
        "Pune - Bengaluru"  :   ["AI247", 'A20N', 'Air India'] #4
        }

def run_gates_updater(): #Realtime Runway/Gates Usage Updater
    global count2, count
    if count2-count <= 1: pass
    else:
        try:    ele = run_use[0]; runways.append(ele); run_use.remove(ele); runways.sort()
        except: pass
        try:    ele2 = gates_use[0]; gates.append(ele2); gates_use.remove(ele2); gates.sort()
        except: pass; count2 -= 2; pass

gates     = ['G-01', 'G-02', 'G-03', 'G-04', 'G-05', 'G-06', 'G-07', 'G-08', 'G-09']
hangars   = ['H1', 'H3', 'H7', 'H8', 'H11', 'H13', 'H17', 'H18']
routes    = ['NAT 1', 'NAT 2', 'NAT 3', 'NAT 4', 'NAT 5']
runways   = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R8', 'R9']
run_use   = []
gates_use = []
ATCs      = ["Lucknow-LUK", "Jaipur-JAI", "Goa-GOI", "Nagpur-NAG", "Dubai-DXB", "Bengaluru-BLR", "Mumbai-BOM", "Pune-PNQ"]
def main(status, cur_flight):
    if status == "Request for Take-off": #Complete + Checked
        iterate = True
        gate = choice(gates)
        while iterate == True:
            cmd = w_input("Commands available (Ok/Wait): ").lower()
            if cmd == "ok":
                w_print("Command: OK")
                while iterate == True:
                    runway = w_input("Assign runway to take-off from ("+", ".join(runways)+"): ").upper()
                    if runway in runways:
                        s_print(f"Updated status: Taking off from {runway}\nLeaving from gate: {gate}") #Slow
                        run_use.append(runway); runways.remove(runway); gates_use.append(gate); gates.remove(gate)
                        while iterate == True:
                            alt = int(w_input("Enter the altitude to climb up to (5000-15000 ft)*: "))
                            if alt >= 5000 and alt <= 15000:
                                w_print(f"Climbing up to an altitude: {alt}")
                                while iterate == True:
                                    route = w_input("Enter route to be assigned ("+", ".join(routes)+"): ").upper()
                                    if route in routes:
                                        w_print(f'Route assigned: {route}')
                                        while iterate == True:
                                            atc = w_input("Enter the ATC to be handed over to ("+", ".join(ATCs)+"): ").upper()
                                            for atc_list in [i.split('-') for i in ATCs]: #because list is interlinked [[del], [jai]](Can be improved)
                                                if atc in atc_list:
                                                    w_print(f"Heading over to {atc_list[0]} ATC")
                                                    ticket(cur_flight)
                                                    sleep(0.3); iterate = False; break
                                                
                                            else: w_print(wroval)
                                    else: w_print(wroval)
                            else: w_print(wroval)
                    else: w_print(wroval)
            else: w_print("Command: WAIT"); sleep(1)
    elif status == 'Mayday! Request for emergency landing': #Complete + Checked
        iterate = True
        altitude = randrange(3000, 5000)
        w_print(f"Altitude: {altitude} ft")
        dist = randrange(1000, 2500)
        while iterate == True:
            route = w_input("Enter route to be assigned ("+", ".join(routes)+"): ").upper()
            if route in routes:
                s_print(f'Route assigned: {route}')
                s_print(f"Proximity from airport: {dist} KM\nRanways have been cleared. Land onto {route}")
                s_print("PROCEED WITH CAUTION\nFire Engines are being deployed\nAmbulances have been deployed")
                while iterate == True:
                    hangar = w_input("Hangars available are ("+", ".join(hangars)+"): ").upper()
                    if hangar in hangars:
                        s_print(f'Hangar {hangar} is assigned\nSituation solved\nHangar {hangar} is occupied indefinitely')
                        hangars.remove(hangar)
                        ticket(cur_flight)
                        sleep(0.3); iterate = False; break
                    else: w_print(wroval)
            else: w_print(wroval)
    elif status == 'Flight passing by. Handover to next ATC': #Complete + Checked
        iterate = True
        altitude = randrange(20000, 30000)
        w_print(f"Altitude: {altitude} ft")
        while iterate == True:
            route = w_input("Enter route to be assigned ("+", ".join(routes)+"): ").upper()
            if route in routes:
                s_print(f'Route assigned: {route}')
                while iterate == True:
                    atc = w_input("Enter the ATC to be handed over to ("+", ".join(ATCs)+"): ").upper()
                    for atc_list in [i.split('-') for i in ATCs]: 
                        if atc in atc_list:
                            w_print(f"Heading over to {atc.split()[0]} ATC")
                            ticket(cur_flight)
                            sleep(0.3); iterate = False; break
                    else: w_print(wroval)
            else: w_print(wroval)
    elif status == "Request for landing": #Complete + Checked
        iterate = True 
        altitude = randrange(3000, 5000)
        w_print(f"Altitude: {altitude} ft")
        while iterate == True:
            cmd = w_input("Enter command to be given (Ok/Turn Around): ").lower()
            if cmd == 'ok':
                w_print("Command: OK")
                while iterate == True:
                    runway = w_input("Assign runway to land on ("+str(", ".join(runways))+"): ").upper()
                    if runway in runways:
                        run_use.append(runway); runways.remove(runway)
                        s_print(f"Steady descent from {altitude} ft towards {runway}\nUpdated status: Landing in {runway}")
                        while iterate == True:
                            gate = w_input("Enter the gate to be assigned ("+", ".join(gates)+"): ").upper()
                            if gate in gates:
                                gates_use.append(gate); gates.remove(gate)
                                w_print(f"Heading to gate: {gate}")
                                ticket(cur_flight)
                                sleep(0.3); iterate = False; break
                            else: w_print(wroval)
                    else: w_print(wroval)
            elif cmd == 'turn around': 
                w_print("Command: Turn Around"); continue
            else: w_print(wroval)
    elif status == 'Passenger needs medic! Request for emergency landing': #Complete + Checked
        iterate = True
        altitude = randrange(3000, 5000)
        w_print(f"Altitude: {altitude} ft")
        while iterate == True:
            runway = w_input("Assign runway to land on ("+", ".join(runways)+"): ").upper()
            if runway in runways:
                run_use.append(runway); runways.remove(runway)
                w_print(f"Runway assigned: {runway}")
                while iterate == True:
                    gate = w_input("Enter the gate to be assigned ("+", ".join(gates)+"): ").upper()
                    if gate in gates:
                        gates_use.append(gate); gates.remove(gate)
                        w_print(f"Heading to gate: {gate}")
                        s_print('Passenger is being treated\nPassenger is OK') #slow
                        ticket(cur_flight)
                        sleep(0.3); iterate = False; break
                    else: w_print(wroval)
            else: w_print(wroval)
    elif status == 'Low on fuel. Request for refuel': #Complete + Checked
        iterate = True
        altitude = randrange(3000, 5000)
        w_print(f"Altitude: {altitude} ft")
        while iterate == True:
            runway = w_input("Assign runway to land on ("+", ".join(runways)+"): ").upper()
            if runway in runways:
                run_use.append(runway); runways.remove(runway)
                w_print(f"Runway assigned: {runway}")
                while iterate == True:
                    gate = w_input("Enter the gate to be assigned ("+", ".join(gates)+"): ").upper()
                    if gate in gates:
                        gates_use.append(gate); gates.remove(gate)
                        s_print(f"Heading to gate: {gate}\nRefueling")
                        ticket(cur_flight)
                        sleep(0.3); iterate = False; break
                    else: w_print(wroval)
            else: w_print(wroval)
chances = [(0, 9), (10, 19), (20, 39), (40, 64), (65, 89), (90, 99)]        ######
def main_p():                                                                    #
    global trips, count, marker                                                  #
    s_print("\nInitiating terminal...\nEstablishing connection...\n\nAssuming role of Delhi ATC")
    s_print(f"\nHello, {username1.capitalize()}\nWelcome to your day!\n\nATC MODULE:")
                                                                                 #
    while count >= -1: #Last iteration                                           #
        if count == -1: #End                                                     #
            s_print("\nAll flights for the day are taken care of.\nDay Ended")   #
            s_print(f"\n\nLog file exported as {a}")                             #
            f.close()                                                            #
            quit()                                                               #
        cur_trip = choice(list(trips.keys())) #3 cases are trip independant, for special cases it's redefined
        if len(chances) >= 1:                                                    #
            ini_choice = choice(chances)                                         #
            chance = choice(ini_choice)                                          # To ensure
            chances.remove(ini_choice)                                           # each case
        else:                                                                    # occurs(6)
            chance = randint(20, 39) # Define chance                        ######
        if chance >= 0 and chance <= 9: # Any Flight
            cur_stat = 'Passenger needs medic! Request for emergency landing'
        elif chance >= 10 and chance <= 19: #Any Flight
            cur_stat = 'Low on fuel. Request for refuel'
        elif chance >= 20 and chance <= 39: #Any Flight without Delhi
            cur_stat = 'Flight passing by. Handover to next ATC'
            cur_trip = choice(list(trips.keys())[14:len(trips)])
        elif chance >= 40 and chance <= 64: #Flights is cur_des == 'Delhi
            cur_stat = 'Request for landing'
            cur_trip = choice(list(trips.keys())[7:14])
        elif chance >= 65 and chance <= 89: #Flights is cur_loc == 'Delhi
            cur_stat = 'Request for Take-off'
            cur_trip = choice(list(trips.keys())[:7])
        else: # (chance of 10/100) Any Trip
            cur_stat = 'Mayday! Request for emergency landing'

        run_gates_updater()
        cur_flight, cur_flight_mod, cur_flight_airlines = trips[cur_trip] #Flight Number, Model, Airlines
        cur_flight_type = 'Domestic' 
        if 'Dubai' in cur_trip.split(" - "):
            cur_flight_type = 'International'
        w_print(f"""\nFlights for the day: {count+1}\n\nStatus: {cur_stat}\nFlight: {cur_flight}\nAirlines: {cur_flight_airlines}
Type: {cur_flight_type}\nTrip: {cur_trip}\nModel: {cur_flight_mod}""")
        # del trips[cur_trip]
        main(cur_stat, cur_flight)
        count -= 1

################################################################################################
########## Tkinter (Grphical Phase) ############################################################
################################################################################################

########## (reduce code redunduncy) ############################################################
def br(*screen, m=1):                                                                          #
    for i in range(m):    # m = multiplier                                                     #
        Label(*screen, text="", bg='white').pack()                                             #
def d_br(*screen):    # Dot-br                                                                 #
    Label(*screen, text="-"*160, font=("Gabriola", 20), bg='white').pack()                     #
def txt_label(txt, *screen, h=1):    # Regular Labels compressed to a function with formatings #
    Label(*screen, text=txt, width="300", height=h, font=("Gabriola", 24), bg='white').pack()  #
def tit_label(txt, *screen, h=1):                                                              #
    Label(*screen, text=txt, width="300", height=h, font=("Gabriola", 46), bg='white').pack()  #
################################################################################################

def login_sucess():
    messagebox.showinfo('Login Successful','User logged in successfully! Proceed to terminal...')
    screen2.destroy(); screen.destroy()
    f.write("\nLogin Successful. Proceeding to terminal\n")
    main_p()
def password_not_recognised():
    messagebox.showwarning('Error', 'Incorrect password...')
    f.write("Login Failed. Incorrect Password...\n")
def user_not_found():
    messagebox.showerror('Error', 'User not found. Please consider registering first...')
    f.write("Login Failed. User not found...\n")
def register_user():
    username_info = username.get()
    password_info = password.get()
    iterate = True
    while iterate == True:
        a = "ATC_Users.csv"
        try: 
            with open(a, "a+", newline="") as g:
                csv_w = writer(g)
                csv_w.writerow([username_info, password_info])
                messagebox.showinfo('Registration Complete', 'User registered successfully.')
                f.write(f"Registration Successful. Added user: {username_info}\n")
                screen1.destroy(); iterate = False; break   
        except:
            with open(a, "w+", newline="") as g:  #Create file with field-names
                csv_w = writer(g)
                csv_w.writerow(['username', 'password'])
def register():
    global screen2, screen1, br, d_br, tit_label, txt_label
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.config(bg='white')
    screen1.geometry("1920x1080")
    screen1.state('zoomed')
    global username, password, username_entry, password_entry, button_font
    username = StringVar()
    password = StringVar()
    tit_label("ENTER CREDENTIALS TO REGISTER", screen1, h=1)
    d_br(screen1)
    txt_label("Please enter your username.", screen1)
    txt_label("Username *:", screen1)
    username_entry = Entry(screen1, textvariable=username, relief=GROOVE, bd=2, font=("Gabriola", 25), bg='white').pack()
    br(screen1)
    txt_label("Please enter your password.", screen1)
    txt_label("Password *:", screen1)
    password_entry = Entry(screen1, textvariable=password, relief=GROOVE, bd=2, show='*', font=("Gabriola", 25), bg='white').pack()
    br(screen1, m=3)
    Button(screen1, text="Register", width='30', height='1', relief=GROOVE, command=register_user, font=(button_font, 25), bg='white', fg='dark green').pack()
def login_verify():
    global username1, username_entry1, password_entry1
    username1 = username_verify.get()
    password1 = password_verify.get()
    # del username_entry1, password_entry1
    list_of_files = listdir()
    a = "ATC_Users.csv"
    if a in list_of_files:
        with open(a, 'r+') as g:
            database = reader(g)
            database = list(database)
            for user in database: #Linked list [[U1, P1], [U2, P2]]
                if user[0] == username1: # Username exists
                    if user[1] == password1:
                        login_sucess()
                        break
                    else: 
                        password_not_recognised()
                        break
                else:
                    continue
            else: user_not_found()
    else: user_not_found() # No registrations yet
button_font = "OCR A Extended"
label_font = ""
def login():
    global screen1, button_font, screen2, br, d_br, txt_label, tit_label
    screen2 = Toplevel(screen)
    screen2.config(bg='white')
    screen2.title("Login")
    screen2.geometry("1920x1080")
    screen2.state('zoomed')
    tit_label("ENTER CREDENTIALS TO LOGIN", screen2, h=1); d_br(screen2)
    txt_label("Please enter your username.", screen2)
    global username_verify, password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1, password_entry1
    txt_label("Username *:", screen2)
    username_entry1 = Entry(screen2, textvariable=username_verify, bd=2, relief=GROOVE, font=("Gabriola", 25), bg='white').pack()
    br(screen2)
    txt_label("Please enter your password.", screen2)
    txt_label("Password *:", screen2)
    password_entry1 = Entry(screen2, textvariable=password_verify, bd=2, relief=GROOVE, show='*', font=("Gabriola", 25), bg='white').pack(); br(screen2, m=3)
    Button(screen2, text="Login", width="30", height="1", relief=GROOVE, command=login_verify, font=(button_font, 25), bg='white', fg='dark green').pack()
def ok1():
    screen0.destroy()
def about1():
    global screen0, button_font, d_br, txt_label, tit_label
    screen0 = Toplevel(screen)
    screen0.config(bg='white')
    screen0.title("About")
    screen0.geometry("1920x1080")
    screen0.state('zoomed')
    tit_label("ABOUT THE MODULE", screen0); d_br(screen0)
    txt_label("This is a module, created to honour the people who work round the clock at the Air Traffic Control (ATC) towers,", screen0)
    txt_label("monitoring all flight activities and making air travel safe and worry free in today's contemporary world.", screen0)
    txt_label("Among the most important professions in the world, they also constitute a fair percent of GDP to our country", screen0)
    txt_label("by facilitating air travel which in turn facilitates tourism, accommodates for a large number of tourists.", screen0)
    txt_label("This module has been created by us, who aspire in being a great coder in the near future and this project is a", screen0)
    txt_label("stepping stone to them in lieu with their great future. We are the students of Grade XII of Shalom Hills Int'l School,", screen0)
    txt_label("Gurgaon and we are driven towards our interest in coding due to our CS teacher Ms. Sarika Aneja, PGT in CS.", screen0)
    txt_label("- Rohan Kurup (XII-B) & Bhavya Dhoot (XII-A)", screen0); d_br(screen0)
    Button(screen0, text="OK", height="1", width="10", bg='white', bd=2, relief=GROOVE, activebackground='#ffcc33', font=(button_font, 25), command=ok1).pack()
def main_screen():
    global button_font, txt_label, tit_label, screen, d_br, br
    screen = Tk()
    screen.config(bg='white')
    screen.geometry("1920x1080")
    screen.title("ATC SIMULATOR")
    screen.state('zoomed')
    tit_label("ATC SIMULATOR"); d_br()
    txt_label("If you are an existing member, please login to experience the ATC simulator.", h=1)
    Button(text="Login", height="1", width="30", command=login, relief=GROOVE, activebackground='#8ad8ff', bg='white', font=(button_font, 25)).pack(); br(m=1); d_br()
    txt_label("If you are a new here, please register and then login to experience the ATC simulator.", h=1)
    Button(text="Register", height="1", width="30", command=register, relief=GROOVE, activebackground='#8ad8ff', bg='white', font=(button_font, 25)).pack(); br(m=1); d_br(); br(m=1)
    Button(text="About", height="1", width="10", bg='white', relief=GROOVE, activebackground='#8ad8ff', font=(button_font, 25), command=about1).pack(); br(m=1); d_br()
    screen.mainloop()
###^#^#^#^ Tkinter (Graphical Phase) ^#^#^#^###################################################

count2 = marker = count = 6
main_screen()

### Trips with flight detials have potential to repeat when same cases appear.
#08-11-22 (FINAL)
