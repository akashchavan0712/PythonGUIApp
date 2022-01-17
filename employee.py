from tkinter import *
from PIL import Image,ImageTk                   # Necessary to install pillow library first
from tkinter import ttk,messagebox
import pymongo

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x550+250+200")      # Width X Height + X-axis + Y-axis
        self.root.title("Employee Details")
        self.root.focus_force()

        # ====================All Variables==================
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        self.var_emp_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_dob = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_doj = StringVar()
        self.var_salary = StringVar()

        # ========Search Frame================
        search_frame = LabelFrame(self.root,text="Search Employee",font=("arial",15,"bold"))
        search_frame.place(x=200,y=20,width=700,height=70)

        # ============Options=================

        cmb_search = ttk.Combobox(search_frame,textvariable=self.var_search_by,values=("Select","EmployeeID","Name","Email","Phone"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(search_frame,textvariable=self.var_search_txt,font=("arial",14),bg="#F9F9F9").place(x=200,y=10,width=300)
        btn_search = Button(search_frame,command=self.search,text="Search",bg="#A2416B",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=505,y=10,width=120,height=26)

        # ===========Title====================

        title = Label(self.root,text="Employee Details",font=("arial",15,"bold"),bg="#A2416B",fg="#fff").place(x=35,y=100,width=1000,height=30)

        # ============Content=================

        label_emp_id = Label(self.root,text="Emp ID",font=("arial",15)).place(x=30,y=150)
        label_gender = Label(self.root,text="Gender",font=("arial",15)).place(x=410,y=150)
        label_contact = Label(self.root,text="Contact",font=("arial",15)).place(x=750,y=150)

        txt_emp_id = Entry(self.root,textvariable=self.var_emp_id,bg="#F9F9F9",font=("arial",15)).place(x=110,y=150,width=100)

        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female",),state="readonly",justify=CENTER,font=("arial",14))
        cmb_gender.place(x=510,y=150,width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root,textvariable=self.var_contact,bg="#F9F9F9",font=("arial",15)).place(x=870,y=150,width=160)

        # =======================ROW2===========================

        label_name = Label(self.root,text="Name",font=("arial",15)).place(x=30,y=190)
        label_dob = Label(self.root,text="Birth Date",font=("arial",15)).place(x=410,y=190)
        label_doj = Label(self.root,text="Joining Date",font=("arial",15)).place(x=750,y=190)

        txt_name = Entry(self.root,textvariable=self.var_name,bg="#F9F9F9",font=("arial",15)).place(x=110,y=190,width=200)
        txt_dob = Entry(self.root,textvariable=self.var_dob,bg="#F9F9F9",font=("arial",15)).place(x=510,y=190,width=180)
        txt_doj = Entry(self.root,textvariable=self.var_doj,bg="#F9F9F9",font=("arial",15)).place(x=870,y=190,width=160)

        # =======================ROW3===========================

        label_email = Label(self.root,text="Email",font=("arial",15)).place(x=30,y=230)
        label_pass = Label(self.root,text="Password",font=("arial",15)).place(x=410,y=230)
        label_u_type = Label(self.root,text="User Type",font=("arial",15)).place(x=750,y=230)

        txt_email = Entry(self.root,textvariable=self.var_email,bg="#F9F9F9",font=("arial",15)).place(x=110,y=230,width=280)
        txt_pass = Entry(self.root,textvariable=self.var_pass,bg="#F9F9F9",font=("arial",15)).place(x=510,y=230,width=180)

        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee",),state="readonly",justify=CENTER,font=("arial",14))
        cmb_utype.place(x=870,y=230,width=160)
        cmb_utype.current(0)


        # =============Buttons=============

        btn_add = Button(self.root,command=self.add,text="Save",bg="#A2416B",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=600,y=270,width=100,height=30)
        btn_update = Button(self.root,command=self.update,text="Update",bg="#A2416B",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=710,y=270,width=100,height=30)
        btn_delete = Button(self.root,command=self.delete,text="Delete",bg="#A2416B",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=820,y=270,width=100,height=30)
        btn_clear = Button(self.root,command=self.clear,text="Clear",bg="#A2416B",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=930,y=270,width=100,height=30)

        # ===============Employee Details=============

        emp_frame = Frame(self.root,bd=0,relief=RIDGE)
        emp_frame.place(x=-10,y=320,width=1100,height=190)

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11,"bold"))
        style.configure("Treeview", font=(None, 11))
        self.employeeTable = ttk.Treeview(emp_frame,columns=("employeeID","name","email","gender","contact","dateOfBirth","dateofJoining","password","userType"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)

        self.employeeTable.heading("employeeID",text="Emp ID")
        self.employeeTable.heading("name",text="Name")
        self.employeeTable.heading("email",text="Email")
        self.employeeTable.heading("gender",text="Gender")
        self.employeeTable.heading("contact",text="Contact")
        self.employeeTable.heading("dateOfBirth",text="Birth Date")
        self.employeeTable.heading("dateofJoining",text="Joining Date")
        self.employeeTable.heading("password",text="Password")
        self.employeeTable.heading("userType",text="User Type")
        self.employeeTable["show"] = "headings"

        self.employeeTable.column("employeeID",width=75)
        self.employeeTable.column("name",width=130)
        self.employeeTable.column("email",width=190)
        self.employeeTable.column("gender",width=90)
        self.employeeTable.column("contact",width=110)
        self.employeeTable.column("dateOfBirth",width=100)
        self.employeeTable.column("dateofJoining",width=100)
        self.employeeTable.column("password",width=100)
        self.employeeTable.column("userType",width=100)

        self.employeeTable.pack(fill=Y,expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

# =============================================== Main Functions =====================================================
# fields = {"employeeID":"","employeeName":"","email":"","gender":"","contact":"","dateOfBirth":"","dateOfJoin":"","Password":"","userType":""}
#         fields = {
    #                   "employeeID":self.var_emp_id.get(),
    #                   "employeeName":self.var_emp_id.get(),
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
        collection = db["employeeDetails"]
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","employeeID must be required",parent=self.root)
            else:
                one = collection.find_one({"employeeID":self.var_emp_id.get()})
                if one is not None:
                    messagebox.showerror("Error","Sorry ID is already used , try using different one)",parent=self.root)
                else:
                    fields = {
                                "employeeID":self.var_emp_id.get(),
                                "employeeName":self.var_name.get(),
                                "email":self.var_email.get(),
                                "gender":self.var_gender.get(),
                                "contact":self.var_contact.get(),
                                "dateOfBirth":self.var_dob.get(),
                                "dateOfJoining":self.var_doj.get(),
                                "password":self.var_pass.get(),
                                "userType":self.var_utype.get()}
                    collection.insert_one(fields)
                    messagebox.showinfo(title="success",message="Account Succefully Created")
                    self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def show(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["employeeDetails"]
        all_data = collection.find({},{"_id":0}).sort("employeeID")
        self.employeeTable.delete(*self.employeeTable.get_children())
        for i in all_data:
            list_ = list(i.values())
            self.employeeTable.insert('',END,values=list_)

    def get_data(self,ev):
        j = self.employeeTable.focus()
        content = (self.employeeTable.item(j))
        row = content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8])

    def update(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["employeeDetails"]
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","employeeID must be required",parent=self.root)
            else:
                one = collection.find_one({"employeeID":self.var_emp_id.get()})
                if one is None:
                    messagebox.showerror("Error","Employee ID not found)",parent=self.root)
                else:

                    emp_id = self.var_emp_id.get()
                    emp_name = self.var_name.get()
                    emp_email = self.var_email.get()
                    emp_gender = self.var_gender.get()
                    emp_contact = self.var_contact.get()
                    emp_birthdate = self.var_dob.get()
                    emp_joindate = self.var_doj.get()
                    emp_password = self.var_pass.get()
                    emp_usertype = self.var_utype.get()

                    prev = {"employeeID":emp_id}
                    next1 = {"$set":{"employeeName":emp_name}}
                    next2 = {"$set":{"email":emp_email}}
                    next3 = {"$set":{"gender":emp_gender}}
                    next4 = {"$set":{"contact":emp_contact}}
                    next5 = {"$set":{"dateOfBirth":emp_birthdate}}
                    next6 = {"$set":{"dateofJoining":emp_joindate}}
                    next7 = {"$set":{"password":emp_password}}
                    next8 = {"$set":{"userType":emp_usertype}}

                    collection.update_one(prev,next1)
                    collection.update_one(prev,next2)
                    collection.update_one(prev,next3)
                    collection.update_one(prev,next4)
                    collection.update_one(prev,next5)
                    collection.update_one(prev,next6)
                    collection.update_one(prev,next7)
                    collection.update_one(prev,next8)

                    messagebox.showinfo(title="success",message="Successfully Updated",parent=self.root)
                    self.show()

        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def delete(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["employeeDetails"]
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","employeeID must be required",parent=self.root)
            else:
                one = collection.find_one({"employeeID":self.var_emp_id.get()})
                if one is None:
                    messagebox.showerror("Error","Data Not Available",parent=self.root)
                else:
                    emp_id = self.var_emp_id.get()

                    option = messagebox.askyesno(message="Are You Sure , Data Will be lost permanently")
                    if option is True:
                        collection.delete_one({"employeeID":emp_id})
                        messagebox.showinfo(title="success",message="Successfully Deleted",parent=self.root)
                        self.show()
                    else:
                        pass
                        self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def clear(self):
        j = self.employeeTable.focus()
        content = (self.employeeTable.item(j))
        row = content['values']
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Select")
        self.var_search_txt.set("")
        self.var_search_by.set("Select")

    def search(self):
        i = 0
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["employeeDetails"]
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
                if search_by == "EmployeeID":
                    emp_id = collection.find_one({"employeeID":search_field})
                    if emp_id is not None:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        only_data = collection.find_one(emp_id,{"_id":0})
                        list_ = list(only_data.values())
                        self.employeeTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                elif search_by == "Name":
                    emp_name = collection.find_one({"employeeName":search_field})
                    if emp_name is not None:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        only_data = collection.find_one(emp_name,{"_id":0})
                        list_ = list(only_data.values())
                        self.employeeTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                elif search_by == "Email":
                    emp_email = collection.find_one({"email":search_field})
                    if emp_email is not None:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        only_data = collection.find_one(emp_email,{"_id":0})
                        list_ = list(only_data.values())
                        self.employeeTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                else:
                    emp_contact = collection.find_one({"contact":search_field})
                    if emp_contact is not None:
                        self.employeeTable.delete(*self.employeeTable.get_children())
                        only_data = collection.find_one(emp_contact,{"_id":0})
                        list_ = list(only_data.values())
                        self.employeeTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()

