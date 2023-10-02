from tkinter import *
from tkinter import ttk,messagebox

class s2_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Cardiac Sciences")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Cardiac Sciences", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals for Heart and Vascular Sciences ", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''Cardiovascular disease (CVD) is often interchangeably used with the term heart disease.
         Global Health Institute of Heart and Vascular Sciences, which is one of the best heart hospitals 
         in India provides treatment for conditions like heart defects, congenital heart disease, pulmonary
         heart failure, and coronary artery diseases.We are a tertiary care centre equipped with cutting edge
         technology to offer cardiac care program to our patients. We also offer an alternative treatment for
         end-stage heart failure patients with procedures like Pacemaker, ACD, CRT, Heart Hole surgeries (ASD, VSD, PDA),
        Paediatric Cardiac Surgery, Angioplasty/Angiography.Our Institute is a one-stop destination for 
        several kinds of cardiac treatments like Invasive and Interventional Cardiology, Electrophysiology,
        pacemaker and Arrhythmia services, management of abdominal and descending thoracic aneurysm and varicose veins.
        Our hospitals are equipped with state of the art Cath Labs, operation theatres, and several other heart care technologies.
        What is Cardiology?
        Derived from the Greek words, “Cardia” meaning heart and “logy” that means “study of”, cardiology is the branch of
        medicine that deals with the defects and diseases associated with the heart. Such diseases are managed by cardiologists. 
        Global Health Hospitals have team of best cardiologists in India. The surgery, however, is performed by heart surgeons 
        who specialize in surgical procedures to correct heart problems.
        At Global Health Institute of Heart and Vascular Sciences, we use the latest technologies and methodologies to be the 
        best cardiac hospital in India.'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s2_class(root)
    root.mainloop()