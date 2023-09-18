from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1100x320")
root.resizable(0,0)
root['bg']= 'gray'

root.title( 'Language translator by BURA')
Label(root, text= "Language Translator", font= "Arial 20 bold").pack()



Label(root,text= "Enter Text", font="Arial 13 bold", bg = "White smoke").place(x=168, y=99)


input_text = Entry(root, width=60)
input_text.place(x=30, y=130)
input_text.get()

Label(root, text="output", font="arial 13 bold", bg="white smoke").place(x=780, y=90)
output_text = Text(root, font="arial 10", height=5, wrap=WORD, padx=5, pady=5, width=50)
output_text.place(x=600, y= 130)

language = list(LANGUAGES.values())

dest_lang = ttk.Combobox(root, values=language, width= 22)
dest_lang.place(x=130, y=160)
dest_lang.set("choose Language")


def Translate():
    translator = Translator()
    translated = translator.translate(text = input_text.get(), dest = dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

trans_btn = Button(root, text= 'Translate', font='arial 12 bold',pady= 5, command= Translate, bg="orange", activebackground="green")
trans_btn.place(x=445, y=180 )




root.mainloop()

 
