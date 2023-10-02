import tkinter as tk
from option2 import option2_class


class option4_class:
    def __init__(self,root):
        
        self.root = root
        root.title('Global Health Hospitals')
        root.geometry("1280x700+0+0")
        self.bg_image = tk.PhotoImage(file="bg1.png")
        self.label1 = tk.Label(root,image=self.bg_image).place(x = 0, y = 30, width = 1280, height = 700)
        root.configure(bg='teal')


        title = tk.Label(root, text = "Global Health Hospitals", padx = 20, compound = 'center', font = ("courier new", 30, "bold","underline"), bg = "white", fg = "black").place(x = 0, y = 0, relwidth = 1, height = 50)
        M_Frame = tk.LabelFrame(root, text = "Delhi", font = ("arial", 20,"bold", 'underline'), bg = "#ADD8E6",fg="green",border=10)
        M_Frame.place(x = 10, y = 70, width = 400, height = 300)
 
        N_Frame = tk.LabelFrame(root, text = "Maharashtra", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="green",border=10)
        N_Frame.place(x = 440, y = 70, width = 400, height = 300)

        T_Frame = tk.LabelFrame(root, text = "Gujarat", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="green",border=10)
        T_Frame.place(x = 870, y = 70, width = 400, height = 300)

        U_Frame = tk.LabelFrame(root, text = "Punjab", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="green",border=10)
        U_Frame.place(x = 870, y = 375, width = 400, height = 300)

        P_Frame = tk.LabelFrame(root, text = "Rajasthan", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="green",border=10)
        P_Frame.place(x = 440, y = 375, width = 400, height = 300)

        S_Frame = tk.LabelFrame(root, text = "Kerela", font = ("arial", 20,"bold",'underline'), bg = "#ADD8E6",fg="green",border=10)
        S_Frame.place(x = 10, y = 375, width = 400, height = 300)

        btn01 = tk.Button(M_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)
        btn02 = tk.Button(N_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)
        btn03 = tk.Button(T_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)
        btn04 = tk.Button(U_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)
        btn05 = tk.Button(P_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)
        btn06 = tk.Button(S_Frame, text = "Request call back", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command = self.option2).place(x =0, y = 200, width =300, height = 40)

        label01=tk.Label(M_Frame, text="PunjabiBagh 110026", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        #label02=tk.Label(M_Frame, text="Cardiac Sciences", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=50)
        label03=tk.Label(M_Frame, text="Saket 110045", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label04=tk.Label(M_Frame, text="Purana Bazaar 110056", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label05=tk.Label(M_Frame, text="Ashok Nagar 110066", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        label06=tk.Label(M_Frame, text="Ashok park Extension 110067", font=("arial",15, 'bold'),fg='black').place(x=20, y=160)

        label07=tk.Label(N_Frame, text="Pune 111045", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        label08=tk.Label(N_Frame, text="Bandra 410014", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label09=tk.Label(N_Frame, text="Borivali 411001", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label10=tk.Label(N_Frame, text="Bakarwada 411014", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        #label11=tk.Label(N_Frame, text="Rs 1300", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        label12=tk.Label(T_Frame, text="Ahmedabad 380001", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        label13=tk.Label(T_Frame, text="Dhandhuka 382460", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        label14=tk.Label(T_Frame, text="Dholka 282225", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        label15=tk.Label(T_Frame, text="Sanand 382110", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        #label16=tk.Label(T_Frame, text="Rs 1100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        # label17=tk.Label(T_Frame, text="PAEDIATRICS", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        # label18=tk.Label(T_Frame, text="Senior Consultant", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        # label19=tk.Label(T_Frame, text="Global Health Mumbai", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        # label20=tk.Label(T_Frame, text="17 years of expertise", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        # label21=tk.Label(T_Frame, text="Rs 2100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        labe17=tk.Label(U_Frame, text="Amloh Road 141401", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        labe18=tk.Label(U_Frame, text="Amritsar G.P.O 143001", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        labe19=tk.Label(U_Frame, text="Amrit Bazaar 144601", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        labe20=tk.Label(U_Frame, text="Ahmedgarh 148021", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        labe21=tk.Label(U_Frame, text="Chandigrah 147043", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        lab17=tk.Label(P_Frame, text="Ajmer 406", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        lab18=tk.Label(P_Frame, text="Alwar 486", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        lab19=tk.Label(P_Frame, text="Banswara 281", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        lab20=tk.Label(P_Frame, text="Bikaner 261", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        #lab21=tk.Label(P_Frame, text="Rs 3100", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

        la17=tk.Label(S_Frame, text="Ernakulum 393", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=20)
        la18=tk.Label(S_Frame, text="Idukki 298", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=55)
        la19=tk.Label(S_Frame, text="Kannur 382", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=90)
        la20=tk.Label(S_Frame, text="Kozhikode 410", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=125)
        la21=tk.Label(S_Frame, text="Kollam 364", compound='left',font=("arial",15,'bold'),fg='black').place(x=20, y=160)

    def option2(self) :
        new_win = tk.Toplevel(self.root)  
        new_obj = option2_class(new_win)
   
         

if __name__ == "__main__":
    root = tk.Tk()
    obj = option4_class(root)
    root.mainloop()