import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    gender = gender_var.get()
    phone = entry_phone.get()

    if name and email and age and gender and phone:
        messagebox.showinfo("Registration", "Registration Successful!")
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Set window size
root.geometry("300x250")

# Create and place the widgets
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky='w')

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky='w')

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5, sticky='w')

entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=3, column=0, padx=10, pady=5, sticky='w')

gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.grid(row=3, column=1, padx=10, pady=5, sticky='w')

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.grid(row=3, column=1, padx=10, pady=5, sticky='e')

label_phone = tk.Label(root, text="Phone Number:")
label_phone.grid(row=4, column=0, padx=10, pady=5, sticky='w')

entry_phone = tk.Entry(root)
entry_phone.grid(row=4, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, columnspan=2, pady=10)


root.mainloop()
