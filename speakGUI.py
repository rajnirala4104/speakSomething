#modual we need
from tkinter import *
from speak_func import speakTheSentence

# star the loop
root = Tk()
root.geometry("400x250")
root.resizable(0,0)
root.config(background="grey")

def showText():
    # print(userText.get())
    USER_TEXT = userText.get()
    if USER_TEXT == "":
        speakTheSentence("apko khuchh likhna parega tabhi to mai bolungi, nahito pata chala mene kuchh ulta sidha bol diya, tab to mere source code ko delete kar doge", "hi")
        root.destroy()
    speakTheSentence(USER_TEXT, 'hi')
    userText.set("")
    root.destroy()


userText = StringVar()
Label(root, text="Write something here...",bg="grey",fg='white' ,font="cascadia 20 bold").pack()
Entry(root, textvariable=userText, width=30, font="cascadia 15").pack(pady=10)
Button(root, text='Speak', font='cascadia 10 bold', command=showText, bg="grey", fg='white',padx=7, pady=5, border=4, relief='raised').pack(pady=10)

# end of the loop
root.mainloop()