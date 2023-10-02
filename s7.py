from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class s7_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Neurosciences")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Neurosciences", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals for Neurosciences", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''The Institute of Neurosciences provides round-the-clock, comprehensive Diagnostic and Therapeutic
        Neurology services, according to evidence based protocols set as per internationally accepted guidelines. 
        Our casualty services are available round-the-clock for diagnosis and early management of Neurological 
        emergencies like Status Epilepticus, Stroke and Neuromuscular Weakness, Encephalitis, Meningitis, other 
        Neuroinfectious diseases and behaviour changes.
        The Institute Houses Four Departments: 
        Department of Neurology & Stroke
        Department of Neurosurgery & Spine
        Rehabilitation Services and Behavioural Sciences
        Department of Neurocritical Care
        Department of Neurology & Stroke
        The Department of Neurology is supported by well-equipped ICU facilities and bedside Electro Encephalogram 
        (EEG) Monitoring for managing critically ill patients with Neurological illnesses. Our team of Neurologists
        is available round-the-clock for diagnosis, treatment and management of patients. We have state-of-the-art 
        diagnostic imaging modalities like 3T MRI and CT Scan.'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 15, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s7_class(root)
    root.mainloop()