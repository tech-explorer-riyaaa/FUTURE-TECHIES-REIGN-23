from tkinter import *

from option1 import option1_class
from option2 import option2_class
from option3 import option3_class
from option4 import option4_class

from s1 import s1_class
from s2 import s2_class
from s3 import s3_class
from s4 import s4_class
from s5 import s5_class
from s6 import s6_class
from s7 import s7_class
from s8 import s8_class

from p1 import p1_class
from p2 import p2_class
from p3 import p3_class
from p4 import p4_class
from p5 import p5_class
from p6 import p6_class
from p7 import p7_class
from p8 import p8_class

from bmi import bmi_class

from PIL import Image,ImageTk

class SRM:
    def __init__(self,root):
        self.root = root
        self.root.title("Global Health Hospitals")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
##(Upload Images)
        self.bg_image = PhotoImage(file="bg1.png")
        self.label1 = Label(self.root,image=self.bg_image).place(x = 0, y = 30, width = 1280, height = 700)
        self.chatbot_img = Image.open("chatbot.png")
        self.chatbot_img = self.chatbot_img.resize((80, 80), Image.ANTIALIAS)
        self.chatbot_img = ImageTk.PhotoImage(self.chatbot_img)
##TITLE
        title = Label(self.root, text = "Global Health Hospitals", padx = 10, compound = LEFT,font = ("courier new", 35, "bold"), bg = "#003A70", fg = "white").place(x = 0, y = 0, relwidth = 1, height = 50)
        ambulance = Button(self.root, text = "Ambulance  \nHelp", font = ("courier new", 18, "bold"),justify=LEFT, bg = "#003A70", fg = "white").place(x = 1115, y = 280,width=200, height = 100)
        bmi = Button(self.root, text = "Find your  \nBMI now", font = ("courier new", 19, "bold"),justify=LEFT, bg = "#003A70", fg = "white",command=self.bmi).place(x = 1115, y = 420,width=200, height = 100)
        chatbot = Button(self.root, text = "CHAT\nBOT", compound = RIGHT,image = self.chatbot_img, font = ("courier new", 24, "bold","underline"), bg = "#003A70", fg = "white").place(x = 1115, y = 560, height = 100)
##Menu
        M_Frame = LabelFrame(self.root, text = "+", font = ("times new roman", 30,"bold"), bg = "#00a5bf",fg="white",border=10)
        M_Frame.place(x = 0, y = 50, width = 1280, height = 110)
##Buttons
        btn_1 = Button(M_Frame, text = "Book Appointment", font = ("corbel", 18, "bold"), bd = 3, bg = "light yellow", fg = "black", cursor = "hand2",command=self.option1).place(x = 80, y = 5, width = 250, height = 40)
        btn_2 = Button(M_Frame, text = "Request callback", font = ("corbel", 18, "bold"), bd = 3, bg = "light yellow", fg = "black", cursor = "hand2",command=self.option2).place(x = 360, y = 5, width =250, height = 40)
        btn_3 = Button(M_Frame, text = "Doctors", font = ("corbel", 18, "bold"), bd = 3, bg = "light yellow", fg = "black", cursor = "hand2",command=self.option3).place(x = 650, y = 5, width =200, height = 40)
        btn_4 = Button(M_Frame, text = "Hospitals", font = ("corbel", 18, "bold"), bd = 3, bg = "light yellow", fg = "black", cursor = "hand2",command=self.option4).place(x = 890, y = 5, width =200, height = 40)
        
        label_specialities  = Label(self.root, text = "Specialities", font = ("times new romen", 20, "bold","underline"), fg="#003A70", bg = "#ADD8E6").place(x = 200,y= 230)
        label_procedures  = Label(self.root, text = "Procedures", font = ("times new romen", 20, "bold","underline"), fg="#003A70", bg = "#ADD8E6").place(x = 630,y =230)
        
        btn_s1 = Button(text = "Cancer Care \n/ Oncology", font = ("corbel",12, "bold"),cursor = "hand2",command=self.s1).place(x =100, y = 300, width =150, height = 48)
        btn_s2 = Button(text = "Cardiac Sciences", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s2).place(x=100, y = 370, width =150, height = 45)
        btn_s3 = Button(text = "Orthopaedics &\n Joint Replacement", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s3).place(x = 100, y = 440, width =150, height = 48)
        btn_s4 = Button(text = "Gastroenterology,\n& Hepatology", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s4).place(x = 100, y = 510, width =150, height = 48)
        btn_s5 = Button(text = "Robotic ", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s5).place(x = 280, y = 300, width =150, height = 48)
        btn_s6 = Button(text = "Liver Transplant &\n Biliary Sciences", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s6).place(x = 280, y = 370, width =150, height = 48)
        btn_s7 = Button(text = "Neurosciences", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s7).place(x = 280, y = 440, width =150, height = 48)
        btn_s8 = Button(text = "Thoracic Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.s8).place(x = 280, y = 510, width =150, height = 48)

        btn_p1 = Button(text = "Aortic Valve\n Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p1).place(x = 530, y = 300, width =150, height = 48)
        btn_p2 = Button(text = "Da Vinci Robotic\n Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p2).place(x = 530, y = 370, width =150, height = 48)
        btn_p3 = Button(text = "Lung Transplant", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p3).place(x = 530, y = 440, width =150, height = 48)
        btn_p4 = Button(text = "LVAD Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p4).place(x = 530, y = 510, width =150, height = 48)
        btn_p5 = Button(text = "Knee Replacement\n surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p5).place(x = 730, y = 300, width =150, height = 48)
        btn_p6 = Button(text = "Bone Marrow\n Transplant", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p6).place(x = 730, y = 370, width =150, height = 48)
        btn_p7 = Button(text = "Thoracic Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p7).place(x = 730, y = 440, width =150, height = 48)
        btn_p8 = Button(text = "Bariatric Surgery", font = ("corbel",12, "bold"), cursor = "hand2",command=self.p8).place(x = 730, y = 510, width =150, height = 48)

##Footer
        footer = Label(self.root, text = "Contact @ 9911991199 | Email: help@globalhealthcare.com\n Global Health Care | 2023 | All Rights Reserved.", font = ("times new romen", 10), bg = "#262626", fg = "white").pack(side = BOTTOM, fill = X)

    def option1(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = option1_class(self.new_win)
    def option2(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = option2_class(self.new_win)
    def option3(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = option3_class(self.new_win)
    def option4(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = option4_class(self.new_win)   
        
    def s1(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s1_class(self.new_win) 
    def s2(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s2_class(self.new_win) 
    def s3(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s3_class(self.new_win) 
    def s4(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s4_class(self.new_win) 
    def s5(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s5_class(self.new_win) 
    def s6(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s6_class(self.new_win) 
    def s7(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s7_class(self.new_win) 
    def s8(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = s8_class(self.new_win) 
        
    def p1(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p1_class(self.new_win) 
    def p2(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p2_class(self.new_win) 
    def p3(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p3_class(self.new_win) 
    def p4(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p4_class(self.new_win) 
    def p5(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p5_class(self.new_win) 
    def p6(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p6_class(self.new_win) 
    def p7(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p7_class(self.new_win) 
    def p8(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = p8_class(self.new_win) 
 
    def bmi(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = bmi_class(self.new_win) 

if __name__ == "__main__":
    root = Tk()
    obj = SRM(root)
    root.mainloop()