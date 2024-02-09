import tkinter

def gen_ean():
    ean = input_field.get()
    info_label.config(text=ean)

def check_ean():
    ean = input_field.get()
    info_label.config(text=ean)

window = tkinter.Tk()
window.title("Hello World")
window.geometry("300x200+10+20")

#Buttons & Label

input_field = tkinter.Entry(window)

generate_button = tkinter.Button(window, text="EAN generieren", command=gen_ean)
check_button = tkinter.Button(window, text="Check EAN", command=check_ean)

anweisungs_label = tkinter.Label(window, text="Drücke einen Button")
info_label = tkinter.Label(window, text="Ich bin eine Info")

anweisungs_label.pack()
input_field.pack()
generate_button.pack()
check_button.pack()
info_label.pack()

window.mainloop()

