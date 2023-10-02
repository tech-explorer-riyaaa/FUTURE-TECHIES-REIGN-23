from tkinter import *
from tkinter import ttk,messagebox

class p4_class:
    def __init__(self,root):
        self.root = root
        self.root.title("LVAD Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "LVAD Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "LVAD Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        A left ventricular assist device (LVAD) is a lightweight pump that helps restore normal blood flow in patients whose hearts are weakened by 
        cardiac disease. It is used to sustain cardiac function in those with end-stage heart failure or as a bridge to heart transplants.

        Left Ventricular Assisted Device (LVAD) is designed to improve survival and quality of life of patients with end-stage heart failure. Today's 
        LVADs are lightweight and smaller than earlier models, so you'll most likely to be able to move around fairly easily. An LVAD restores normal 
        blood flow to a person whose heart has been weakened by heart disease.

        The device does not replace the heart rather it is a rescue for patients whose heart is so weak not able to sustain the blood pressure and 
        vital functions of body or as bridge to heart transplant. LVAD has increased the survival rates of patients and more importantly improves the 
        quality of life in certain subset of patients; however, there can be some risks like stroke, infection and bleeding.'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p4_class(root)
    root.mainloop()