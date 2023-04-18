from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital managment system")
        self.root.geometry("1540x800+0+0")

        # ..................................................take variable..................................................

        self.var_nameoftablets=StringVar()
        self.var_ref=StringVar()
        self.var_Dose=StringVar()
        self.var_NoofTablets=StringVar()
        self.var_Lot=StringVar()
        self.var_Issuedate=StringVar()
        self.var_Expdate=StringVar()
        self.var_Dailydose=StringVar()
        self.var_Sideeffect=StringVar()
        self.var_FurtherInformation=StringVar()
        self.var_BloodPressure=StringVar()
        self.var_StorageAdvice=StringVar()
        self.var_Medication=StringVar()
        self.var_PatientId=StringVar()
        self.var_NhsNumber=StringVar()
        self.var_PatientName=StringVar()
        self.var_DateofBirth=StringVar()
        self.var_PatientAddress=StringVar()

        # ....................................take frame................................................................


        labletitle=Label(self.root,bd=10,relief=RIDGE,text="HOSPITAL MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",30,"bold"))
        labletitle.pack(side=TOP,fill=X)
        dataframe=Frame(self.root,bd=10,relief=RIDGE)
        dataframe.place(x=0,y=110,width=1530,height=400)
        dataframeleft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="patient information")
        dataframeleft.place(x=0,y=5,width=900,height=350)
        dataframeright=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Precription")
        dataframeright.place(x=930,y=5,width=570,height=350)
        buttonframe = Frame(self.root, bd=10, relief=RIDGE)
        buttonframe.place(x=0, y=530, width=1530, height=60)
        detailframe = Frame(self.root, bd=10, relief=RIDGE)
        detailframe.place(x=0, y=600, width=1530, height=190)

        # .....................................take lable and text field hospitalleft side......................................
        labletable=Label(dataframeleft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        labletable.grid(row=0,column=0)
        comnametablet=ttk.Combobox(dataframeleft,textvariable=self.var_nameoftablets,font=("arial",12,"bold"),width=33)
        comnametablet["values"]=("Nice","corona vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comnametablet.grid(row=0,column=1)


        labref=Label(dataframeleft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        labref.grid(row=1,column=0,sticky=W)
        textref=Entry(dataframeleft,textvariable=self.var_ref,font=("arial",12,"bold"),width=35)
        textref.grid(row=1,column=1)

        labdose = Label(dataframeleft, font=("arial", 12, "bold"), text="Dose:", padx=2,pady=6)
        labdose.grid(row=2, column=0, sticky=W)
        textdose = Entry(dataframeleft, textvariable=self.var_Dose,font=("arial", 12, "bold"), width=35)
        textdose.grid(row=2, column=1)

        labnumtablet = Label(dataframeleft, font=("arial", 12, "bold"), text="No of Tablet", padx=2,pady=6)
        labnumtablet.grid(row=3, column=0, sticky=W)
        textnumtablet = Entry(dataframeleft,textvariable=self.var_NoofTablets, font=("arial", 12, "bold"), width=35)
        textnumtablet.grid(row=3, column=1)

        lablot = Label(dataframeleft, font=("arial", 12, "bold"), text="Lot:", padx=2,pady=6)
        lablot.grid(row=4, column=0, sticky=W)
        textlot = Entry(dataframeleft,textvariable=self.var_Lot, font=("arial", 12, "bold"), width=35)
        textlot.grid(row=4, column=1)

        labissuedate= Label(dataframeleft, font=("arial", 12, "bold"), text="Issue Date:", padx=2,pady=6)
        labissuedate.grid(row=5, column=0, sticky=W)
        textissuedate = Entry(dataframeleft, textvariable=self.var_Issuedate,font=("arial", 12, "bold"), width=35)
        textissuedate.grid(row=5, column=1)

        labexpdate = Label(dataframeleft, font=("arial", 12, "bold"), text="Exp Date:", padx=2,pady=6)
        labexpdate.grid(row=6, column=0, sticky=W)
        textexpdate = Entry(dataframeleft, textvariable=self.var_Expdate,font=("arial", 12, "bold"), width=35)
        textexpdate.grid(row=6, column=1)

        labdailydose = Label(dataframeleft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2,pady=6)
        labdailydose.grid(row=7, column=0, sticky=W)
        textdailydose = Entry(dataframeleft, textvariable=self.var_Dailydose,font=("arial", 12, "bold"), width=35)
        textdailydose.grid(row=7, column=1)


        labsideeffect = Label(dataframeleft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        labsideeffect.grid(row=8, column=0, sticky=W)
        textsideeffect = Entry(dataframeleft, textvariable=self.var_Sideeffect,font=("arial", 12, "bold"), width=35)
        textsideeffect.grid(row=8, column=1)

        labfurtherinfo = Label(dataframeleft, font=("arial", 12, "bold"), text="Further Information:", padx=2, pady=6)
        labfurtherinfo.grid(row=0, column=2, sticky=W)
        textfurtherinfo = Entry(dataframeleft, textvariable=self.var_FurtherInformation,font=("arial", 12, "bold"), width=33)
        textfurtherinfo.grid(row=0, column=3)

        labbloodpress = Label(dataframeleft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        labbloodpress.grid(row=1, column=2, sticky=W)
        textbloodpress = Entry(dataframeleft,textvariable=self.var_BloodPressure, font=("arial", 12, "bold"), width=33)
        textbloodpress.grid(row=1, column=3)

        labstoragead = Label(dataframeleft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        labstoragead .grid(row=2, column=2, sticky=W)
        textstoragead  = Entry(dataframeleft,textvariable=self.var_StorageAdvice, font=("arial", 12, "bold"), width=33)
        textstoragead .grid(row=2, column=3)

        labmedication = Label(dataframeleft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        labmedication.grid(row=3, column=2, sticky=W)
        textmedication= Entry(dataframeleft,textvariable=self.var_Medication, font=("arial", 12, "bold"), width=33)
        textmedication.grid(row=3, column=3)

        labpatientid = Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        labpatientid .grid(row=4, column=2, sticky=W)
        textpatientid  = Entry(dataframeleft, textvariable=self.var_PatientId,font=("arial", 12, "bold"), width=33)
        textpatientid .grid(row=4, column=3)

        labnhsnum = Label(dataframeleft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        labnhsnum.grid(row=5, column=2, sticky=W)
        textnhsnum = Entry(dataframeleft,textvariable=self.var_NhsNumber, font=("arial", 12, "bold"), width=33)
        textnhsnum.grid(row=5, column=3)

        labpatientname = Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        labpatientname.grid(row=6, column=2, sticky=W)
        textpatientname = Entry(dataframeleft,textvariable=self.var_PatientName, font=("arial", 12, "bold"), width=33)
        textpatientname.grid(row=6, column=3)

        labdob = Label(dataframeleft, font=("arial", 12, "bold"), text="Date od Birth:", padx=2, pady=6)
        labdob.grid(row=7, column=2, sticky=W)
        textdob = Entry(dataframeleft,textvariable=self.var_DateofBirth, font=("arial", 12, "bold"), width=33)
        textdob.grid(row=7, column=3)

        labpatientadd = Label(dataframeleft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        labpatientadd.grid(row=8, column=2, sticky=W)
        textpatientadd = Entry(dataframeleft, textvariable=self.var_PatientAddress,font=("arial", 12, "bold"), width=33)
        textpatientadd.grid(row=8, column=3)


        self.txtprescription=Text(dataframeright,font=("arial",12,"bold"),width=59,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

        # ...................................................button......................................................
        btnprescription = Button(buttonframe, text="Prescription",command=self.iprescription,fg="white",bg="green",padx=7,pady=15,font=("arial",12,"bold"),width=23)

        btnprescription.grid(row=0,column=0)

        btnprescriptiondata = Button(buttonframe, text="Prescription Data",command=self.prescriptdata, fg="white", bg="green", padx=7, pady=15,font=("arial",12,"bold"),width=23)

        btnprescriptiondata.grid(row=0, column=1)

        btnupdate= Button(buttonframe, text="Update", command=self.iupdate,fg="white", bg="green",
                                     font=("arial", 12, "bold"),padx=7, pady=15,width=23)
        btnupdate.grid(row=0, column=2)

        btndelete = Button(buttonframe, command=self.idelete,text="Delete", fg="white", bg="green",
                                     font=("arial", 12,"bold"), padx=7, pady=15,width=23)
        btndelete.grid(row=0, column=3)

        btnclear = Button(buttonframe, text="clear", command=self.iclear,fg="white", bg="green",
                                     font=("arial", 12, "bold"),padx=7, pady=15,width=23)
        btnclear.grid(row=0, column=4)

        btnexit = Button(buttonframe, text="Exit", command=self.iexit,fg="white", bg="green",
                                     font=("arial", 12, "bold"),padx=7, pady=15,width=23)
        btnexit.grid(row=0, column=5)

# .................................................scrollbar..................................................................

        scroll_x=ttk.Scrollbar(detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(detailframe,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","sideeffect","furtherinformation","bloodpressure","storageadvice","medication","patientid","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)



        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffect", text="Side Effect")
        self.hospital_table.heading("furtherinformation", text="Further Information")
        self.hospital_table.heading("bloodpressure", text="Blood Pressure")
        self.hospital_table.heading("storageadvice",text="Storage Advice")
        self.hospital_table.heading("medication", text="Madication")
        self.hospital_table.heading("patientid", text="Patient Id")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob",text="Date od Birth")
        self.hospital_table.heading("address",text="Patient Address")
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("sideeffect",width=100)
        self.hospital_table.column("furtherinformation", width=100)
        self.hospital_table.column("bloodpressure", width=100)
        self.hospital_table.column("storageadvice", width=100)
        self.hospital_table.column("medication", width=100)
        self.hospital_table.column("patientid", width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def prescriptdata(self):
        if self.var_nameoftablets.get()=="" or self.var_ref.get()=="":
                messagebox.showerror("error","All field are required",parent=self.root)
        else:
            try:

               conn=mysql.connector.connect(host="localhost",user="root",password="data1234",database="hospitalmanagment")
               d1=conn.cursor()
               d1.execute("insert into hospitaldata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
               self.var_nameoftablets.get(),self.var_ref.get(),self.var_Dose.get(),self.var_NoofTablets.get(),self.var_Lot.get(),self.var_Issuedate.get(),
               self.var_Expdate.get(),self.var_Dailydose.get(),self.var_Sideeffect.get(),self.var_FurtherInformation.get(),self.var_BloodPressure.get(),
               self.var_StorageAdvice.get(),self.var_Medication.get(),self.var_PatientId.get(),self.var_NhsNumber.get(),self.var_PatientName.get(),self.var_DateofBirth.get(),self.var_PatientAddress.get()))

               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("success", "hospital data details has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

                # ...................................................fetching data.......................................................

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="data1234", database="hospitalmanagment")
        d1 = conn.cursor()
        d1.execute("select * from hospitaldata")
        rows=d1.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        # ..................................................Highlite text cusror..........................................................

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.var_nameoftablets.set(row[0]),
        self.var_ref.set(row[1]),
        self.var_Dose.set(row[2]),
        self.var_NoofTablets.set(row[3]),
        self.var_Lot.set(row[4]),
        self.var_Issuedate.set(row[5]),
        self.var_Expdate.set(row[6]),
        self.var_Dailydose.set(row[7]),
        self.var_Sideeffect.set(row[8]),
        self.var_FurtherInformation.set(row[9]),
        self.var_BloodPressure.set(row[10]),
        self.var_StorageAdvice.set(row[11]),
        self.var_Medication.set(row[12]),
        self.var_PatientId.set(row[13]),
        self.var_NhsNumber.set(row[14]),
        self.var_PatientName.set(row[15]),
        self.var_DateofBirth.set(row[16]),
        self.var_PatientAddress.set(row[17])

        # ..............................................Update button..........................................................

    def iupdate(self):

         conn = mysql.connector.connect(host="localhost", user="root", password="data1234",
                                        database="hospitalmanagment")
         d1 = conn.cursor()
         d1.execute("update hospitaldata set Nameoftablets=%s,Dose=%s, Nooftablets=%s,Lot=%s,Issuedata=%s,Expdate=%s,Dailydose=%s,Sideeffect=%s,Furtherinformation=%s,Bloodpressure=%s,Storageadvice=%s,Medication=%s,Patientid=%s,Nhsnumber=%s,Patientname=%s,Dateofbirth=%s,Patientaddress=%s where Ref=%s",(
             self.var_nameoftablets.get(),
             self.var_Dose.get(),
             self.var_NoofTablets.get(),
             self.var_Lot.get(),
             self.var_Issuedate.get(),
             self.var_Expdate.get(),
             self.var_Dailydose.get(),
             self.var_Sideeffect.get(),
             self.var_FurtherInformation.get(),
             self.var_BloodPressure.get(),
             self.var_StorageAdvice.get(),
             self.var_Medication.get(),
             self.var_PatientId.get(),
             self.var_NhsNumber.get(),
             self.var_PatientName.get(),
             self.var_DateofBirth.get(),
             self.var_PatientAddress.get(),
             self.var_ref.get(),
         ))
         messagebox.showinfo("updated","recorded has been sucessfully")
         conn.commit()
         self.fetch_data()
         conn.close()


        # ...........................................Prescription text....................................................................



    def iprescription(self):
        self.txtprescription.insert(END,"Name of Tablets:\t\t\t" + self.var_nameoftablets.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t" + self.var_ref.get()+"\n")
        self.txtprescription.insert(END,"Dose:\t\t\t" + self.var_Dose.get()+"\n")
        self.txtprescription.insert(END,"No of Tablets:\t\t\t" + self.var_NoofTablets.get()+"\n")
        self.txtprescription.insert(END,"Lot:\t\t\t" + self.var_Lot.get()+"\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t" + self.var_Issuedate.get()+"\n")
        self.txtprescription.insert(END,"Exp Date:\t\t\t" + self.var_Expdate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t" + self.var_Dailydose.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t" + self.var_Sideeffect.get()+"\n")
        self.txtprescription.insert(END,"Further Information:\t\t\t" + self.var_FurtherInformation.get()+"\n")
        self.txtprescription.insert(END,"Blood Pressure:\t\t\t" + self.var_BloodPressure.get()+"\n")
        self.txtprescription.insert(END,"Storage Advice:\t\t\t" + self.var_StorageAdvice.get()+"\n")

        self.txtprescription.insert(END,"Medication:\t\t\t" + self.var_Medication.get()+"\n")
        self.txtprescription.insert(END,"Patient Id:\t\t\t" + self.var_PatientId.get()+"\n")

        self.txtprescription.insert(END,"NHS Number:\t\t\t" + self.var_NhsNumber.get()+"\n")
        self.txtprescription.insert(END,"Patient Name:\t\t\t" + self.var_PatientName.get()+"\n")
        self.txtprescription.insert(END,"DOB:\t\t\t" + self.var_DateofBirth.get()+"\n")
        self.txtprescription.insert(END,"Patient Address:\t\t\t" + self.var_PatientAddress.get()+"\n")

        # ...................................................Delete Button..........................................................

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="data1234",
                                       database="hospitalmanagment")
        d1 = conn.cursor()
        query="delete from hospitaldata where ref=%s"
        value=(self.var_ref.get(),)
        d1.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("delete","Patient has been sucessfully")

        # .................................................Clear button.........................................................

    def iclear(self):
        self.var_nameoftablets.set("")
        self.var_ref.set("")
        self.var_Dose.set("")
        self.var_NoofTablets.set("")
        self.var_Lot.set("")
        self.var_Issuedate.set("")
        self.var_Expdate.set("")
        self.var_Dailydose.set("")
        self.var_Sideeffect.set("")
        self.var_FurtherInformation.set("")
        self.var_BloodPressure.set("")
        self.var_StorageAdvice.set("")
        self.var_Medication.set("")
        self.var_PatientId.set("")
        self.var_NhsNumber.set("")
        self.var_PatientName.set("")
        self.var_DateofBirth.set("")
        self.var_PatientAddress.set("")

        # ...................................................Exit button.......................................................

    def iexit(self):
        iexit=messagebox.askyesno("hospital managmet system","confirm you want to exit")
        if iexit>0:
            root.destroy()
            return

root=Tk()
ob=Hospital(root)
root.mainloop()