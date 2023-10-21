''' Tried to make a program which collects data about vehicles from their drivers and allows multiple entries '''

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import xlsxwriter
from tkinter.ttk import *

master_list=list()
thing=None

def open_file():
    global file_path
    global what_file

    file_path = askopenfilename()
    what_file.config(text="File uploaded is "+file_path)

    if file_path is not None:
        pass

def clicked_submit():
    global thing

    if thing!=None:
        thing.after(1000, thing.destroy())

    main_dict=dict()
    main_dict["Name"]=name.get()
    main_dict["Company Name"]=comname.get()
    main_dict["Address"]=address.get()
    main_dict["PAN No."]=pan.get()
    main_dict["G.S.T No."]=gst.get()
    main_dict["Aadhaar Card No."]=aadhar.get()
    main_dict["Contact No."]=cont.get()
    main_dict["Reference Person"]=refer.get()
    main_dict["Reference Person's contact No."]=refercon.get()
    main_dict["Prefered roads from Chennai"]=prefroad.get()
    main_dict["Vehicle Type"]=typ.get()
    main_dict["Vehicle Ft"]=ft.get()
    main_dict["Vehicle Registration Number"]=vrn.get()
    main_dict["Documents"]=file_path

    master_list.append(main_dict)

    thing=Label(window,text="Data entered succesfully").grid(row = 15,column = 0)

def clicked_finish():
    workbook = xlsxwriter.Workbook('Final.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Serial No.")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "Company Name")
    worksheet.write(0, 3, "Address")
    worksheet.write(0, 4, "PAN No.")
    worksheet.write(0, 5, "G.S.T No.")
    worksheet.write(0, 6, "Aadhar card No.")
    worksheet.write(0, 7, "Contact No.")
    worksheet.write(0, 8, "Reference Person")
    worksheet.write(0, 9, "Reference person contact info")
    worksheet.write(0, 10, "Prefered Roads from Chennai")
    worksheet.write(0, 11, "Vehicle Type")
    worksheet.write(0, 12, "Vehicle Ft")
    worksheet.write(0, 13, "Vehicle Registration Number")
    worksheet.write(0, 14, "Documents")

    records=len(master_list)

    for i in range(records):
        record=master_list[i]
        worksheet.write(i+1, 0, i+1)
        worksheet.write(i+1,1,record["Name"])
        worksheet.write(i+1,2,record["Company Name"])
        worksheet.write(i+1,3,record["Address"])
        worksheet.write(i+1,4,record["PAN No."])
        worksheet.write(i+1,5,record["G.S.T No."])
        worksheet.write(i+1,6,record["Aadhaar Card No."])
        worksheet.write(i+1,7,record["Contact No."])
        worksheet.write(i+1,8,record["Reference Person"])
        worksheet.write(i+1,9,record["Reference Person's contact No."])
        worksheet.write(i+1,10,record["Prefered roads from Chennai"])
        worksheet.write(i+1,11,record["Vehicle Type"])
        worksheet.write(i+1,12,record["Vehicle Ft"])
        worksheet.write(i+1,13,record["Vehicle Registration Number"])
        worksheet.write(i+1,14,record["Documents"])

    workbook.close()

#def clicked_entered():
    #global thing2
    #global thing1

    #if thing!=None:
        #thing.after(1000, thing.destroy())
    #elif thing1!=None:
        #thing1.after(1000, thing.destroy())

    #for i in master_list:
        #useful="Vehicle Type:"+i["Vehicle Type"]+" Vehicle Ft:"+i["Vehicle Ft"]+" Vehicle Registration Number:"+i["Vehicle Registration Number"]+" Documents"+i["Documents"]
        #for j in range(len(master_list)):
            #thing1=Label(window,text=useful,font=("Times New Roman", 25)).grid(row=6+j,column=0,)


window = Tk()
window.title("Vehicle Registration")
window.geometry('2000x1000')
window.configure(background = "grey");

name=StringVar()
comname=StringVar()
address=StringVar()
pan=StringVar()
gst=StringVar()
aadhar=StringVar()
cont=StringVar()
refer=StringVar()
refercon=StringVar()
prefroad=StringVar()
typ=StringVar()
ft=StringVar()
vrn=StringVar()
do =StringVar()


k1 = Label(window ,text = "Name",font=("Times New Roman", 25)).grid(row = 0,column = 0)
k2 = Label(window ,text = "Company Name",font=("Times New Roman", 25)).grid(row = 1,column = 0)
k3 = Label(window ,text = "Address",font=("Times New Roman", 25)).grid(row = 2,column = 0)
k4 = Label(window ,text = "PAN No.",font=("Times New Roman", 25)).grid(row = 3,column = 0)
k5 = Label(window ,text = "G.S.T No.",font=("Times New Roman", 25)).grid(row = 4,column = 0)
k6 = Label(window ,text = "Aadhaar Card No.",font=("Times New Roman", 25)).grid(row = 5,column = 0)
k7 = Label(window ,text = "Contact No.",font=("Times New Roman", 25)).grid(row = 6,column = 0)
k8 = Label(window ,text = "Reference Person",font=("Times New Roman", 25)).grid(row = 7,column = 0)
k9 = Label(window ,text = "Reference Person's contact No.",font=("Times New Roman", 25)).grid(row = 8,column = 0)
k10 = Label(window ,text = "Prefered roads from Chennai",font=("Times New Roman", 25)).grid(row = 9,column = 0)
a = Label(window ,text = "Vehicle Type",font=("Times New Roman", 25)).grid(row = 10,column = 0)
b = Label(window ,text = "Vehicle Ft",font=("Times New Roman", 25)).grid(row = 11,column = 0)
c = Label(window ,text = "Vehicle Registration Number",font=("Times New Roman", 25)).grid(row = 12,column = 0)
d = Label(window ,text = "Documents",font=("Times New Roman", 25)).grid(row = 13,column = 0)

what_file=Label(window).grid(row = 13,column = 4)

k11 = Entry(window,textvariable=name,font=("Times New Roman", 25)).grid(row = 0,column = 2)
k22 = Entry(window,textvariable=comname,font=("Times New Roman", 25)).grid(row = 1,column = 2)
k33 = Entry(window,textvariable=address,font=("Times New Roman", 25)).grid(row = 2,column = 2)
k44 = Entry(window,textvariable=pan,font=("Times New Roman", 25)).grid(row = 3,column = 2)
k55 = Entry(window,textvariable=gst,font=("Times New Roman", 25)).grid(row = 4,column = 2)
k66 = Entry(window,textvariable=aadhar,font=("Times New Roman", 25)).grid(row = 5,column = 2)
k77 = Entry(window,textvariable=cont,font=("Times New Roman", 25)).grid(row = 6,column = 2)
k88 = Entry(window,textvariable=refer,font=("Times New Roman", 25)).grid(row = 7,column = 2)
k99 = Entry(window,textvariable=refercon,font=("Times New Roman", 25)).grid(row = 8,column = 2)
k1010 = Entry(window,textvariable=prefroad,font=("Times New Roman", 25)).grid(row = 9,column = 2)
a1 = Entry(window,textvariable=typ,font=("Times New Roman", 25)).grid(row = 10,column = 2)
b1 = Entry(window,textvariable=ft,font=("Times New Roman", 25)).grid(row = 11,column = 2)
c1 = Entry(window,textvariable=vrn,font=("Times New Roman", 25)).grid(row = 12,column = 2)


btn3 = ttk.Button(window ,text="Choose file",command=lambda:open_file()).grid(row=13,column=2)
btn = ttk.Button(window ,text="Submit",command=lambda:clicked_submit()).grid(row=14,column=0)
#btn1 = ttk.Button(window ,text="See Vehicles entered",command=lambda:clicked_entered()).grid(row=14,column=1)
btn2 = ttk.Button(window ,text="Finish",command=lambda:clicked_finish()).grid(row=14,column=2)


window.mainloop()
