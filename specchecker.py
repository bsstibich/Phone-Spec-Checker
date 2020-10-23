import tkinter as tk

def buttonf(phonevar): #function to use when button is pushed, changes display to show the specs of the selected phone
    global Xr,XsMax,i8,i8p,X,Xs,s10,s10e,s10p,s105g
    name = phonevar["name"]
    price = phonevar["full price"]
    monthly = phonevar["monthly price"]
    screen = phonevar["screen size"]
    camera = phonevar["camera"]
    colors = phonevar["colors"]
    label['text'] = 'Name: %s \n\nFull Price: %s \n\nMonthly Price: %s \n\nScreen Size: %s \n\nCamera: %s \n\nColors: %s' % (name,price,monthly,screen,camera,colors)


HEIGHT = 800
WIDTH = 800

#Dictionaries containg the phone specs
#If Done now, would have been made into a class rather than several dictionaries

Xr = {
    "name":"iPhone XR",
    "full price":"$749.99",
    "monthly price":"$15 for new lines or $31.25 normally",
    "colors":"Black, White, Red, Coral, Blue, Yellow",
    "screen size":"6.1 inches",
    "camera":"Single 12 mp Rear Camera"
}
XsMax = {
    "name":"iPhone Xs Max",
    "full price":"$1099.99",
    "monthly price":"$45.84",
    "colors":"Space Gray, Gold, Silver",
    "screen size":"6.4 inches",
    "camera":"Dual 12 mp Rear Camera"
}
i8p = {
    "name":"iPhone 8 Plus",
    "full price":"$699.99",
    "monthly price":"$12.17 for new lines or $29.17 normally",
    "colors":"Rose Gold",
    "screen size":"5.5 inches",
    "camera":"Dual 12 mp Rear Camera"
}
i8 = {
    "name":"iPhone 8",
    "full price":"$599.99",
    "monthly price":"$8 for new lines or $25 normally",
    "colors":"Black",
    "screen size":"4.7 inches",
    "camera":"Single 12 mp Rear Camera"
}
Xs = {
    "name":"iPhone Xs",
    "full price":"$999.99",
    "monthly price":"$41.67",
    "colors":"Space Gray, Gold, Silver",
    "screen size":"5.8 inches",
    "camera":"Dual 12 mp Rear Camera"
}
X = {
    "name":"iPhone X",
    "full price":"$899.99",
    "monthly price":"$37.50",
    "colors":"Space Gray, Gold, Silver",
    "screen size":"5.8 inches",
    "camera":"Dual 12 mp Rear Camera"
}
s10p = {
    "name":"Samsung Galaxy S10+",
    "full price":"$999.99",
    "monthly price":"$25 for new lines or $41.67 normally",
    "colors":"Black, Blue, Pearl",
    "screen size":"6.4 inches",
    "camera":"16 mp ultra wide lense, triple rear camera"
}
a50 = {
    "name":"Samsung Galaxy A50",
    "full price":"$349.99",
    "monthly price":"$10 for new lines or $14.59 normally",
    "colors":"Black",
    "screen size":"6.4 inches",
    "camera":"Triple Rear Camera"
}
s10 = {
    "name":"Samsung Galaxy S10",
    "full price":"$899.99",
    "monthly price":"$15 for new lines or $37.50 normally",
    "colors":"Black, Blue, Pearl",
    "screen size":"6.1 inches",
    "camera":"16 mp ultra wide lense, triple rear camera"
}
s10e = {
    "name":"Samsung Galaxy S10e",
    "full price":"$749.99",
    "monthly price":"$10 for new lines or $31.25 normally",
    "colors":"Black, Blue, Pearl",
    "screen size":"5.8 inches",
    "camera":"16 mp ultra wide lense, triple rear camera"
}
s105g = {
    "name":"Samsung Galaxy S10 5G",
    "full price":"$1299.99",
    "monthly price":"$40.28 for new lines or $54.17 normally",
    "colors":"Black, Blue, Pearl",
    "screen size":"6.1 inches",
    "camera":"16 mp ultra wide lense, triple rear camera"
}


#Base of GUI
root = tk.Tk()
root.title("Spec Checker")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#802618',)
frame.place(relx=0.5, rely=0, relheight=1, relwidth=1, anchor="n")

#Buttons
#If done now, would have made a function to place all these buttons, rather than copy and pasting the code
button = tk.Button(frame, text="iPhone Xs Max",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(XsMax))
button.place(relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="iPhone Xs",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(Xs))
button.place(relx=0,rely=0.05, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="iPhone X",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(X))
button.place(relx=0,rely=0.1, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="iPhone Xr",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(Xr))
button.place(x=0,rely=0.15, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="iPhone 8",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(i8))
button.place(relx=0,rely=0.25, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="iPhone 8 plus",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(i8p))
button.place(relx=0,rely=0.2, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="Samsung Galaxy S10 5G",font=('ariel',15), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(s105g))
button.place(relx=0.51,rely=0, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="Samsung Galaxy S10+",font=('ariel',18), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(s10p))
button.place(relx=0.51,rely=0.05, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="Samsung Galaxy S10",font=('ariel',18), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(s10))
button.place(relx=0.51,rely=0.1, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="Samsung Galaxy S10e",font=('ariel',18), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(s10e))
button.place(relx=0.51,rely=0.15, relheight=0.05, relwidth=0.49)

button = tk.Button(frame,text="Samsung A50",font=('ariel',20), bg="#5c5b52",fg=("#f2f0da"),command=lambda: buttonf(a50))
button.place(relx=0.51,rely=0.2, relheight=0.05, relwidth=0.49)

#Label

label = tk.Label(frame,font=('ariel',18),bg='#5c5b52',fg='#f2f0da', anchor='nw', justify='left',bd=20)
label.place(relx=0.005,rely=0.35, anchor='nw',relwidth=0.99,relheight=0.645)


root.mainloop()