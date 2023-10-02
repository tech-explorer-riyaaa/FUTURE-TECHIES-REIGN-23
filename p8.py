from tkinter import *
from tkinter import ttk,messagebox

class p8_class:
    def __init__(self,root):
        self.root = root
        self.root.title("Bariatric Surgery")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.bg_image = PhotoImage(file='p73.png')
        self.image_label = Label(self.root, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #root.configure(bg='teal')
##TITLE
        title = Label(self.root, text = "Bariatric Surgery", font = ("goudy old style", 30, "bold",'underline'), bg = "#000064", fg = "white").place(x = 0, y = 15, width = 1270, height = 70)
        M_Frame = LabelFrame(self.root, text = "Bariatric Surgery in Global Health Hospitals", font = ("goudy old style", 25,"bold",'underline'), bg ="#000064",fg="white")
        M_Frame.place(x = 0, y = 100, width = 1270, height = 110)
##Variables
        info = '''   
        Bariatric Obesity Weight loss surgery is an effective treatment option for patients suffering with morbid obesity. It also causes significant 
        improvement in the obesity-related co-morbid conditions like Type 2 diabetes, high blood pressure, and joint pains, sleeping disorders 
        like sleep apnea, heart diseases, infertility issues and several others
        
        There are several types of bariatric surgery, including:
        -> Gastric Bypass Surgery
        -> Sleeve Gastrectomy
        -> Adjustable Gastric Banding
        -> Biliopancreatic diversion with duodenal switch
        
        Bariatric surgery is typically only recommended for people with a body mass index (BMI) of 40 or higher, or a BMI of 35 or higher with at 
        least one obesity-related medical condition. It is a major surgery and requires significant lifestyle changes to be successful.'''
        
        I_Frame = LabelFrame(self.root, text = "Overview", font = ("goudy old style", 15))
        I_Frame.place(x = 20, y = 250, width = 1100, height = 250)
        lbl_txt = Label(self.root, text = info, font = ("goudy old style", 16, "bold"), bg = "white",justify=LEFT).place(x = 0, y = 250, width = 1270, height = 350)


if __name__ == "__main__":
    root = Tk()
    obj = p8_class(root)
    root.mainloop()