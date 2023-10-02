from tkinter import *
from tkinter import ttk,messagebox

class p2_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Da Vinci Robotic Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Da Vinci RObotic Surgery", font = ("goudy old style", 30, "bold", 'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Da Vinci Robotic Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Da Vinci robotic surgical system is used to perform the most advanced, minimally invasive surgical procedures with extreme precision. It 
        offers the surgeon high-resolution 3D vision and superior control.
        
        Da Vinci Robotic Surgery is a leading edge technology that is used in several specialities to carry out the surgical procedures with proven
        superior patient outcomes. With the Da Vinci System, the surgeons operate through a few incisions by utilizing a high resolution 3D vision 
        system. It features small wristed instruments that bend and rotates greater than the human hand providing a superior precision and control 
        to the surgeon. Today, surgeons are using Da Vinci Surgical System on patients who are diagnosed with several complexconditions like cancers,
        urological procedures, cancers of cervix, prostate, lung, uterus, colon/rectum as well as heart disease and fibroid tumors.

        Da Vinci Robotic Surgery uses a high resolution 3D vision system, it allows the surgeons to view anatomical structures in natural colours.
        It provides a natural hand-eye positioning coordination plus the built in microphone facilitates efficient communication in operation theatre.'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p2_class(root)
    root.mainloop()