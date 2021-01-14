from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    random_letters = random.choices(letters, k=nr_letters)
    random_symbols = random.choices(symbols, k=nr_symbols)
    random_numbers = random.choices(numbers, k=nr_numbers)
    random_password = random_letters + random_symbols + random_numbers

    random.shuffle(random_password)

    random_password_as_string = ''.join(random_password)
    password_in.insert(0, random_password_as_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_in.get()
    email = user_in.get()
    password = password_in.get()

    new_data = {
        website : {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty.")

    else:
        try:
            with open('data.json', mode='r') as data_file:
                # reads json file
                data = json.load(data_file)
                # updates dictionary
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent = 4)
    website_in.delete(0, END)
    password_in.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    search_term = website_in.get()
    try:
        with open('data.json', mode='r') as json_file:
            json_dict = json.load(json_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    else:
        try:
            json_dict[search_term]
        except KeyError:
            messagebox.showinfo("Error", f"No Details For {search_term} Found")
        else:
            email = json_dict[search_term]['email']
            password = json_dict[search_term]['password']
            messagebox.showinfo(f"{search_term}", f"Email: {email}\n"
                                                  f"Password: {password}")







# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)

my_image = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=my_image)


canvas.grid(row=0, column=1)

website_label = Label(text='Website:', font=('Courier', 10, 'normal'))
website_label.grid(row=1, column=0)

website_in = Entry(width=33)
website_in.grid(row=1, column=1)
website_in.focus()

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2)


user_label = Label(text='Email/Username:', font=('Courier', 10, 'normal'))
user_label.grid(row=2, column=0)

user_in = Entry(width=52)
user_in.grid(row=2, column=1, columnspan=2)
user_in.insert(0, 'KarinAlbiez@gmail.com')

password_label = Label(text='Password:', font=('Courier', 10, 'normal'))
password_label.grid(row=3, column=0)

password_in = Entry(width=33)
password_in.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()