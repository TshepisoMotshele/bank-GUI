import tkinter as tk
from tkinter import messagebox
import secrets
import string

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def signup(name_entry=None, surname_entry=None, gender_entry=None, phone_entry=None, password_entry_signup=None,
           user_info=None):
    # Get user information from the entry fields
    name = name_entry.get()
    surname = surname_entry.get()
    gender = gender_entry.get()
    phone = phone_entry.get()
    password = password_entry_signup.get()

    # Check if any field is empty
    if not name or not surname or not gender or not phone or not password:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        return

    # Save user information to the dictionary
    user_info['Name'] = name
    user_info['Surname'] = surname
    user_info['Gender'] = gender
    user_info['Phone'] = phone
    user_info['Password'] = password

    messagebox.showinfo(title="Sign Up Success", message="You have successfully signed up.")

def generate_password(event, password_entry_signup, confirm_password_entry_signup):
    password_length = 20  # Adjusted the length of the generated password
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))
    password_entry_signup.delete(0, tk.END)
    confirm_password_entry_signup.delete(0, tk.END)
    password_entry_signup.insert(0, generated_password)
    confirm_password_entry_signup.insert(0, generated_password)




def use_password(password_entry_signup):
    password = password_entry_signup.get()
    if password:
        messagebox.showinfo(title="Generated Password", message=f"Your password is:\n{password}")
    else:
        messagebox.showwarning(title="No Password", message="Please generate a password first.")


def open_signup_page():
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up form")
    signup_window.geometry('340x640')  # Increased height to accommodate the "Generate Password" button
    signup_window.configure(bg='#333333')

    # Add widgets for sign-up page
    name_label = tk.Label(signup_window, text="Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    name_entry = tk.Entry(signup_window, font=("Arial", 16))

    surname_label = tk.Label(signup_window, text="Surname", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    surname_entry = tk.Entry(signup_window, font=("Arial", 16))

    gender_label = tk.Label(signup_window, text="Gender", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    gender_entry = tk.Entry(signup_window, font=("Arial", 16))

    phone_label = tk.Label(signup_window, text="Phone Number", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    phone_entry = tk.Entry(signup_window, font=("Arial", 16))

    password_label_signup = tk.Label(signup_window, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    password_entry_signup = tk.Entry(signup_window, show="*", font=("Arial", 16))
    password_entry_signup.bind("<Button-1>", lambda event: generate_password(event, password_entry_signup, confirm_password_entry_signup))

    confirm_password_label_signup = tk.Label(signup_window, text="Confirm Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    confirm_password_entry_signup = tk.Entry(signup_window, show="*", font=("Arial", 16))

    generate_password_button = tk.Button(signup_window, text="Generate Password", bg="#669900", fg="#FFFFFF", font=("Arial", 16), command=lambda: generate_password(None, password_entry_signup, confirm_password_entry_signup))
    use_password_button = tk.Button(signup_window, text="Use Password", bg="#3366CC", fg="#FFFFFF", font=("Arial", 16), command=lambda: use_password(password_entry_signup))
    signup_button = tk.Button(signup_window, text="Sign Up", bg="#3399FF", fg="#FFFFFF", font=("Arial", 16), command=signup)


    # Place widgets on the sign-up window
    name_label.grid(row=0, column=0, pady=10)
    name_entry.grid(row=0, column=1, pady=10)

    surname_label.grid(row=1, column=0, pady=10)
    surname_entry.grid(row=1, column=1, pady=10)

    gender_label.grid(row=2, column=0, pady=10)
    gender_entry.grid(row=2, column=1, pady=10)

    phone_label.grid(row=3, column=0, pady=10)
    phone_entry.grid(row=3, column=1, pady=10)

    phone_label.grid(row=3, column=0, pady=10)
    phone_entry.grid(row=3, column=1, pady=10)

    password_label_signup.grid(row=4, column=0, pady=10)
    password_entry_signup.grid(row=4, column=1, pady=10)

    confirm_password_label_signup.grid(row=5, column=0, pady=10)
    confirm_password_entry_signup.grid(row=5, column=1, pady=10)

    signup_button.grid(row=6, column=0, columnspan=2, pady=10)

    signup_window.mainloop()

window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
signup_button = tk.Button(frame, text="Sign Up", bg="#3399FF", fg="#FFFFFF", font=("Arial", 16), command=open_signup_page)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
signup_button.grid(row=4, column=0, columnspan=2, pady=10)

frame.pack()

window.mainloop()
