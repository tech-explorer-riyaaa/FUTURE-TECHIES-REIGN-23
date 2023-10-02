from tkinter import *
from tkinter import ttk,messagebox

class p7_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Thoracic Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        root.configure(bg='white')
##TITLE
        title = Label(self.root, text = "Thoracic Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Thoracic Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Thoracic surgery is a type of surgery that deals with conditions of the chest, including the lungs, esophagus, diaphragm, and 
        mediastinum (the area between the lungs). This type of surgery is often used to treat lung cancer, chest trauma, esophageal 
        cancer, mediastinal tumors, hyperhidrosis (excessive sweating), and other conditions.

        Thoracic surgery can be performed using open surgery or minimally invasive techniques such as video-assisted thoracic surgery 
        (VATS) or robotic-assisted thoracic surgery (RATS). In VATS and RATS, the surgeon uses small incisions and a camera to perform 
        the surgery, rather than making a large incision.

        The specific procedure performed during thoracic surgery depends on the condition being treated. For example, a lobectomy may 
        be performed to remove a portion of the lung affected by cancer, while an esophagectomy may be performed to remove a portion 
        of the esophagus affected by cancer. Other procedures may involve repairing a damaged diaphragm or removing a tumor from the 
        mediastinum'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg='white',justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p7_class(root)
    root.mainloop()