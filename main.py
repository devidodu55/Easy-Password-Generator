import random
import string
import tkinter as tk
import subprocess

def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(characters)for i in range(12))

    result_label.config(text=f"The generated password is: {password}")

    command = 'echo ' + password.strip() + '| clip'
    subprocess.run(command, shell=True)

def clear_password():

    result_label.config(text="")



root = tk.Tk()
root.title("Easy Password generator")


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
copy_button = tk.Button(root, text="Copy Password", command=lambda: subprocess.run('powershell.exe -command "Add-Type -AssemblyName PresentationCore,PresentationFramework;[Windows.Clipboard]::SetText(\'' + result_label.cget("text").split(": ")[1] + '\')"', shell=True))
clear_button = tk.Button(root, text="Clear", command=clear_password)
result_label = tk.Label(root, text="")


generate_button.pack(pady=10)
copy_button.pack(pady=10)
clear_button.pack(pady=10)
result_label.pack()


root.mainloop()

