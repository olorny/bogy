from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action():
    anweisungs_label.config(text="Ich wurde geaendert!")

# Ein Fenster erstellen
fenster = Tk()

# Den Fenstertitle erstellen
fenster.title("PyGUISmall - ein Fenster.")

# Label und Buttons erstellen.
change_button = Button(fenster, text="Aendern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
Klicke auf 'Aendern'.")

info_label = Label(fenster, text="Ich bin eine Info:\n\
Der Beenden Button schliesst das Programm.")

# Nun fügen wir die Komponenten unserem Fenster 
# in der gwünschten Reihenfolge hinzu.
anweisungs_label.pack()
change_button.pack()
info_label.pack()
exit_button.pack()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()
button_action()

