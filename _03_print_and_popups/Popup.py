from tkinter import Tk, messagebox, simpledialog

window=Tk()
window.withdraw()

messagebox.showinfo("Title", "Message")
messagebox.showinfo("Food", "Tacos and Burritos")

userInput=simpledialog.askstring("Title", "Question")
favoriteFood=simpledialog.askstring("Food", "What is your favorite food?")
if favoriteFood=="tacos":
    messagebox.showinfo("Food", "HEY! ME TOO!")
else:
    messageBox.showinfo("Food","Nice!")