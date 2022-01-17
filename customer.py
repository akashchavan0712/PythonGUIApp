from tkinter import *
from tkinter import ttk,messagebox
import pymongo

class Customer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1170x625+240+190")      # Width X Height + X-axis + Y-axis
        self.root.title("Customer Details")
        self.root.focus_force()


        # ====================All Variables==================
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        self.var_cst_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()

        # ========Search Frame================
        search_frame = LabelFrame(self.root,text="Search Customer",font=("arial",15,"bold"))
        search_frame.place(x=200,y=20,width=700,height=70)

        # ============Options=================

        cmb_search = ttk.Combobox(search_frame,textvariable=self.var_search_by,values=("Select","CustomerID","Name","Email","Phone"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(search_frame,textvariable=self.var_search_txt,font=("arial",14),bg="#F9F9F9").place(x=200,y=10,width=300)
        btn_search = Button(search_frame,command=self.search,text="Search",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=505,y=10,width=120,height=26)

        # ===========Title====================

        title = Label(self.root,text="Customer Details",font=("arial",15,"bold"),bg="#22577A",fg="#fff").place(x=35,y=100,width=1000,height=30)

        # ============Content=================

        label_cst_id = Label(self.root,text="Customer ID",font=("arial",15)).place(x=30,y=150)
        label_gender = Label(self.root,text="Gender",font=("arial",15)).place(x=410,y=150)
        label_contact = Label(self.root,text="Contact",font=("arial",15)).place(x=750,y=150)

        txt_cst_id = Entry(self.root,textvariable=self.var_cst_id,bg="#F9F9F9",font=("arial",15)).place(x=160,y=150,width=100)

        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female",),state="readonly",justify=CENTER,font=("arial",14))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root,textvariable=self.var_contact,bg="#F9F9F9",font=("arial",15)).place(x=830,y=150,width=205)

        # =======================ROW2===========================

        label_name = Label(self.root,text="Name",font=("arial",15)).place(x=30,y=190)
        txt_name = Entry(self.root,textvariable=self.var_name,bg="#F9F9F9",font=("arial",15)).place(x=160,y=190,width=200)

        # =======================ROW3===========================

        label_email = Label(self.root,text="Email",font=("arial",15)).place(x=30,y=230)
        txt_email = Entry(self.root,textvariable=self.var_email,bg="#F9F9F9",font=("arial",15)).place(x=160,y=230,width=320)


        # =============Buttons=============

        btn_add = Button(self.root,command=self.add,text="Save",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=600,y=270,width=100,height=30)
        btn_update = Button(self.root,command=self.update,text="Update",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=710,y=270,width=100,height=30)
        btn_delete = Button(self.root,command=self.delete,text="Delete",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=820,y=270,width=100,height=30)
        btn_clear = Button(self.root,command=self.clear,text="Clear",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=930,y=270,width=100,height=30)

        # ===============Employee Details=============

        cst_frame = Frame(self.root,bd=0,relief=RIDGE)
        cst_frame.place(x=-10,y=320,width=1100,height=250)

        scrolly = Scrollbar(cst_frame,orient=VERTICAL)
        scrollx = Scrollbar(cst_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11,"bold"),justify=CENTER)
        style.configure("Treeview", font=(None, 11),justify=CENTER)
        self.customerTable = ttk.Treeview(cst_frame,columns=("customerID","name","gender","email","contact"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.customerTable.xview)
        scrolly.config(command=self.customerTable.yview)

        self.customerTable.heading("customerID",text="CustomerID")
        self.customerTable.heading("name",text="Name")
        self.customerTable.heading("email",text="Email")
        self.customerTable.heading("gender",text="Gender")
        self.customerTable.heading("contact",text="Contact")
        self.customerTable["show"] = "headings"

        self.customerTable.column("customerID",width=120)
        self.customerTable.column("name",width=160)
        self.customerTable.column("email",width=220)
        self.customerTable.column("gender",width=100)
        self.customerTable.column("contact",width=120)

        self.customerTable.pack(fill=Y,expand=1)
        self.customerTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

# =============================================== Main Functions =====================================================
# fields = {"customerID":"","name":"","email":"","gender":"","contact":"","dateOfBirth":"","dateOfJoin":"","Password":"","userType":""}
#         fields = {
    #                   "customerID":self.var_cst_id.get(),
    #                   "name":self.var_cst_id.get(),
    #                   "email":self.var_email.get(),
    #                   "gender":self.var_gender.get(),
    #                   "contact":self.var_contact.get(),
    #                   "dateOfBirth":self.var_dob.get(),
    #                   "dateOfJoin":self.var_doj.get(),
    #                   "Password":self.var_pass.get(),
    #                   "userType":self.var_utype.get()
    #              }

    def add(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["customerDetails"]
        try:
            if self.var_cst_id.get() == "":
                messagebox.showerror("Error","customerID must be required",parent=self.root)
            else:
                one = collection.find_one({"customerID":self.var_cst_id.get()})
                if one is not None:
                    messagebox.showerror("Error","Sorry ID is already used , try using different one)",parent=self.root)
                else:
                    fields = {
                                "customerID":self.var_cst_id.get(),
                                "name":self.var_name.get(),
                                "gender":self.var_gender.get(),
                                "email":self.var_email.get(),
                                "contact":self.var_contact.get(),}
                    collection.insert_one(fields)
                    messagebox.showinfo(title="success",message="Account Succefully Created")
                    self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def show(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["customerDetails"]
        all_data = collection.find({},{"_id":0}).sort("customerID")
        self.customerTable.delete(*self.customerTable.get_children())
        for i in all_data:
            list_ = list(i.values())
            self.customerTable.insert('',END,values=list_)

    def get_data(self,ev):
        j = self.customerTable.focus()
        content = (self.customerTable.item(j))
        row = content['values']
        self.var_cst_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_email.set(row[3]),
        self.var_contact.set(row[4]),


    def update(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["customerDetails"]
        try:
            if self.var_cst_id.get() == "":
                messagebox.showerror("Error","customerID must be required",parent=self.root)
            else:
                one = collection.find_one({"customerID":self.var_cst_id.get()})
                if one is None:
                    messagebox.showerror("Error","Employee ID not found)",parent=self.root)
                else:

                    cst_id = self.var_cst_id.get()
                    cst_name = self.var_name.get()
                    cst_gender = self.var_gender.get()
                    cst_email = self.var_email.get()
                    cst_contact = self.var_contact.get()


                    prev = {"customerID":cst_id}
                    next1 = {"$set":{"name":cst_name}}
                    next2 = {"$set":{"gender":cst_gender}}
                    next3 = {"$set":{"email":cst_email}}
                    next4 = {"$set":{"contact":cst_contact}}


                    collection.update_one(prev,next1)
                    collection.update_one(prev,next2)
                    collection.update_one(prev,next3)
                    collection.update_one(prev,next4)

                    messagebox.showinfo(title="success",message="Successfully Updated",parent=self.root)
                    self.show()

        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def delete(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["customerDetails"]
        try:
            if self.var_cst_id.get() == "":
                messagebox.showerror("Error","customerID must be required",parent=self.root)
            else:
                one = collection.find_one({"customerID":self.var_cst_id.get()})
                if one is None:
                    messagebox.showerror("Error","Data Not Available",parent=self.root)
                else:
                    cst_id = self.var_cst_id.get()

                    option = messagebox.askyesno(message="Are You Sure , Data Will be lost permanently")
                    if option is True:
                        collection.delete_one({"customerID":cst_id})
                        messagebox.showinfo(title="success",message="Successfully Deleted",parent=self.root)
                        self.show()
                    else:
                        pass
                        self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def clear(self):
        j = self.customerTable.focus()
        content = (self.customerTable.item(j))
        row = content['values']
        self.var_cst_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_search_txt.set("")
        self.var_search_by.set("Select")



    def search(self):
        i = 0
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["customerDetails"]
        try:
            search_by = self.var_search_by.get()
            search_field = self.var_search_txt.get()
            if search_by == "Select":
                messagebox.showerror("Error","Select Search by Option",parent=self.root)
            elif search_field == "":
                messagebox.showerror("Error","Search Can't be left blank",parent=self.root)
            else:
                if self.var_search_txt.get() is None:
                    messagebox.showerror("Error","Nothing To Search",parent=self.root)
                if search_by == "CustomerID":
                    cst_id = collection.find_one({"customerID":search_field})
                    if cst_id is not None:
                        self.customerTable.delete(*self.customerTable.get_children())
                        only_data = collection.find_one(cst_id,{"_id":0})
                        list_ = list(only_data.values())
                        self.customerTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                elif search_by == "Name":
                    name = collection.find_one({"name":search_field})
                    if name is not None:
                        self.customerTable.delete(*self.customerTable.get_children())
                        only_data = collection.find_one(name,{"_id":0})
                        list_ = list(only_data.values())
                        self.customerTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                elif search_by == "Email":
                    cst_email = collection.find_one({"email":search_field})
                    if cst_email is not None:
                        self.customerTable.delete(*self.customerTable.get_children())
                        only_data = collection.find_one(cst_email,{"_id":0})
                        list_ = list(only_data.values())
                        self.customerTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                else:
                    cst_contact = collection.find_one({"contact":search_field})
                    if cst_contact is not None:
                        self.customerTable.delete(*self.customerTable.get_children())
                        only_data = collection.find_one(cst_contact,{"_id":0})
                        list_ = list(only_data.values())
                        self.customerTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Customer(root)
    root.mainloop()


