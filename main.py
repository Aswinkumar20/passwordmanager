from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import array
import pyperclip


# ---------------------PASSWORD MANAGER-------------------------- #
def set_password():
    # maximum length of password needed
    MAX_LEN = 12
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    temp_pass = [choice(COMBINED_LIST) for _ in range(MAX_LEN - 4)]

    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = "".join(temp_pass_list)
    # print out password in entry
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------SAVE PASSWORD-------------- #
def action():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # check the empty entries

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="confirmation", message=f'These are the details you have entered\n'
                                                                     f'Email/Username: {email}\n'
                                                                     f'Password: {password}\nis it ok to Save?')
        if is_ok:
            with open("data_file.txt", mode='a')as file:
                file.write(f"website: {website} | User/Mail.id: {email} | Password: {password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# --------------------UI SETUP------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="images_1.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# to create Labels

website_label = Label(text="website :")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

# entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "aswinkumar@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons

password_entry_button = Button(text="Generate Password", command=set_password)
password_entry_button.grid(column=3, row=3)
add_button = Button(text="Add", command=action)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
