from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymongo

class Brands:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+250+200")      # Width X Height + X-axis + Y-axis
        self.root.title("Brands")
        self.root.focus_force()

        # =============================================Variables========================================================

        self.var_brand_id = StringVar()
        self.var_name = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()

        # ===================================================Title======================================================

        title = Label(self.root,text="Brand Details",font=("arial",20,"bold"),bg="#FF87CA",fg="#1F1D36",bd=0).pack(side=TOP,fill=X)

        # ================================================Search Frame==================================================

        search_frame = LabelFrame(self.root,text="Search Brand",font=("arial",15,"bold"))
        search_frame.place(x=200,y=50,width=700,height=70)

        # ===================================================Options====================================================

        cmb_search = ttk.Combobox(search_frame,textvariable=self.var_search_by,values=("Select","Brand ID","Brand Name"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(search_frame,textvariable=self.var_search_txt,font=("arial",14),bg="#F9F9F9").place(x=200,y=10,width=300)
        btn_search = Button(search_frame,text="Search",command = self.search,bg="#FF87CA",fg="#1F1D36",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2",).place(x=505,y=10,width=120,height=26)

        # =============================================== Entry Labels =================================================

        brandID = Label(self.root,text="Brand",font=("arial",14,"bold"),bd=0).place(x=200,y=140)
        brandName = Label(self.root,text="Brand Name",font=("arial",14,"bold"),bd=0).place(x=510,y=140)

        # =============================================== Entries ======================================================
        

        txt_brandID = Entry(self.root,textvariable=self.var_brand_id,bg="#F9F9F9",font=("arial",15)).place(x=270,y=140)
        txt_brandName = Entry(self.root,textvariable=self.var_name,bg="#F9F9F9",font=("arial",15)).place(x=650,y=140)
        
        # =============================================== Add and Delete ===============================================
        
        btn_add = Button(self.root,command=self.add,text="Save",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=520,y=200,width=100,height=30)
        btn_delete = Button(self.root,command=self.delete,text="Delete",bg="#22577A",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=520,y=240,width=100,height=30)
        
        # =============================================== TreeView =====================================================

        cst_frame = Frame(self.root,bd=0,relief=RIDGE)
        cst_frame.place(x=200,y=200)

        scrolly = Scrollbar(cst_frame,orient=VERTICAL)
        scrollx = Scrollbar(cst_frame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11,"bold"),justify=CENTER)
        style.configure("Treeview", font=(None, 11),justify=CENTER)
        self.brandTable = ttk.Treeview(cst_frame,columns=("brandID","brandName"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.brandTable.xview)
        scrolly.config(command=self.brandTable.yview)

        self.brandTable.heading("brandID",text="Brand ID")
        self.brandTable.heading("brandName",text="Brand Name")
        self.brandTable["show"] = "headings"

        self.brandTable.column("brandID",width=120)
        self.brandTable.column("brandName",width=160)

        self.brandTable.pack(fill=Y,expand=1)
        self.brandTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        # ================================================= Image ======================================================

        # self.m1 = Image.open("icons/laptop-1.png")
        # self.m1 = self.m1.resize((300,200),Image.ANTIALIAS)
        # self.m1.place(x=200,y=500)

        self.load = Image.open("icons/laptop-4.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.render)
        self.img.place(x=650, y=200)

    
    def show(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["brandDetails"]
        all_data = collection.find({},{"_id":0}).sort("brandID")
        self.brandTable.delete(*self.brandTable.get_children())
        for i in all_data:
            list_ = list(i.values())
            self.brandTable.insert('',END,values=list_)

    def get_data(self,ev):
        j = self.brandTable.focus()
        content = (self.brandTable.item(j))
        row = content['values']
        self.var_brand_id.set(row[0]),
        self.var_name.set(row[1])
    
    # ================================================== Add Function ==================================================
    
    def add(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["brandDetails"]
        try:
            if self.var_brand_id.get() == "":
                messagebox.showerror("Error","brandID must be required",parent=self.root)
            else:
                one = collection.find_one({"brandID":self.var_brand_id.get()})
                if one is not None:
                    messagebox.showerror("Error","Sorry ID is already used , try using different one)",parent=self.root)
                else:
                    fields = {
                                "brandID":self.var_brand_id.get(),
                                "brandName":self.var_name.get(),
                             }
                    collection.insert_one(fields)
                    messagebox.showinfo(title="success",message="Account Succefully Created")
                    self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)
            
        # ================================================== Delete Function ==================================================
            
    def delete(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["brandDetails"]
        try:
            if self.var_brand_id.get() == "":
                messagebox.showerror("Error","brandID must be required",parent=self.root)
            else:
                one = collection.find_one({"brandID":self.var_brand_id.get()})
                if one is None:
                    messagebox.showerror("Error","Data Not Available",parent=self.root)
                else:
                    cst_id = self.var_brand_id.get()

                    option = messagebox.askyesno(message="Are You Sure , Data Will be lost permanently")
                    if option is True:
                        collection.delete_one({"brandID":cst_id})
                        messagebox.showinfo(title="success",message="Successfully Deleted",parent=self.root)
                        self.show()
                    else:
                        pass
                        self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)
            
    def clear(self):

        j = self.brandTable.focus()
        content = (self.brandTable.item(j))
        row = content['values']
        self.var_brand_id.set("")
        self.var_name.set("")
        self.var_search_txt.set("")
        self.var_search_by.set("Select")



    def search(self):
        i = 0
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["brandDetails"]
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
                if search_by == "Brand ID":
                    cst_id = collection.find_one({"brandID":search_field})
                    if cst_id is not None:
                        self.brandTable.delete(*self.brandTable.get_children())
                        only_data = collection.find_one(cst_id,{"_id":0})
                        list_ = list(only_data.values())
                        self.brandTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
                elif search_by == "Brand Name":
                    name = collection.find_one({"brandName":search_field})
                    if name is not None:
                        self.brandTable.delete(*self.brandTable.get_children())
                        only_data = collection.find_one(name,{"_id":0})
                        list_ = list(only_data.values())
                        self.brandTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The data doesn't Exist",parent=self.root)
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Brands(root)
    root.mainloop()


