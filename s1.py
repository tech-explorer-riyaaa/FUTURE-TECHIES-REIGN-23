from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class s1_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Cardiac Sciences", font = ("goudy old style", 30, "bold",'underline'), bg ="#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Lab for Cardiac Sciences ", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''At Max Institute of Cancer Care, 
        we offer a holistic and integrated treatment by consolidating views of experts in 
        Surgical Oncology, Radiation Oncology, and Medical Oncology. 
        Our best cancer doctors at Saket, Patparganj, Vaishali, Shalimar Bagh, Gurgaon, Max Smart, Lajpat Nagar, Mohali and Bathinda, specialize 
        in treating cancers affecting Breast, Head and Neck, Lung, Gastrointestinal tract and others.
        We believe in treating Cancer with a combination of 
        Chemotherapy, Radiation Therapy, Surgery and Targeted Therapy. 
        We are the first facility in northern India to acquire 
        Novalis Tx for IMRT/IGRT, Radiosurgery, HIPEC and SRS/SRT. 
        Additionally, we are equipped with an advanced 
        Da Vinci XI Robotic System for treating complex conditions like cancers of prostate, 
        cervix, colon/rectum, as well as heart tumors. 
        The procedure is the next frontier for minimally invasive surgery. '''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s1_class(root)
    root.mainloop()