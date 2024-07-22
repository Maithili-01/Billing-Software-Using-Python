from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x800+0+0")
        self.root.title("Billing Software")

        #Variables
        self.C_name=StringVar()
        self.C_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.C_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_Total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        


        #Product categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

        #SubCatClothing
        self.SubCatClothing=["Pant","T-shirt","Shirt"]
        self.pant=["Levis","CottonKing","Mufti","Spykar"]
        self.price_Levis=5000
        self.price_CottonKing=6000
        self.price_Mufti=4000
        self.price_Spykar=3000
        
        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_peter=2100
        self.price_louis=2700
        self.price_park=1740

        #SubCatLifStyle

        self.SubCatLifStyle=['Bath Soap','Face Cream','Hair oil']
        self.Bath_soap=['lifebuy','Lux','Santoor','Pears']
        self.price_lifebuy=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pears=30

        self.Face_cream=['Fair&Lovely','Ponds','Olay','Himalaya']
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=30
        self.price_himalaya=40

        self.Hair_oil=['Parashut','Jasmin','Bajaj','Almonddrop']
        self.price_parashut=25
        self.price_jasmin=28
        self.price_bajaj=30
        self.price_almond=45

        #SubCatMobiles

        self.SubCatMobiles=['Iphone','Samsung','Xiome','Realme','oneplus']
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']        
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']        
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiome=['Red11','Redme-12','RedmePro']        
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.Realme=['RealMe 12','RealMe 13','RealMe Pro']        
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.oneplus=['OnePlus1','OnePlus2','OnePlus3']        
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45800
        
        
        






        #Image1
        img=Image.open("image/pos-billing-screen.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)          #conver the high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #Image2
        img_1=Image.open("image/restro.jpg")
        img_1=img_1.resize((500,130),Image.Resampling.LANCZOS)          #conver the high level image to low level image
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        #Image3
        img_2=Image.open("image/b2.jpg")
        img_2=img_2.resize((320,130),Image.Resampling.LANCZOS)          #conver the high level image to low level image
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=320,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="White",fg="blue")
        lbl_title.place(x=0,y=130,width=1430,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1430,height=620)


        # Customer LabelFRame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.C_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entryCustName=ttk.Entry(Cust_Frame,textvariable=self.C_name,font=("arial",12,"bold"),width=24)
        self.entryCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,text="Email",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entryEmail=ttk.Entry(Cust_Frame,textvariable=self.C_email,font=("arial",10,"bold"),width=24)
        self.entryEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
         

        #Product labelframe
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
        #Category
        self.lblCategory=Label(Product_Frame,text="Select categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        #SubCategory
        self.lblSubCategory=Label(Product_Frame,text="Subcategory",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #ProductName
        self.lblproduct=Label(Product_Frame,text="ProductName",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26,state="readonly")
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        # middleFrame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        #Image1
        img12=Image.open("image/pos-billing-screen.jpg")
        img12=img12.resize((490,340),Image.Resampling.LANCZOS)          #conver the high level image to low level image
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        #Image2
        img13=Image.open("image/restro.jpg")
        img13=img13.resize((490,340),Image.Resampling.LANCZOS)          #conver the high level image to low level image
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=500,y=0,width=490,height=340)






        # Search

        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=10)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',7,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)






        # RightFrame Bill Aria
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=250,height=275)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter labelframe
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=320,width=1250,height=140)

        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=11,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    # ===========================================Function Declaration=====================================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t{self.qty.get()}\t\t{self.m}")
            self.sub_Total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100))) 
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100))))) 
    

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,"\n=========================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_Total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
            self.textarea.insert(END,"\n=========================")
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bill/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved sucessfully")
            f1.close()
    
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bill/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.C_name.set("")
        self.C_phon.set("")
        self.C_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_Total.set("")
        self.tax_input.set('')
        self.welcome()


    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWelcome to Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.C_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.C_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.C_email.get()}")

        self.textarea.insert(END,"\n=========================")
        self.textarea.insert(END,f"\nProducts\tQTY\tPrice")
        self.textarea.insert(END,"\n=========================")





    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifStyle)
            self.ComboSubCategory.current(0)
 
        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    
    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="T-shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
        

        # LifeStyle

        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

    
        #Mobile

        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)
        
        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="oneplus":
            self.ComboProduct.config(value=self.oneplus)
            self.ComboProduct.current(0)



    def price(self,event=""):
        #pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="CottonKing":
            self.ComboPrice.config(value=self.price_CottonKing)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_Mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_Spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Tshirt


        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)    
        
        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)   

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)     

        #shirt
        

        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_peter)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_louis)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_park)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        #bathsoap

        if self.ComboProduct.get()=="lifeBuy":
            self.ComboPrice.config(value=self.price_lifebuy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Pears":
            self.ComboPrice.config(value=self.price_pears)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        #facecream
        
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1) 
        
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1) 
        
        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1) 
        
        if self.ComboProduct.get()=="Himalaya":
            self.ComboPrice.config(value=self.price_himalaya)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        #oil
        
        if self.ComboProduct.get()=="Parashut":
            self.ComboPrice.config(value=self.price_parashut)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Jasmin":
            self.ComboPrice.config(value=self.price_jasmin)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1) 
        
        if self.ComboProduct.get()=="Almonddrop":
            self.ComboPrice.config(value=self.price_almond)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        #phone
        
        
        
        if self.ComboProduct.get()=="Iphone_X":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1) 


        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1) 
        
        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1) 

        
        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)





        


        







        







        
        
        
        
        
        
        




        
        


















        





    


    











      




if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()