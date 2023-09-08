from tkinter import *
import tkinter
import random

window = tkinter.Tk()
window.title("Password Generator")
window.geometry('450x360')  # specify the size of the window

# condition variables
cond1 = IntVar()
cond2 = IntVar()
cond3 = IntVar()
cond4 = IntVar()
length = IntVar()

# charecter lists
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
list_3 = ['!', '@', '#', '$', '%', '^', '&', '*']
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# function to generate password
def password():
    final_list = []
    ln = length.get()
    if (cond3.get()):
        final_list.append(list_1)
    if (cond4.get()):
        final_list.append(list_2)
    if (cond2.get()):
        final_list.append(list_3)
    if (cond1.get()):
        final_list.append(list_4)
    bound = cond1.get() + cond2.get() + cond3.get() + cond4.get()
    if not (bound):
        return ("Nothing selected")
    password = []
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))

# gloabal password variable
pswrd = StringVar()
pswrd.set(password())
txt_1 = tkinter.Label(window, textvariable=pswrd, font=("ComicSansMS", 14))

# function to display generated password
def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = tkinter.Label(window, textvariable=pswrd, font=("ComicSansMS", 14))
    txt_1.pack()

#top labels
label_1 = tkinter.Label(window, text="\nPassword Generator", font=("ComicSansMS", 20))
label_2 = tkinter.Label(window, text="Select atleast two options\n", font=("ComicSansMS", 10))
label_1.pack()
label_2.pack()

# creating gui components
chkbutton_1 = tkinter.Checkbutton(window, text='Numbers', variable=cond1, onvalue=1, offvalue=0)
chkbutton_2 = tkinter.Checkbutton(window, text='Special Charecters', variable=cond2, onvalue=1, offvalue=0)
chkbutton_3 = tkinter.Checkbutton(window, text='Small Letters', variable=cond3, onvalue=1, offvalue=0)
chkbutton_4 = tkinter.Checkbutton(window, text='Capital Letters', variable=cond4, onvalue=1, offvalue=0)
slider_1 = tkinter.Scale(window, variable=length, orient=HORIZONTAL, label="Set length of password", length=130,
                         from_=8, to=30)
button_1 = tkinter.Button(window, text="Generate password", command=display_password)

# run created components
chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
slider_1.pack()
button_1.pack()

window.mainloop()
