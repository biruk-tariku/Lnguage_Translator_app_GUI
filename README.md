# Lnguage_Translator-app_GUI

its a basic text_translation application using tkinter and the `googletrans` library. When you run this code, it will create a graphical user interface (GUI) that allows you to enter text, select a destination language, and then translate the text into the selected language.

Here's a brief overview of what the code does:

1. It creates a tkinter window (`root`) with specific dimensions, a black background, and a title.

2. It adds labels, input fields, and a button to the GUI to allow the user to input text, select a destination language, and trigger the translation.

3. When the "Translate" button is clicked, it uses the `googletrans` library to perform the translation and displays the translated text in a text box.

4. The supported languages for translation are obtained from the `LANGUAGES` dictionary provided by `googletrans`.

5. The GUI is launched using `root.mainloop()`.

If you have installed the required dependencies (`tkinter` and `googletrans`) and you have an active internet connection, this code should work without any issues. Simply run it, and you'll have a basic language translation application.
