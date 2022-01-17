from tkinter import *
from PIL import Image,ImageTk                   # Necessary to install pillow library first
from billing import Billing
from employee import Employee
from customer import Customer
from brands import Brands
from products import Products
from purchases import Purchases


class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x755+60+60")      # Width X Height + X-axis + Y-axis
        self.root.title("laptopStore")

        # Title
        self.iconTitle = PhotoImage(file="icons/storeIcon.png")
        title = Label(self.root,text="Laptop Store Management System",image=self.iconTitle,compound=LEFT,font=("arial",35),bg="#009DAE",fg="#fff",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=80)

        # Logout Button
        self.logoutButton = Button(self.root,text="Logout",font=("helvetica",15,"bold"),bg="#544179",fg="#fff",bd=0,cursor="hand2").place(x=1200,y=20)

        # Date and Time
        self.labelClock = Label(self.root,text="Welcome To Management System\t\t\t    Date: DD-MM-YYYY\t\t\t\t Time: HH:MM:SS",font=("arial",15),bg="#161E54",fg="#fff",anchor="w",padx=45)
        self.labelClock.place(x=0,y=75,relwidth=1,height=25)

        # Left Menu
        self.menuLogo = Image.open("icons/menuLogo.png")
        self.menuLogo = self.menuLogo.resize((180,180),Image.ANTIALIAS)
        self.menuLogo = ImageTk.PhotoImage(self.menuLogo)

        self.leftFrame = Frame(self.root,bd=0,relief=RIDGE,bg="#94DAFF")
        self.leftFrame.place(x=0,y=100,width=180,height=710)

        self.labelMenuLogo = Label(self.leftFrame,image=self.menuLogo)
        self.labelMenuLogo.pack(side=TOP,fill=X)

        # Left Menu Label

        self.leftFrameMenu = Label(self.root,text="Menu",font=("arial",15),bg="#544179",fg="#fff",bd=0).place(x=0,y=285,width=180,height=55)

        # Creating Buttons and Button Logo

        self.sideEmployeeIcon = PhotoImage(file="icons/employeeLogo.png")
        self.sideCustomerIcon = PhotoImage(file="icons/customerLogo.png")
        self.sideBrandsIcon = PhotoImage(file="icons/brandLogo.png")
        self.sideProductsIcon = PhotoImage(file="icons/productsLogo.png")
        self.sidePurchasesIcon = PhotoImage(file="icons/purchaseLogo.png")
        self.sideInventoryIcon = PhotoImage(file="icons/inventoryLogo.png")
        self.sideBillingIcon = PhotoImage(file="icons/billingLogo.png")
        self.sideExitIcon = PhotoImage(file="icons/exitLogo.png")

        self.employeeButton = Button(self.root,text="Employee",command=self.employee,image=self.sideEmployeeIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=338,width=180,height=55)
        self.customerButton = Button(self.root,text="Customers",command=self.customer,image=self.sideCustomerIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=392,width=180,height=55)
        self.brandsButton = Button(self.root,text="Brands",command=self.brands,image=self.sideBrandsIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=445,width=180,height=55)
        self.productsButton = Button(self.root,text="Products",command=self.products,image=self.sideProductsIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=495,width=180,height=55)
        self.purchasesButton = Button(self.root,text="Purchases",command=self.purchases,image=self.sidePurchasesIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=545,width=180,height=55)
        self.inventoryButton = Button(self.root,text="Inventory",image=self.sideInventoryIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=595,width=180,height=55)
        self.billingButton = Button(self.root,text="Billing",command=self.billing,image=self.sideBillingIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=645,width=180,height=55)
        self.exitButton = Button(self.root,text="Exit",image=self.sideExitIcon,compound=LEFT,padx=10,anchor="w",font=("arial",15),bg="#009DAE",fg="#fff",bd=1,cursor="hand2",relief=RIDGE).place(x=0,y=700,width=180,height=55)


        # Right Frame
        self.rightFrame = Frame(self.root,bd=0,relief=RIDGE,bg="#38A3A5")
        self.rightFrame.place(x=180,y=100,relwidth=180,relheight=710)

        # Content
        #
        # self.employeeLabel = Label(self.root,text="Total Employee\n[0]",bg="#521262",fg="#fff",font=("arial",20))
        # self.employeeLabel.place(x=380,y=250,width=250,height=150)
        #
        # self.customerLabel = Label(self.root,text="Total Customers\n[0]",bg="#CC0E74",fg="#fff",font=("arial",20))
        # self.customerLabel.place(x=630,y=250,width=250,height=150)
        #
        # self.productLabel = Label(self.root,text="Total Products\n[0]",bg="#8E05C2",fg="#fff",font=("arial",20))
        # self.productLabel.place(x=880,y=250,width=250,height=150)
        #
        # self.brandLabel = Label(self.root,text="Total Brands\n[0]",bg="#590D82",fg="#fff",font=("arial",20))
        # self.brandLabel.place(x=380,y=400,width=250,height=150)
        #
        # self.inventoryLabel = Label(self.root,text="Total Inventory\n[0]",bg="#821752",fg="#fff",font=("arial",20))
        # self.inventoryLabel.place(x=630,y=400,width=250,height=150)
        #
        # self.salesLabel = Label(self.root,text="Total Purchases\n[0]",bg="#B61AAE",fg="#fff",font=("arial",20))
        # self.salesLabel.place(x=880,y=400,width=250,height=150)

        self.load = Image.open("icons/Preview.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.render,bd=0)
        self.img.place(x=180,y=100)
# ======================================================================================================================

    def employee(self):
        self.newWin = Toplevel(self.root)
        self.newObj = Employee(self.newWin)

    def customer(self):
        self.newWin1 = Toplevel(self.root)
        self.newObj1 = Customer(self.newWin1)

    def brands(self):
        self.newWin2 = Toplevel(self.root)
        self.newObj2 = Brands(self.newWin2)

    def products(self):
        self.newWin3 = Toplevel(self.root)
        self.newObj3 = Products(self.newWin3)

    def purchases(self):
        self.newWin4 = Toplevel(self.root)
        self.newObj4 = Purchases(self.newWin4)

    # def inventory(self):
    #     self.newWin5 = Toplevel(self.root)
    #     self.newObj5 = Products(self.newWin5)

    def billing(self):
        self.newWin6 = Toplevel(self.root)
        self.newObj6 = Billing(self.newWin6)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
