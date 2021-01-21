# Random Password Generator (GUI), Using Python
# Shashwat Rauthan
# Btech. (CSE) 2019-23
# University Roll No.: 2014458

# SPECIFICATIONS:
# password is having minimum length of 12 characters & maximum of 32 characters
# password starts with lowercase alphabet & ends with uppercase alphabet
# password is having atleast 2 uppercase alphabets ,2 lowercase alphabets,1 number,1 special character & no space
# no inbuilt fuction is used for randomisation, pseudo random number generator is used
# GUI 


import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *

# Main Window 

root = Tk()
root.geometry("300x300")
root.resizable(0,0)
root.title("Random Password Generator")


# Select Password Length                        //for manual length selection
pass_len_label = Label(root, text = 'PASSWORD LENGTH').pack(pady = 4)
pass_len = IntVar()
length = Combobox(root, textvariable = pass_len , width = 15, state = 'readonly')
length['values'] = (12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
length.current(0)
length.pack()

# Randomise Length Button                       ////for random length selection
def Random_Length():
    i = random.choice(range(12,33))          #pseudo random number generator
    # i = random.randint(12,33)             
    pass_len.set(i)

random_button = Button(root, text = 'Randomise Lenght',command = Random_Length,width = 18)
random_button.pack(pady = 5)


# Password Generator Function

pass_str = StringVar()

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = '!@#$%^&*()'

def Pass_Generator():
    password = ''
    password = random.choice(lowercase)                       #first character should be lowercase
    password = password + random.choice(uppercase)+random.choice(lowercase)+random.choice(digits)+random.choice(punctuation)
                                            #for, atleast 1 uppercase  1 lowercase   1 digit 1 special character
    for x in range(pass_len.get() - 6):
        password = password + random.choice(uppercase + lowercase + digits + punctuation)    #random remaining characters
    password = password + random.choice(uppercase)              ##last character should be uppercase
    pass_str.set(password)
    Copy_button.config(text = 'COPY TO CLIPBOARD')

# Generate Button
Generate_button = Button(root, text = "GENERATE PASSWORD" , command = Pass_Generator).pack(pady = 6)

# Password Entry Box
Entry(root , textvariable = pass_str,width = 38).pack()


# Copy Function
def Copy_Password():
    pyperclip.copy(pass_str.get())
    Copy_button.config(text = 'COPIED!')

Copy_button = Button(root, text = 'COPY TO CLIPBOARD', command = Copy_Password,width = 20)
Copy_button.pack(pady=5)

End_label = Label(root, text = '~Shashwat Rauthan').pack(side = 'bottom')

# loop to run program
root.mainloop()