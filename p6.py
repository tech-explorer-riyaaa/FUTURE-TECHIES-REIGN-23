from tkinter import *
from tkinter import ttk,messagebox

class p6_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Bone Marrow Transplant (BMT)")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Bone Marrow Transplant", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Bone Marrow Transplant (BMT) in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Bone marrow in our bones is responsible for formation of blood cells. In fact, all the blood cells are formed by a subset of bone marrow cells 
        known as “hematopoietic stem cells” or simple “stem cells”. These stem cells have special characteristics, i.e. they can renew themselves, and 
        have the capability to develop into any type of blood cells.

        Nowadays, hematopoietic stem cells can also be obtained from peripheral blood after treatment with certain growth factors or from umbilical cord. 
        Thus, “Hematopoietic stem cell transplantation” is now also referred to as “Bone Marrow Transplantation”, wherein the stem cells from bone 
        marrow that produce red blood cells, white blood cells, and platelets are injected into a recipient after a short course of chemotherapy called 
        conditioning. Today, this is a viable option for several disorders and with continued research, success has improved markedly.

        A bone marrow transplant is a medical procedure performed to replace unhealthy bone marrow stem cells with the healthy ones. This transplant is 
        carried out to treat people with conditions like leukaemia - Blood Cancer, multiple myeloma, severe blood diseases such as aplastic anaemia, 
        thalassemia, sickle cell anaemia and certain immune deficiency diseases.'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p6_class(root)
    root.mainloop()