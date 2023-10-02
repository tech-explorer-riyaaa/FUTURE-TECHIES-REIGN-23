import tkinter as tk

class bmi_class:
    def __init__(self,root):
        self.root = root
        root.geometry("400x600")
        self.bmi_image = tk.PhotoImage(file='bmi.png')

        # Create label with image
        image_label = tk.Label(root, image=self.bmi_image)
        image_label.place(x=0,y=0,width=10,height=50)

        # Set the size and position of the label to cover the full screen
        image_label.place(x=0, y=0, relwidth=1, relheight=1)
    
        # Add other widgets and elements to the window
        title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 24), fg='black')
        title_label.pack(pady=20)

        height_label = tk.Label(root, text="Enter height (m):", font=("Arial", 14), fg='black')
        height_label.pack()

        self.height_entry = tk.Entry(root, font=("Arial", 14))
        self.height_entry.pack()

        weight_label = tk.Label(root, text="Enter weight (kg):", font=("Arial", 14), fg='black')
        weight_label.pack()

        self.weight_entry = tk.Entry(root, font=("Arial", 14))
        self.weight_entry.pack()

        calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14), bg='white',command=self.calculate_bmi)
        calculate_button.pack(pady=20)

        bmi_result_label = tk.Label(root, text="BMI:", font=("Arial", 14), fg='black')
        bmi_result_label.pack()

        self.bmi_result = tk.Label(root, text="", font=("Arial", 14), fg='black')
        self.bmi_result.pack()

        self.suggestion = tk.Label(root, text="", font=("Arial", 14), fg='black')
        self.suggestion.pack(side='bottom', pady=20)

    def calculate_bmi(self):
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())
        bmi = round(weight / (height * height), 2)
        self.bmi_result.config(text=bmi)
        if bmi < 18.5:
            self.suggestion.config(text="You are underweight.\n Eat more and exercise regularly to gain weight.", font=("Arial", 14))
        elif bmi >= 18.5 and bmi < 25:
            self.suggestion.config(text="You have a healthy weight.\n Maintain a balanced diet and\n exercise regularly to stay healthy.", font=("Arial", 14))
        elif bmi >= 25 and bmi < 30:
            self.suggestion.config(text="You are overweight.\n Cut down on junk food and \nincrease physical activity to lose weight.", font=("Arial", 14))
        elif bmi >= 30:
            self.suggestion.config(text="You are obese.\n Consult a doctor and make significant lifestyle changes\n to improve your health.", font=("Arial", 14))
        else:
            print("invalid output") 
            

if __name__ == "__main__":
    root = tk.Tk()
    obj = bmi_class(root)
    root.mainloop()