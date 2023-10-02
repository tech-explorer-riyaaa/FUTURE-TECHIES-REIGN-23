from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class s8_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Thoracic Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Thoracic Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals for Thoracic Surgery", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''Thoracic surgery provides services for the surgical treatment of non-cardiac,
        benign and malignant diseases of the chest. The Thoracic Surgery specialists at Max Hospital,
        offer consultation and surgical management of a wide range of disorders and diseases involving:
        Lungs
        Pleura (Chest cavity)
        Trachea and bronchus (wind pipe)
        Esophagus (food pipe)
        Chest wall
        Diaphragm
        Mediastinum
        Chest Trauma
        Hyperhidrosis (excessive sweating): of axilla or hand'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s8_class(root)
    root.mainloop()