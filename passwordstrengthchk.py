import tkinter as tk
from tkinter import messagebox
import re

def password_strength_checker(password):
    # Initialize score
    score = 0
    
    # Length criteria
    if len(password) >= 8:
        score += 1
    
    # Uppercase letter criteria
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Lowercase letter criteria
    if re.search(r'[a-z]', password):
        score += 1
    
    # Digit criteria
    if re.search(r'\d', password):
        score += 1
    
    # Special character criteria
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    
    # Evaluate strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength

def check_password_strength():
    password = password_entry.get()
    strength = password_strength_checker(password)
    messagebox.showinfo("Password Strength", f"The strength of the password is: {strength}")

# Create main window
window = tk.Tk()
window.title("Password Strength Checker")

# Create label and entry for password input
password_label = tk.Label(window, text="Enter password:")
password_label.pack(pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

# Create button to check password strength
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

# Run the main loop
window.mainloop()
