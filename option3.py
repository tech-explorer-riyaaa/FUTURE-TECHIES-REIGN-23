import tkinter as tk
from option1 import option1_class

class option3_class:
    def __init__(self,root):
        # self.root = tk.Tk()
        self.root = root
        root.title('Global Health Hospitals')
        root.geometry("1280x700+0+0")
        self.bg_image = tk.PhotoImage(file="bg1.png")
        self.label1 = tk.Label(root,image=self.bg_image).place(x = 0, y = 30, width = 1280, height = 700)

        root.configure(bg='teal')

        title = tk.Label(root, text = "Top experts for your health", padx = 20, compound = 'center', font = ("courier new", 30, "bold","underline"), bg = "white", fg = "black").place(x = 0, y = 0, relwidth = 1, height = 50)
        M_Frame = tk.LabelFrame(root, text = "Dr Ravi Mishra", font = ("arial", 20,"bold", 'underline'), bg = "#ADD8E6",fg="white",border=10)
        M_Frame.place(x = 10, y = 70, width = 400, height = 300)

        N_Frame = tk.LabelFrame(root, text = "Dr Swati Ghosh", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="white",border=10)
        N_Frame.place(x = 440, y = 70, width = 400, height = 300)

        T_Frame = tk.LabelFrame(root, text = "Dr Shashank", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="white",border=10)
        T_Frame.place(x = 870, y = 70, width = 400, height = 300)

        U_Frame = tk.LabelFrame(root, text = "Dr Ravina Singh", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="white",border=10)
        U_Frame.place(x = 870, y = 375, width = 400, height = 300)

        P_Frame = tk.LabelFrame(root, text = "Dr Amit Saxena", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="white",border=10)
        P_Frame.place(x = 440, y = 375, width = 400, height = 300)

        S_Frame = tk.LabelFrame(root, text = "Dr Asokan Pichai", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="white",border=10)
        S_Frame.place(x = 10, y = 375, width = 400, height = 300)

        btn01 = tk.Button(M_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)
        btn02 = tk.Button(N_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)
        btn03 = tk.Button(T_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)
        btn04 = tk.Button(U_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)
        btn05 = tk.Button(P_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)
        btn06 = tk.Button(S_Frame, text = "Book an appointment", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.option1).place(x =0, y = 200, width =300, height = 40)

        label01=tk.Label(M_Frame, text="Cardiologist", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        #label02=tk.Label(M_Frame, text="Cardiac Sciences", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=50)
        label03=tk.Label(M_Frame, text="Director Cardiology", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label04=tk.Label(M_Frame, text="Global Health Delhi", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label05=tk.Label(M_Frame, text="22 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        label06=tk.Label(M_Frame, text="Rs 1200", font=("arial",15),fg='black').place(x=20, y=160)

        label07=tk.Label(N_Frame, text="ENT", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        label08=tk.Label(N_Frame, text="Senior Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label09=tk.Label(N_Frame, text="Global Health Delhi", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label10=tk.Label(N_Frame, text="10 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        label11=tk.Label(N_Frame, text="Rs 1300", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        label12=tk.Label(T_Frame, text="Cardio Thoracic Surgery", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        label13=tk.Label(T_Frame, text="Senior Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label14=tk.Label(T_Frame, text="Global Health Mumbai", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label15=tk.Label(T_Frame, text="7 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        label16=tk.Label(T_Frame, text="Rs 1100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        # label17=tk.Label(T_Frame, text="PAEDIATRICS", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        # label18=tk.Label(T_Frame, text="Senior Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        # label19=tk.Label(T_Frame, text="Global Health Mumbai", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        # label20=tk.Label(T_Frame, text="17 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        # label21=tk.Label(T_Frame, text="Rs 2100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        labe17=tk.Label(U_Frame, text="Plastic Surgery", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        labe18=tk.Label(U_Frame, text="Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        labe19=tk.Label(U_Frame, text="Global Health hyderabad", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        labe20=tk.Label(U_Frame, text="13 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        labe21=tk.Label(U_Frame, text="Rs 4100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        lab17=tk.Label(P_Frame, text="General Physician", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        lab18=tk.Label(P_Frame, text="Empanelled Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        lab19=tk.Label(P_Frame, text="Global Health hyderabad", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        lab20=tk.Label(P_Frame, text="23 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        lab21=tk.Label(P_Frame, text="Rs 3100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        la17=tk.Label(S_Frame, text="Urologist", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        la18=tk.Label(S_Frame, text="Paediatric Urology", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        la19=tk.Label(S_Frame, text="Global Health Surat", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        la20=tk.Label(S_Frame, text="11 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        la21=tk.Label(S_Frame, text="Rs 1000", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)
    
    def option1(self) :
        new_win = tk.Toplevel(self.root)  
        new_obj = option1_class(new_win)
   

if __name__ == "__main__":
    root = tk.Tk()
    obj = option3_class(root)
    root.mainloop()