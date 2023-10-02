from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class s5_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Robotic Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Robotic Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals for Robotic Surgery", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''At Global Health Healthcare, we are committed to deliver the highest standards of clinical excellence
         and that’s why we continuously invest in innovative technologies of the future to ensure our patients 
         get the best care. Global Health Institute of Robotic Surgery is one of the largest robotic surgical programmes 
        in India, which combines the advancements of robotic systems and the experience of specialists to make
        patient recovery easier and faster. Global Health Institute of Robotic Surgery aims to deliver superior
        patient outcomes over conventional surgical approaches. Max Healthcare is equipped with 15 advanced 
        surgical robotic systems including Da Vinci X, Da Vinci Xi, Next Gen Versius, ExcelsiusGPS and CORI 
        surgical system. We have over 150 trained robotic surgeons in Max network hospitals, who have successfully
        performed numerous robotic surgeries.Advantages of Robotic Surgeries over Conventional Surgeries:
        Minimally invasive,Greater precision,Reduced blood loss,3D surgery powered by Artificial Intelligence,
        Faster recovery,Short hospital stay'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s5_class(root)
    root.mainloop()