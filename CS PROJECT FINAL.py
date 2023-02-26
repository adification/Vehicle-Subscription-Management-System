import datetime
import random

#NOTE
#PLEASE IGNORE SPELLING MISTAKES!!

#<------------<<<Universal List Declaration >>>------------>

name=[]#-------------list for customer name
mob=[]#-------------'list for customer phone number'''
add=[] #--------------list for customer adhress
checkin=[] # ---------'''list for take away date'''
checkout=[] #---------list for return date
sub=[]# -------------'''list for suscribed vehical'''
price=[] #--------------list for vehical price
carno=[]#--------------'''list for car number'''
custid=[] #--------------list for customer id
day=[]#----------------'''list for days suscribed '''
paymentcheck=[]#-------list for storing payment done data
pws=["admin123"]#------list for default'''
paid=[]#--------------'''list for online paid customers'''
cash=[]#--------------'''list for xash payment customers'''
caralp=[]#--------------'''list for car number'''
caralp2=[]#--------------'''list for car number'''
tax=[]

#<<<Universal Dictionary Declaration>>>
sco={'Honda Activa 6G':4999,'TVS Jupiter':5499,'Honda Dio':6499}
bi={'Hero HF Deluxe':5499,'Hero Passion Pro':5999,'Bajaj Pulsar 150':6999}
car={'Maruti Swift':10599,'Hyundai i20':11499,'Tata Tiago':10599}
suv={'Mahindra XUV300':16599,'Mahindra Bolero':13499,'Toyota Fortuner':16999}

#<<< Global Variable Declaration >>
i = 0

#<<----------------------------------------------------------------------------<<< # DEFAULT HOME PAGE>>>------------------------------------------------------------------------>> 
def Default():
        print("\t\t\t\t<<<|======================================|>>>")
        print("\t\t\t\t\t\t WELCOME TO my.VROOM")
        print("\t\t\t\t\t   Why To Purchase When You can Subscribe")
        print("\t\t\t\t<<<|======================================|>>>\n")
        print("\t\t\t-------------------------------------")
        print("\t\t\t USER")
        print("\t\t\t------------------------------------\n-")
        print("\t\t\t |1|-->AVAILABLE VEHICAL LIST\n")
        print("\t\t\t |2|-->SUBSCRIBE YOUR VEHICAL\n")
        print("\t\t\t |3|-->PAYMENT STATUS\n")
        print("\t\t\t |#|-->Any Number to exit\n")
        print("\t\t\t-------------------------------------")
        print("\t\t\t ADMIN")
        print("\t\t\t------------------------------------\n-")
        print("\t\t\t |4|-->ADMIN")
        print("\t\t\t-------------------------------------")
        ch=int(input("->"))
        if ch == 1:
                print(" ")
                vehicals()
        elif ch == 2:
                print(" ")
                Booking()
        elif ch == 3:
                print(" ")
                Payment()
        elif ch == 4:
                print(" ")
                Admin()
        else:
                print("Sorry To See You GO")
                exit()
#<<----------------------------------------------------------------------------<<< # Admin Function#>>>------------------------------------------------------------------------>> 
def Admin():
        pw=[]
        passwordhint=["Password Hint->>You know The Password"]
        inp=input("Enter Password:")
        print("")
        pw.append(inp)
        if pws==pw:
                print("                       1.Edit Vehical List")
                print("                       2. See Records")
                print("                       3. Change Payment Status")
                ch=int(input("->"))
                if ch == 1:
                        print(" ")
                        edit()
                elif ch ==2:
                        print(" ")
                        Data()
                elif ch ==3:
                        if mob==[]:
                                print("NO RECORDS")
                                n = int(input("9-TO GO HOME\n ->"))
                                if n ==9:
                                        Default()
                                else:
                                        exit()
                        else:
                                sl=int(input("Enter the sl. no of the customer:"))
                                cus=int(input("Enter the customer id of the customer:"))
                                print("")
                                print("Mark the above sl customer Paid or Not Paid")
                                print("y-->PAID")
                                print("n-->NOT PAID")
                                pp=str(input("->"))
                        if pp=='y':
                                paid.pop(sl)
                                paid.insert(sl,"PAID")
                                cash.remove(cus)
                                paymentcheck.append(cus)
                                Default()
                        elif pp=='n':
                                paid.pop(sl)
                                paid.insert(sl,"NOT PAID")
                                cash.append(cus)
                                paymentcheck.remove(cus)
                                Default()
        elif pws !=pw:
                print("PASSWORD WRONG!!!")
                print(passwordhint)
                print("")
                pc=str(input("Do you want to change password(y or n):"))
                print("")
                if pc=='y':
                        print("Please Give Your Admin ID")
                        ch=str(input("    ->"))
                        if ch=='adminisowner':
                                nw=input("     |^^Please Enter New Password:^^|->")
                                pws.clear()
                                pws.append(nw)
                                print("")
                                print(" <<New Password set to>>",pws)
                                Default()
                elif pc=="n":
                                Admin()
#<<----------------------------------------------------------------------------<<< # Editing Function#>>>------------------------------------------------------------------------>>
def edit():
        print("\t\t\t\t\t\t           -------------------------------------------       ")
        print("\t\t\t\t\t\t ------|EDITING SECTION my.VROOM (ADMIN)|------ ")
        print("\t\t\t\t\t\t           -------------------------------------------\n       ")
        print("\t\t\t-------------------------------------")
        print("\t\t\t (1)-->EDIT SCOOTER\n")
        print("\t\t\t (2)-->EDIT BIKE\n")
        print("\t\t\t (3)-->EDIT CAR\n")
        print("\t\t\t (4)-->EDIT SUV\n")
        print("\t\t\t (0)-->Home\n")
        print("\t\t\t-------------------------------------")
        ch=int(input("->"))
        if ch == 1:
              print("\t\t\t 1>>ADD\n")
              print("\t\t\t 2>>DELETE\n")
              ch=int(input("->"))
              if ch == 1:
                      print("Available Vehicals",sco)
                      einp=str(input(" Enter New Vehical :"))
                      einp2=str(input("Enter Price :"))
                      sco.setdefault(einp,einp2)
                      print("Yes Done")
                      print("Available Vehicals After Edit is",sco)
                      Default()
              elif ch == 2:
                      print("Available Vehicals",sco)
                      einp=str(input("Enter Vehical :"))
                      einp2=str(input("Enter Price :"))
                      sco.pop(einp,einp2)
                      print("Available Vehicals After Edit is",sco)
                      Default()
        elif ch == 2:
                print("\t\t\t 1>>ADD\n")
                print("\t\t\t 2>>DELETE\n")
                ch=int(input("->"))
                if ch == 1:
                      print("Available Vehicals",bi)
                      einp=str(input("Enter Vehical :"))
                      einp2=str(input("Enter Price :"))
                      bi.setdefault(einp,einp2)
                      print("Available Vehicals After Edit is",bi)
                      Default()
                elif ch == 2:
                        print("Available Vehicals",bi)
                        einp=str(input("Enter Vehical :"))
                        einp2=str(input("Enter Price :"))
                        bi.pop(einp,einp2)
                        print("Available Vehicals After Edit is",bi)
                        Default()
        elif ch == 3:
                print("\t\t\t 1>>ADD\n")
                print("\t\t\t 2>>DELETE\n")
                ch=int(input("->"))
                if ch == 1:
                        print("Available Vehicals",car)
                        einp=str(input("Enter Vehical :"))
                        einp2=str(input("Enter Price :"))
                        car.setdefault(einp,einp2)
                        print("Available Vehicals After Edit is",car)
                        Default()
                elif ch == 2:
                        print("Available Vehicals",car)
                        einp=str(input("Enter Vehical :"))
                        einp2=str(input("Enter Price :"))
                        car.pop(einp,einp2)
                        print("Available Vehicals After Edit is",car)
                        Default()
        elif ch == 4:
                print("\t\t\t 1>>ADD\n")
                print("\t\t\t 2>>DELETE\n")
                ch=int(input("->"))
                if ch == 1:
                        print("Available Vehicals",suv)
                        einp=str(input("Enter Vehical :"))
                        einp2=str(input("Enter Price :"))
                        suv.setdefault(einp,einp2)
                        print("Available Vehicals After Edit is",suv)
                        Default()
                elif ch == 2:
                        print("Available Vehicals",suv)
                        einp=str(input("Enter Vehical :"))
                        einp2=str(input("Enter Price :"))
                        suv.pop(einp,einp2)
                        print("Available Vehicals After Edit is",suv)
                        Default()
        elif ch == 0:
                Default()
#<<----------------------------------------------------------------------------<<< # VEHICAL CHART>>>------------------------------------------------------------------------>>

def vehicals(): 
	print("		 ------ AVAILABLE VEHICALS AT my.VROOM ------")
	print("...................................All prices below are on monthly(30 days) basis+TAX.................................|\n")
	print("||| 2-WHEELER SCOOTERS |||\n") 
	print("{Vehical:Price}")
	print(sco)
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::|\n")
	print("||| 2-WHEELER BIKES |||\n")
	print("{Vehical:Price}")
	print(bi)
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::|\n")
	print("||| 4-WHEELER CARS |||\n")
	print("{Vehical:Price}")
	print(car)
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::|\n")
	print("||| 4-WHEELER SUVs |||\n")
	print("{Vehical:Price}")
	print(suv)
	print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::|")
	print() 
	n=int(input("9-TO GO HOME\n ->")) 
	if n==9: 
		Default() 
	else: 
		exit()
#<----------------<<REFRESH FUNCTION>>------------------>
#To Empty The Data in list when input is wrong.

def refresh(c):
                print("\tDate Error Please Give Details Again\n")
                name.pop(c)
                mob.pop(c)
                add.pop(c)
                checkin.pop(c)
                checkout.pop(c)
                Booking()
 #<------------------------------------------------------------------>

                
#<<----------------------------------------------------------------------------<<< DATE ANALIZER FUNCTION>>>------------------------------------------------------------------------>>	
def date(c):
        #-------<<| 1=month | 2=year | 0=day |>>-------------
        if c[2] >= 2022 and c[2] <= 2030:
                if c[1] != 0 and c[1] <= 12:
                        if c[1] == 2 and c[0] != 0 and c[0] <= 31:#-------<<for checking leap year and february>>
                                if c[2]%4 == 0 and c[0] <= 29: 
                                        pass
                                elif c[0]<29:
                                        pass
                                else:
                                        refresh(i)
                                        Booking()
                        elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:#-------<<JAN/MARCH/MAY/JULY>>
                                pass
                        elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:#-------<<APRIL/JUNE>>
                                pass
                        elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:#-------<<AUG/OCT/DECEMBER>>
                                pass
                        elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:#-------<<SEPT/NOV>>
                                pass
                        else:
                                refresh(i)
                                Booking()
                else:
                        refresh(i)
                        Booking()
        else:
                refresh(i)
                Booking()

#<<----------------------------------------------------------------------------<<< BOOKING FUNCTION>>>------------------------------------------------------------------------>>				
def Booking():
        global i
        print("\t|.........SUBSCRIBE YOUR VEHICAL..........|")
        print(" ")
        while 1:
                _name_= str(input("\t| Name | --> "))
                _mobile_= str(input("\t| Mobile Number | --> "))
                _address_= str(input("\t| Address | -->"))

                #<<<IF ANYTHING IS LEFT BY THE USER>>>
                if _name_ !="" and _mobile_!="" and _address_!="":
                        name.append(_name_)
                        add.append(_address_)
                        mob.append(_mobile_)
                        break
                                        
                else:
                        print("\t\tWe Think You Have Left Something!!!") 
                                
        sd=str(input("\t|  Subscription Date(DD/MM/YYYY)  | -->-->")) 
        checkin.append(sd)
        sd=sd.split('/')
        sdd=sd
        sdd[0]=int(sdd[0])#<-------<<| 1=month | 2=year | 0=day |>>------------->
        sdd[1]=int(sdd[1])
        sdd[2]=int(sdd[2])

        rd=str(input("\t|  Return Date(DD/MM/YYYY)  | -->-->")) 
        checkout.append(rd)
        rd=rd.split('/')
        rdd=rd
        rdd[0]=int(rdd[0])
        rdd[1]=int(rdd[1])
        rdd[2]=int(rdd[2])
        #<<<Weather The dates are sequencely right or wrong>>>
        if rdd[1]<sdd[1] and rdd[2]<sdd[2]:
                print("\n\tError..!!\n\tYour Date Is Not In Sequence\n")
                refresh(i)
                Booking() 
        elif rdd[1]==sdd[1] and rdd[2]<=sdd[2] and rdd[0]<=sdd[0]:
                print("\n\tError..!!\n\tYour Date Is Not In Sequence\n")
                refresh(i)
                Booking()
        else:
                pass
		
        date(sdd)
        date(rdd)
        d1 = datetime.datetime(sdd[2],sdd[1],sdd[0])
        d2 = datetime.datetime(rdd[2],rdd[1],rdd[0])
        d = (d2-d1).days
        day.append(d)

        print("=========SELECT VEHICAL TYPE=========")
        print(" | 1-->SCOOTY")
        print(" | 2-->BIKE")
        print(" | 3-->CAR")
        print(" | 4-->SUV")
        print(("\t\tPress 0 for Car Subscription Prices"))

        ch=int(input("->"))

        if ch==0:
                print("{Vehical:Price}")
                print(sco)
                print(bi)
                print(car)
                print(suv)
                print("=========SELECT VEHICAL TYPE=========")
                print(" | 1-->SCOOTY")
                print(" | 2-->BIKE")
                print(" | 3-->CAR")
                print(" | 4-->SUV")
                ch=int(input("->"))
        if ch==1:
                print(sco)
                inp=str(input("Type the scooty name(PLZ TYPE EXACTLY SAME):"))
                sub.append(inp)
                print("Price Of Your Choice Is - ",sco[inp])
                price.append(sco[inp])
                tax.append(3.5)
        elif ch==2:
                print(bi)
                inp=str(input("Type the bike name(PLZ TYPE EXACTLY SAME):"))
                print("Price Of Your Choice Is - ",bi[inp])
                sub.append(inp)
                price.append(bi[inp])
                tax.append(4)
        elif ch==3:
                print(car)
                inp=str(input("Type the car name(PLZ TYPE EXACTLY SAME):"))
                print("Price Of Your Choice Is - ",car[inp])
                sub.append(inp)
                price.append(car[inp])
                tax.append(4.5)
        elif ch==4:
                print(suv)
                inp=str(input("Type the SUV name(PLZ TYPE EXACTLY SAME):"))
                print("Price Of Your Choice Is - ",suv[inp])
                sub.append(inp)
                price.append(suv[inp])
                tax.append(5)
        else:
                print(" Wrong choice..!!")

        #--------------------<<<randomly car no. and customer id>>>------------------
        rn = random.randrange(1000,10000)
        cid = random.randrange(0,51)
        alpha=random.randrange(65,91)
        alpha2=random.randrange(65,91)
        #--------------------<<<randomly car no. and customer id>>>------------------

        print("")
        print("\t\t\t   *** YOUR VEHICAL BOOKED SUCCESSFULLY***")
        print("\t\t\t******JUST ONE STEP TO GET YOUR VEHICAL******\n")
        print("VEHICAL No. - OD 07 ",chr(alpha),chr(alpha2),"",rn)
        print("Customer Id - ",cid)
        carno.append(rn)
        caralp.append(chr(alpha))
        caralp2.append(chr(alpha2))
        custid.append(cid)
        i=i+1
        n=int(input("0-TO PROCEED FOR PAYMENT\n ->"))
        if n==0:
                Payment() 
        else:
                exit
        
#<<-------------------------------------------<<< PAYMENT FUNCTION>>>----------------------------------------------------------->>			 
def Payment():
        print("|===========PAYMENT===========|\n")
        cus=int(input("CUSTOMER ID: "))
        global i
        
        if cus not in paymentcheck:
                if cus not in cash:
                         for n in range(0,i):
                                if cus==custid[n] :
                                        print(" |--------------------------------|")
                                        print("   MODE OF PAYMENT")
                                        print(" |--------------------------------|")
                                        print("   ONLINE")
                                        print(" |--------------------------------|")
                                        print(" | 1- Credit/Debit Card")
                                        print(" | 2- Paytm/PhonePe")
                                        print(" | 3- Using UPI")
                                        print(" |--------------------------------|")
                                        print("   OFFLINE")
                                        print(" |--------------------------------|")
                                        print(" | 4- Pay Later by cash")
                                        x=int(input("-> "))
                                        if x>0 and x<=3:
                                                paid.append("PAID")
                                                paymentcheck.append(cus)
                                        elif x==4:
                                                paid.append("NOT PAID")
                                                cash.append(cus)
                                        print(" --------------------------------")
                                        ea=((price[n]//30)*day[n])
                                        gst=(ea*(tax[n]/100))
                                        print("\n EXACT AMOUNT: ",ea,"\n")
                                        print("G.S.T-")
                                        print({ "3.5% Scooty", "4% Bike", "4.5% Car", "5%SUVs" })
                                        print("\n Price: ",ea)
                                        print(" G.S.T: ",gst,"\n")
                                        print(" Total Amount: ",gst+ea,"\n")
                                        print(" --------------------------------------------------------------")
                                        print("| Show Your Bill Slipt At our counter to get your vehical |")
                                        print("| If not paid you have to pay at counter                             |")
                                        print(" --------------------------------------------------------------\n")
                                        if x>0 and x<=3:
                                                acc=str(input("Give Your debit card number/Paytm Number/UPI ID->"))
                                                print("\n\n============================================|")
                                                print("		            My.Vroom")
                                                print("============================================|")
                                                print("			      Bill")
                                                print("============================================|\n")
                                                print(" Name: ",name[n],"\t\n Phone No.: ",mob[n],"\t\n Address: ",add[n],"\t")
                                                print("\n Car Number:  OR 07 ",caralp[n],caralp2[n],carno[n],"\t\n Customer ID: ",custid[n],"\t")
                                                print("\nTake Away Date: ",checkin[n],"\t\n Return Date: ",checkout[n],"\t")
                                                print("\n Time Of Subscription: ",day[n],"days""\t\n Vehical Price(30 Days): ",price[n],"\t")
                                                print("\n Status Of Payment: ",paid[n],)
                                                print("============================================|")
                                                print("\n Price: ",ea)
                                                print(" G.S.T: ",gst) 
                                                print(" Total Amount(Price+G.S.T): ",gst+ea)
                                                print("\n============================================|")
                                                print("		                Thank You")
                                                print("		Congratulations for new vehical :)")
                                                print("============================================|\n")
                                        elif x==4:
                                                print("\n\n============================================|")
                                                print("		            My.Vroom")
                                                print("============================================|")
                                                print("			      Bill")
                                                print("============================================|\n")
                                                print(" Name: ",name[n],"\t\n Phone No.: ",mob[n],"\t\n Address: ",add[n],"\t")
                                                print("\n Car Number:  OR 07 ",caralp[n],caralp2[n],carno[n],"\t\n Customer ID: ",custid[n],"\t")
                                                print("\nTake Away Date: ",checkin[n],"\t\n Return Date: ",checkout[n],"\t")
                                                print("\n Time Of Subscription: ",day[n],"days""\t\n Vehical Price(30 Days): ",price[n],"\t")
                                                print("\n Status Of Payment: ",paid[n],)
                                                print("============================================|")
                                                print("\n Price: ",ea)
                                                print(" G.S.T: ",gst) 
                                                print(" Total Amount(Price+G.S.T): ",gst+ea)
                                                print("\n============================================|")
                                                print("		                 Thank You")
                                                print("                 Congratulations for new vehical :)")
                                                print("============================================|\n")
                                elif cus!=custid[n] :
                                        print("\n\tSorry Customer Is Not in records :)\n\n")
                else:
                        print("You Have to Pay Cash At our Counter or your online payment failed")
        else:
                print("Payment Already Done")

               
       
        n = int(input("9-TO GO HOME\n ->"))
        if n == 9 :
                Default()
        else:
                exit()
#<<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->>

                
#<<----------------------------------------------------------------------------------------<<< # DATA FUNCTION>>>---------------------------------------------------------------------------------------->> 
def Data():
        # checks if any record exists or not
        if mob!=[]:
                print("______________________________________________________________________________________________________________________________________________________________________________________________________________________________________\n")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||*** CUSTOMER INFO ***||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                print("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
                for n in range(0,i):
                        print(".......................................................................................................................................................................................................................................................................................................................................................................................")
                        print("|SL.NO-",n,"|Customer ID: ",custid[n],"\t| NAME-",name[n],"\t| PHONE NO.-",mob[n],"\t| ADDRESS-",add[n],"\t| TAKE OUT-",checkin[n],"\t| RETURN-",checkout[n],"|")
                        print("| CAR NO.- OR 07",caralp[n],caralp2[n],carno[n],"\t| PRICE -",(price[n]/30)*day[n],"\t| PAYMENT STATUS-",paid[n],"|")
                        print("........................................................................................................................................................................................................................................................................................................................................................................................")
                n = int(input("9-TO GO HOME\n ->"))
                if n ==9:
                        Default()
                else:
                        exit()
        else:
                print("No Records Found")
                n = int(input("9-TO GO HOME\n ->"))
                if n ==9:
                        Default()
                else:
                        exit()
#<<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->> 
Default()
	               
