from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymongo

class Billing:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x678+60+60")    # Width X Height + X-axis + Y-axis
        self.root.title("Fuck You Peter")
        self.root.focus_force()

        # ===========================Declaring Variables========================

        self.var_model_id = StringVar()
        self.var_model_name = StringVar()
        self.var_brand_id = StringVar()
        self.var_quantity = StringVar()
        self.var_Status = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        # ===================================================Title======================================================

        self.iconTitle = PhotoImage(file="icons/storeIcon.png")
        title = Label(self.root,text="Laptop Store Management System",image=self.iconTitle,compound=LEFT,font=("arial",35),bg="#AA14F0",fg="#fff",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=80)

        # ============================================== Logout Button =================================================

        self.logoutButton = Button(self.root,text="Logout",font=("helvetica",15,"bold"),bg="#544179",fg="#fff",bd=0,cursor="hand2").place(x=1200,y=20)

        # =============================================== Date and Time ================================================

        self.labelClock = Label(self.root,text="Welcome To Management System\t\t\t    Date: DD-MM-YYYY\t\t\t\t Time: HH:MM:SS",font=("arial",15),bg="#161E54",fg="#fff",anchor="w",padx=45)
        self.labelClock.place(x=0,y=75,relwidth=1,height=25)

        # ================================================== Product Frame1 ==================================================

        ProductFrame1 = Frame(self.root,bd=0,relief=RIDGE,bg="#38A3A5")
        ProductFrame1.place(x=0,y=100,width=410,height=550)

        pTitle = Label(ProductFrame1,text="All Products",font=("helvetica",18,"bold"),bg="#544179",fg="#fff",bd=0)
        pTitle.place(x=0,y=0,relwidth=1)

        # ================================================= Product Frame2 ============================================

        ProductFrame2 = Frame(ProductFrame1,bg="#38A3A5",bd=1,relief=RIDGE)
        ProductFrame2.place(x=1,y=32,width=410,height=90)

        lbl_search = Label(ProductFrame2,text="Search Product Name",font=("helvetica",13,"bold"),bg="#38A3A5",bd=0)
        lbl_search.place(x=1,y=5,width=178,height=40)

        lbl_name = Label(ProductFrame2,text="Product Name :",font=("helvetica",13,"bold"),bg="#38A3A5",bd=0)
        lbl_name.place(x=3,y=45,width=125,height=40)

        txt_search = Entry(ProductFrame2,textvariable=self.var_search_txt,font=("arial",13),bg="#F9F9F9").place(x=130,y=50,width=180,height=26)
        btn_search = Button(ProductFrame2,text="Search",bg="#511845",fg="#fff",font=("arial",13,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=318,y=50,width=85,height=28)
        btn_search = Button(ProductFrame2,text="All Products",bg="#511845",fg="#fff",font=("arial",13,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=282,y=13,width=120,height=28)

        # ==============================================  Billing Details ==============================================

        left_frame = Frame(ProductFrame1,bd=0,relief=RIDGE)
        left_frame.place(x=0,y=120,width=430,height=450)

        scrolly = Scrollbar(left_frame,orient=VERTICAL)
        scrollx = Scrollbar(left_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11,"bold"),justify=CENTER)
        style.configure("Treeview", font=(None, 10),justify=CENTER)
        self.billingTable = ttk.Treeview(left_frame,columns=("modelID","model","brandID","quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.billingTable.xview)
        scrolly.config(command=self.billingTable.yview)

        self.billingTable.heading("modelID",text="Mo.ID")
        self.billingTable.heading("model",text="Model")
        self.billingTable.heading("brandID",text="Br.ID")
        self.billingTable.heading("quantity",text="Qty")
        self.billingTable.heading("Status",text="Status")
        self.billingTable["show"] = "headings"

        self.billingTable.column("modelID",width=50)
        self.billingTable.column("model",width=175)
        self.billingTable.column("brandID",width=50)
        self.billingTable.column("quantity",width=40)
        self.billingTable.column("Status",width=90)

        self.billingTable.pack(fill=Y,expand=1)
        self.billingTable.bind("<ButtonRelease-1>",self.get_data)

        self.title = Label(self.root,text="Enter '0' in quantity To Remove The Product ",font=("arial",13),bg="#38A3A5",fg="#fff")
        self.title.place(x=0,y=648,width=411,height=30)

        self.show()

    # ==================================================== Middle Frame ================================================

        middle_frame = Frame(self.root,bd=0,relief=RIDGE,bg="red")
        middle_frame.place(x=410,y=99,width=450,relheight=1)

    # ==================================================== Last Frame ================================================

        middle_frame = Frame(self.root,bd=0,relief=RIDGE,bg="green")
        middle_frame.place(x=860,y=99,relwidth=1,relheight=1)

    def show(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["inventoryDetails"]
        all_data = collection.find({},{"_id":0}).sort("modelID")
        self.billingTable.delete(*self.billingTable.get_children())
        for i in all_data:
            list_ = list(i.values())
            self.billingTable.insert('',END,values=list_)

    def get_data(self,ev):
        j = self.billingTable.focus()
        content = (self.billingTable.item(j))
        row = content['values']
        self.var_model_id.set(row[0]),
        self.var_model_name.set(row[1]),
        self.var_brand_id.set(row[2]),
        self.var_quantity.set(row[3]),
        self.var_Status.set(row[4]),



if __name__ == "__main__":
    root = Tk()
    obj = Billing(root)
    root.mainloop()
