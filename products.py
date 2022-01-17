from tkinter import *
from tkinter import ttk,messagebox
import pymongo

class Products:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+250+200")      # Width X Height + X-axis + Y-axis
        self.root.title("Products Details")
        self.root.focus_force()

        # ===========================Declaring Variables========================

        self.var_model_id = StringVar()
        self.var_model_name = StringVar()
        self.var_brand = StringVar()
        self.var_price = StringVar()
        self.var_cpu = StringVar()
        self.var_cpu = StringVar()
        self.var_ram = StringVar()
        self.var_rom = StringVar()
        self.var_screen = StringVar()
        self.var_os = StringVar()
        self.var_graphics = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()


        # =========================== Creating Frame ===========================
        productFrame = Frame(self.root,bd=0,relief=RIDGE)
        productFrame.place(x=10,y=10,width=500,height=480)

        # Title
        title = Label(productFrame,text="Product Details",font=("arial",16,"bold"),bg="#4E9F3D",fg="#fff").pack(side=TOP,fill=X)
        labelModelID = Label(productFrame,text="Model ID",font=("arial",16)).place(x=10,y=50)
        labelModelName = Label(productFrame,text="Model Name",font=("arial",16)).place(x=10,y=85)
        labelBrandID = Label(productFrame,text="Brand ID",font=("arial",16)).place(x=10,y=120)
        labelPrice = Label(productFrame,text="Price",font=("arial",16)).place(x=10,y=155)
        labelCpu = Label(productFrame,text="CPU",font=("arial",16)).place(x=10,y=190)
        labelRam = Label(productFrame,text="RAM",font=("arial",16)).place(x=10,y=225)
        labelRom = Label(productFrame,text="ROM",font=("arial",16)).place(x=10,y=260)
        labelScreen = Label(productFrame,text="Screen",font=("arial",16)).place(x=10,y=295)
        labelOs = Label(productFrame,text="OS",font=("arial",16)).place(x=10,y=330)
        labelGraphics = Label(productFrame,text="Graphics",font=("arial",16)).place(x=10,y=365)


        txt_ModelID = Entry(productFrame,textvariable=self.var_model_id,bg="#F9F9F9",font=("arial",15)).place(x=150,y=50,width=150)
        txt_ModelName = Entry(productFrame,textvariable=self.var_model_name,bg="#F9F9F9",font=("arial",15)).place(x=150,y=85,width=250)

        cmb_brandID = ttk.Combobox(productFrame,textvariable=self.var_brand,values=("Select","B01","B02","B03","B04","B05","B06","B07","B08","B09","B10"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_brandID.place(x=150,y=120,width=150)
        cmb_brandID.current(0)

        # txt_BrandID = Entry(productFrame,textvariable=self.var_brand,bg="#F9F9F9",font=("arial",15))

        txt_Price = Entry(productFrame,textvariable=self.var_price,bg="#F9F9F9",font=("arial",15)).place(x=150,y=155,width=150)
        txt_Cpu = Entry(productFrame,textvariable=self.var_cpu,bg="#F9F9F9",font=("arial",15)).place(x=150,y=190,width=250)

        cmb_Ram = ttk.Combobox(productFrame,textvariable=self.var_ram,values=("Select","2GB","4GB","8GB","12GB","16GB"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_Ram.place(x=150,y=225,width=150)
        cmb_Ram.current(0)

        txt_Rom = Entry(productFrame,textvariable=self.var_rom,bg="#F9F9F9",font=("arial",15)).place(x=150,y=260,width=350)
        txt_Screen = Entry(productFrame,textvariable=self.var_screen,bg="#F9F9F9",font=("arial",15)).place(x=150,y=295,width=350)

        cmb_os = ttk.Combobox(productFrame,textvariable=self.var_os,values=("Select","Windows10","Linux","macOS"),state="readonly",justify=CENTER,font=("arial",14))
        cmb_os.place(x=150,y=330,width=150)
        cmb_os.current(0)

        txt_Graphics = Entry(productFrame,textvariable=self.var_graphics,bg="#F9F9F9",font=("arial",15)).place(x=150,y=365,width=350)

        # =============================================== Buttons ======================================================

        btn_add = Button(productFrame,command=self.add,text="Save",bg="#4E9F3D",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=10,y=420,width=100,height=30)
        btn_update = Button(productFrame,command=self.update,text="Update",bg="#4E9F3D",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=140,y=420,width=100,height=30)
        btn_delete = Button(productFrame,command=self.delete,text="Delete",bg="#4E9F3D",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=270,y=420,width=100,height=30)
        btn_clear = Button(productFrame,command=self.clear,text="Clear",bg="#4E9F3D",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=400,y=420,width=100,height=30)
        # =============================================Search Frame ======================================================

        search_frame = LabelFrame(self.root,text="Search Products",font=("arial",15,"bold"))
        search_frame.place(x=530,y=10,width=550,height=60)

        # =============================================Search Bar ======================================================

        cmb_search = ttk.Combobox(self.root,textvariable=self.var_search_by,values=("Select","Model ID","Model Name"),state="readonly",justify=CENTER,font=("arial",11))
        cmb_search.place(x=540,y=40,width=120)
        cmb_search.current(0)

        txt_search = Entry(self.root,textvariable=self.var_search_txt,font=("arial",14),bg="#F9F9F9").place(x=665,y=38,width=300,height=26)
        btn_search = Button(self.root,command=self.search,text="Search",bg="#4E9F3D",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=970,y=37,width=100,height=26)

        # ==========================================Product Details=====================================================

        proFrame = Frame(self.root,bd=0,relief=RIDGE)
        proFrame.place(x=530,y=80,width=540,height=400)

        scrolly = Scrollbar(proFrame,orient=VERTICAL)
        scrollx = Scrollbar(proFrame,orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 11,"bold"))
        style.configure("Treeview", font=(None, 11))
        self.productTable = ttk.Treeview(proFrame,columns=("modelID","model","brandID","price","cpu","ram","rom","screen","os","graphics"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("modelID",text="Model ID")
        self.productTable.heading("model",text="Model Name")
        self.productTable.heading("brandID",text="Brand ID")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("cpu",text="CPU")
        self.productTable.heading("ram",text="RAM")
        self.productTable.heading("rom",text="ROM")
        self.productTable.heading("screen",text="Screen")
        self.productTable.heading("os",text="OS")
        self.productTable.heading("graphics",text="Graphics")

        self.productTable["show"] = "headings"

        self.productTable.column("modelID",width=120)
        self.productTable.column("model",width=160)
        self.productTable.column("brandID",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("cpu",width=220)
        self.productTable.column("ram",width=60)
        self.productTable.column("rom",width=180)
        self.productTable.column("screen",width=450)
        self.productTable.column("os",width=120)
        self.productTable.column("graphics",width=200)



        self.productTable.pack(fill=Y,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    def add(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["productDetails"]
        try:
            if self.var_model_id.get() == "":
                messagebox.showerror("Error","modelID must be required",parent=self.root)
            else:
                one = collection.find_one({"modelID":self.var_model_id.get()})
                if one is not None:
                    messagebox.showerror("Error","Sorry ID is already used , try using different one)",parent=self.root)
                else:
                    fields = {
                                "modelID":self.var_model_id.get(),
                                "model":self.var_model_name.get(),
                                "brandID":self.var_brand.get(),
                                "price":self.var_price.get(),
                                "cpu":self.var_cpu.get(),
                                "ram":self.var_ram.get(),
                                "rom":self.var_rom.get(),
                                "screen":self.var_screen.get(),
                                "os":self.var_os.get(),
                                "graphics":self.var_graphics.get(),}
                    collection.insert_one(fields)
                    messagebox.showinfo(title="success",message="Account Succefully Created")
                    self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def show(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["productDetails"]
        all_data = collection.find({},{"_id":0}).sort("modelID")
        self.productTable.delete(*self.productTable.get_children())
        for i in all_data:
            list_ = list(i.values())
            self.productTable.insert('',END,values=list_)

    def get_data(self,ev):
        j = self.productTable.focus()
        content = (self.productTable.item(j))
        row = content['values']
        self.var_model_id.set(row[0]),
        self.var_model_name.set(row[1]),
        self.var_brand.set(row[2]),
        self.var_price.set(row[3]),
        self.var_cpu.set(row[4]),
        self.var_ram.set(row[5]),
        self.var_rom.set(row[6]),
        self.var_screen.set(row[7]),
        self.var_os.set(row[8]),
        self.var_graphics.set(row[9])

    def update(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["productDetails"]
        try:
            if self.var_model_id.get() == "":
                messagebox.showerror("Error","modelID must be required",parent=self.root)
            else:
                one = collection.find_one({"modelID":self.var_model_id.get()})
                if one is None:
                    messagebox.showerror("Error","modelID not found)",parent=self.root)
                else:

                    pro_id = self.var_model_id.get()
                    pro_model = self.var_model_name.get()
                    pro_brand = self.var_brand.get()
                    pro_price = self.var_price.get()
                    pro_cpu = self.var_cpu.get()
                    pro_ram = self.var_ram.get()
                    pro_rom = self.var_rom.get()
                    pro_screen = self.var_screen.get()
                    pro_os = self.var_os.get()
                    pro_graphics = self.var_graphics.get()



                    prev = {"modelID":pro_id}
                    next1 = {"$set":{"model":pro_model}}
                    next2 = {"$set":{"brandID":pro_brand}}
                    next3 = {"$set":{"price":pro_price}}
                    next4 = {"$set":{"cpu":pro_cpu}}
                    next5 = {"$set":{"ram":pro_ram}}
                    next6 = {"$set":{"rom":pro_rom}}
                    next7 = {"$set":{"screen":pro_screen}}
                    next8 = {"$set":{"os":pro_os}}
                    next9 = {"$set":{"graphics":pro_graphics}}


                    collection.update_one(prev,next1)
                    collection.update_one(prev,next2)
                    collection.update_one(prev,next3)
                    collection.update_one(prev,next4)
                    collection.update_one(prev,next5)
                    collection.update_one(prev,next6)
                    collection.update_one(prev,next7)
                    collection.update_one(prev,next8)
                    collection.update_one(prev,next9)

                    messagebox.showinfo(title="success",message="Successfully Updated",parent=self.root)
                    self.show()

        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def delete(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["productDetails"]
        try:
            if self.var_model_id.get() == "":
                messagebox.showerror("Error","modelID must be required",parent=self.root)
            else:
                one = collection.find_one({"modelID":self.var_model_id.get()})
                if one is None:
                    messagebox.showerror("Error","Data Not Available",parent=self.root)
                else:
                    pro_id = self.var_model_id.get()
                    option = messagebox.askyesno(message="Are You Sure , Data Will be lost permanently")
                    if option is True:
                        collection.delete_one({"modelID":pro_id})
                        messagebox.showinfo(title="success",message="Successfully Deleted",parent=self.root)
                        self.show()
                    else:
                        pass
                        self.show()
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)

    def clear(self):
        j = self.productTable.focus()
        content = (self.productTable.item(j))
        row = content['values']
        self.var_model_id.set("")
        self.var_model_name.set("")
        self.var_brand.set("Select")
        self.var_price.set("")
        self.var_cpu.set("")
        self.var_ram.set("Select")
        self.var_rom.set("")
        self.var_screen.set("")
        self.var_os.set("Select")
        self.var_graphics.set("")
        self.var_search_txt.set("")
        self.var_search_by.set("Select")

    def search(self):
        i = 0
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client['laptopStore']
        collection = db["productDetails"]
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
                if search_by == "Model ID":
                    pro_id = collection.find_one({"modelID":search_field})
                    if pro_id is not None:
                        self.productTable.delete(*self.productTable.get_children())
                        only_data = collection.find_one(pro_id,{"_id":0})
                        list_ = list(only_data.values())
                        self.productTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The id data doesn't Exist",parent=self.root)
                elif search_by == "Model Name":
                    name = collection.find_one({"model":search_field})
                    if name is not None:
                        self.productTable.delete(*self.productTable.get_children())
                        only_data = collection.find_one(name,{"_id":0})
                        list_ = list(only_data.values())
                        self.productTable.insert('',END,values=list_)
                    else:
                        messagebox.showerror("Error","The model data doesn't Exist",parent=self.root)
        except Exception as Ex:
            messagebox.showerror("Error",f"Error due to : {str(Ex)}",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Products(root)
    root.mainloop()


