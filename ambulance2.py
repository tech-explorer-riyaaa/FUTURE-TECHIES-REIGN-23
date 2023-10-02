import tkinter as tk

root= tk.Tk()
root.title("Ambulance Help")
root.geometry("600x500")
root.option_add("*Font", "Verdana 10")

bg_image = tk.PhotoImage(file="p43.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relx=0.5, rely=0.5, anchor="center")

label= tk.Label(root, text= "Ambulance Help", width=35, height=3, relief="solid", borderwidth=1, bg='teal', font=("Verdana", 20,'bold','underline'), fg="white")
label.grid(row=0, column=0, columnspan=2)

delhi=tk.Label(root, text="DELHI : +91 1231231231",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.3, anchor="center")

delhi=tk.Label(root, text="MAHARASHTRA : +91 1231231232",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.4, anchor="center")

delhi=tk.Label(root, text="GUJARAT : +91 1231231233",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.5, anchor="center")

delhi=tk.Label(root, text="PUNJAB : +91 1231231234",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.6, anchor="center")

delhi=tk.Label(root, text="RAJASTHAN : +91 1231231235",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.7, anchor="center")

delhi=tk.Label(root, text="KERALA : +91 1231231236",font=('arial',15,'bold'))
delhi.place(relx=0.5, rely=0.8, anchor="center")


root.mainloop()