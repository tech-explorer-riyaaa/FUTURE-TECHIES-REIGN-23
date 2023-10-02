from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class p1_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Aortic Valve Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Aortic Valve Surgery", font = ("goudy old style", 30, "bold", 'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Aortic Valve Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Our heart is a pump and needs healthy valves to function optimally. There are 4 valves in our heart, two located between the chambers
        (Mitral and Tricuspid) and the other two located between the chambers and blood vessels (Aortic and Pulmonary Valves). When open, the
        valves allow the blood to flow only in one direction; when closed, these valves form a strong seal between the different chambers of 
        heart as well as blood vessels.
        
        Aortic valve surgery is a surgical procedure that involves replacing a damaged or diseased aortic valve with an artificial valve. The 
        aortic valve is one of the four valves in the heart that regulates blood flow. It is located between the left ventricle and the aorta, 
        which is the largest artery in the body. Aortic valve surgery is typically performed in patients with severe aortic stenosis or 
        regurgitation, which are conditions that can cause heart failure if left untreated. During the surgery, the patient is placed under 
        general anesthesia, and the surgeon makes an incision in the chest to access the heart. The damaged valve is removed and replaced with 
        an artificial valve, which can be made from a variety of materials, including metal, plastic, or animal tissue.'''

        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"),fg='black',justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p1_class(root)
    root.mainloop()