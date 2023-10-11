import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if name == "" or email == "" or phone == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # You can save the user's information to a file or a database here
        # For this example, we'll just display a success message
        message = f"Registration successful!\nName: {name}\nEmail: {email}\nPhone: {phone}"
        messagebox.showinfo("Success", message)

# Create the main window
root = tk.Tk()
root.title("Event Registration")

# Create and place labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Create and place the registration button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

# Start the GUI main loop
root.mainloop()