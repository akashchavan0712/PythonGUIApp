from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter import ttk,messagebox
import pymongo

class Purchases:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x630+250+150")      # Width X Height + X-axis + Y-axis
        self.root.title("Purchases")
        self.root.focus_force()

        # =============================================Variables========================================================

        self.var_model_id = StringVar()
        self.var_model_name = StringVar()
        self.var_brand = StringVar()
        self.var_price = StringVar()
        self.var_search_by = StringVar()
        self.var_search_txt = StringVar()
        self.billLists = []

        # ===================================================Title======================================================

        title = Label(self.root,text="Purchase Details",font=("arial",20,"bold"),bg="#AF0404",fg="#fff",bd=0).pack(side=TOP,fill=X)

        # ================================================Search Frame==================================================

        search_frame = LabelFrame(self.root,text="Search Purchases",font=("arial",15,"bold"))
        search_frame.place(x=10,y=40,width=750,height=70)

        # ==========================================Search Frame Content ===============================================

        invoice_search = Label(search_frame,text="Invoice Number :",font=("arial",14,"bold"),bd=0).place(x=5,y=10)

        txt_search = Entry(search_frame,textvariable=self.var_search_txt,font=("arial",14),bg="#F9F9F9").place(x=165,y=10,width=300)
        btn_search = Button(search_frame,command=self.search,text="Search",bg="#AF0404",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2",).place(x=475,y=10,width=100,height=28)

        btn_clear = Button(search_frame,command=self.clear,text="Clear",bg="#AF0404",fg="#fff",font=("arial",14,"bold"),bd=0,relief=RIDGE,cursor="hand2").place(x=580,y=10,width=100,height=28)

        # ======================================== Left Tree View (Sales Frame) ========================================

        salesFrame = Frame(self.root,bd=0,relief=RIDGE,bg="#F6DFEB")
        salesFrame.place(x=10,y=160,width=260,height=450)

        self.salesList = Listbox(salesFrame,bd=0,bg="#F6DFEB",font=('arial',15))

        # ============================================ Sales Area Label ================================================

        salesArea_title = Label(self.root,text="Invoice Area",font=("arial",20,"bold"),bg="#AF0404",fg="#fff",bd=0)
        salesArea_title.place(x=10,y=120,width=242,height=40)


        # ============================================= ScrollBar ======================================================

        scroll_y = Scrollbar(salesFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.salesList.yview)
        scroll_x = Scrollbar(salesFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.salesList.xview)
        self.salesList.pack(fill=BOTH,expand=1)
        self.salesList.bind("<ButtonRelease-1>",self.get_data)

        # ============================================ Right Tree View  ================================================


        # ============================================ Bill Area Frame =================================================

        billFrame = Frame(self.root,bd=0,relief=RIDGE,bg="#F6DFEB")
        billFrame.place(x=275,y=160,width=550,height=450)
        self.billList = Text(billFrame,bd=0,bg="#F6DFEB",font=('poppins',12))

        # ============================================ Bill Area Label =================================================

        billArea_title = Label(self.root,text="Customer Bills Area",font=("arial",20,"bold"),bg="#AF0404",fg="#fff",bd=0)
        billArea_title.place(x=275,y=120,width=532,height=40)

        # ============================================= ScrollBar ======================================================

        scroll1_y = Scrollbar(billFrame,orient=VERTICAL)
        scroll1_y.pack(side=RIGHT,fill=Y)
        scroll1_y.config(command=self.salesList.yview)
        scroll1_x = Scrollbar(billFrame,orient=HORIZONTAL)
        scroll1_x.pack(side=BOTTOM,fill=X)
        scroll1_x.config(command=self.salesList.xview)
        self.billList.pack(fill=BOTH,expand=1)


        # ============================================ ADDING IMAGE TO RIGHT ===========================================

        self.load = Image.open("icons/laptop-3.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.render,bd=0)
        self.img.place(x=820,y=120)

        self.load1 = Image.open("icons/laptop-4.png")
        self.render1 = ImageTk.PhotoImage(self.load1)
        self.img1 = Label(self.root, image=self.render1,bd=0)
        self.img1.place(x=820,y=350)

        self.show()

        # ====================================== Functions =============================================================

    def show(self):
        del self.billLists[:]
        self.salesList.delete(0,END)
        for i in os.listdir("Bills"):
            if (i.split('.')[-1]) == 'txt':
                self.billLists.append(i.split('.')[0])
                self.salesList.insert(END,i)

    def get_data(self,ev):
        index_ = self.salesList.curselection()
        file_name = self.salesList.get(index_)
        print(file_name)
        self.billList.delete('1.0',END)
        fp = open(f'Bills/{file_name}','r')
        for i in fp:
            self.billList.insert(END,i)
        fp.close()

    def search(self):
        if self.var_search_txt.get() == "":
            messagebox.showinfo("Error","Invoice No Should be Recquired",parent = self.root)
        else:
            if self.var_search_txt.get() in self.billLists:
                fp = open(f'Bills/{str(self.var_search_txt.get())}.txt','r')
                self.billList.delete('1.0',END)
                for i in fp:
                    self.billList.insert(END,i)
                fp.close()
            else:
                messagebox.showinfo("Invalid ID","There is not record with given ID")

    def clear(self):
        self.show()
        self.billList.delete('1.0',END)
        # ======================================= END OF THE PURCHASES CODE ============================================

if __name__ == "__main__":
    root = Tk()
    obj = Purchases(root)
    root.mainloop()

