from tkinter import *
from tkinter import ttk,messagebox

class s3_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Orthopaedics & Joint Replacement")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p60.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Orthopaedics & Joint Replacement", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 10, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Global Health Hospitals Musculoskeletal Sciences & Orthopaedics", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''Global Health Institute of Musculoskeletal Sciences offers comprehensive care for several Orthopaedic
        afflictions including knee, hip, and joint problems. We are dubbed as the top orthopedic Hospital in India and
        are equipped with a wide array of specialties ranging from Sports Medicine, Paediatric orthopaedic services, 
        arthritis Diagnosis to Treatment and Pain Management. We focus on providing the highest level of patient care 
        with professional expertise for early mobilization and have taken orthopedic Treatment in Delhi to an altogether
        different level.We perform procedures like Computer Assisted Joint Replacement Surgery, Arthroscopic Surgery, 
        Traumatic Orthopaedic Surgery, Hand, Shoulder & Elbow Surgery, Spine Surgery, Articular Surface Replacement 
        Hip Surgery, Foot & Ankle Surgery, Total Knee & Hip Replacement Surgery among several others. 
        Global Health Institute of Musculoskeletal Sciences is equipped with a digital Orthopaedic operating suite. 
        The joint implants are planned pre-operatively for perfect size and positioning as per the anatomy of the patient,
        thereby safeguarding the patients. Our wide range of offerings have made us rank among the best hospitals in India.'''
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 15, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = s3_class(root)
    root.mainloop()