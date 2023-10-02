from tkinter import *
from tkinter import ttk,messagebox

class p3_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Lung Transplant")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Lung Transplant", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Lung Transplant in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Damaged lungs can make it challenging for the body to receive the oxygen it requires to function. There exist many diseases as well as
        conditions which either damage the lungs entirely or hinder their ability to operate effectively. Some of these conditions are:
        -> Chronic obstructive pulmonary disease (COPD), including emphysema
        -> Cystic fibrosis
        -> Scarring of the lungs (pulmonary fibrosis)
        -> Pulmonary hypertension
        -> Alpha-1 antitrypsin deficiency
        -> Sarcoidosis
        -> Severe bronchiectasis
        -> Lymphangioleiomyomatosis (LAM Lung Disease)
        No organ or tissue can survive without oxygen. Oxygen is used throughout the body in chemical reactions to produce energy. The chemical
        eactions create carbon dioxide as a waste product. Carbon dioxide must then be removed from the body. This is called "gas exchange".
        The lungs perform both sides of this vital gas exchange for the entire body, both taking in oxygen and expelling carbon dioxide.'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p3_class(root)
    root.mainloop()