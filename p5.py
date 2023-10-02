from tkinter import *
from tkinter import ttk,messagebox

class p5_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Knee Replacement Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Knee Replacement Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Knee Replacement Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg = "#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Knee replacement surgery also known as knee arthroplasty is a procedure that decreases the pain in knee joint and improves the quality of life. 
        During knee replacement surgery, the worn-out surfaces of the knee joint are removed/shaved off and replaced with implants. The femoral (thigh 
        bone) and tibial (leg bone) component is made up of a metal alloy that covers the end of these bones. The insert/spacer that is put between the 
        two metal components serves as a cushion, a smooth gliding surface between the two. The patella (knee cap) is resurfaced with a special 
        polyethylene
        
        Knee replacement surgery can be performed using several different techniques, including traditional open surgery, minimally invasive surgery, 
        and computer-assisted surgery. The choice of technique will depend on the patient's individual needs and the surgeon's expertise.
        
        After the surgery, patients typically stay in the hospital for several days and then undergo physical therapy to help them regain strength 
        and range of motion in the knee joint. Most patients are able to resume normal activities within a few months of surgery. Like any surgery, 
        knee replacement surgery does carry some risks, including infection, blood clots, and nerve damage. However, for most patients, the benefits 
        of the procedure far outweigh the risks. With proper care and rehabilitation, a knee replacement can last for many years and improve life 
        quality.'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p5_class(root)
    root.mainloop()