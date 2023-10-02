from tkinter import *
from tkinter import ttk,messagebox

class s6_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Liver Transplant and Biliary Sciences")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Liver Transplant and Biliary Sciences", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals for Neurosciences", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''In liver transplant surgery, the patient’s old liver is removed completely 
        and a new one from a liver donor is put in the same place after joining the blood 
        vessels and the bile duct. The donor liver can be from a dead person where usually 
        the whole liver is transplanted or more commonly it is from a family member who donates
        part of his or her liver. Although we only have one liver in our body, liver can now 
        be safely divided in to 2 parts so that one part can be taken out for transplantation 
        and the remaining liver is sufficient for the donor. Both these portions can regenerate 
        quickly to its original size though the shape will become different. Liver transplant 
        is reserved for those whose liver disease has progressed so much that their general 
        condition is critical. Generally, these are patients who have exhausted other forms of 
        treatment or side by side have developed liver cancer. In cadaveric transplant, the wait
        can be unpredictable and some patients will die while waiting for a donor liver. 
        On the other hand, living donor liver transplant can be done when the patient really needs 
        it and when the entire team is available as it is a planned operation.'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s6_class(root)
    root.mainloop()