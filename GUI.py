from main import *
from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Jarvis")
root.iconbitmap('C:\Tkinter\levi.ico')



#creating Frames and Displaying them
frame1 = LabelFrame(root,text="I am Jarvis",padx=20,pady=20)
frame1.grid(row=4,columnspan=4,padx=10,pady=0)


frame2 = LabelFrame(root,text="Display")
frame2.grid(row=3,columnspan=5)


frame3 = LabelFrame(root,text="Chatbox")
frame3.grid(row=8,columnspan=4)


#creating image widget
my_img = ImageTk.PhotoImage(Image.open("jarvislogo2.jpg"))

#storing the images in a variable i.e widget                                       
my_logo = Label(root,image=my_img)

#displaying image widget
#my_logo.grid(row=0, column=3)


#Creating widgets

mic_button = Button(frame1, text="Speak!",command=run_jarvis)
quit_button = Button(frame1, text="Quit", command=root.quit)




#Displaying widgets

mic_button.grid(row=1, column=1,padx=5)
quit_button.grid(row=1, column=3,padx=5)


#creating and displaying Display box

textbox = Text(frame2)
textbox.grid(row=1)


#to print all the output or print function in tkinter display box.
def redirector(inputStr):
    textbox.insert(INSERT, inputStr)


sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

#to give written commands.

chat_command = StringVar()
def submit():
    global chat
    global chat_command
    
    chat=chat_command.get()
    print(chat + "1")
    chat_command.set("")
    run_jarvis_chat(chat)
    
    chat_entry = Entry(frame3, textvariable=chat_command)
    chat_entry.grid(row=1, column=1,columnspan=2,rowspan=2,padx=5,pady=10)

    sub_btn = Button(frame3, text="submit", command = submit)
    sub_btn.grid(row=1,column=3,padx=5,pady=10)
    


chat_entry = Entry(frame3, textvariable=chat_command)
chat_entry.grid(row=1, column=1,columnspan=2,rowspan=2,padx=5,pady=10)

sub_btn = Button(frame3, text="submit", command = submit)
sub_btn.grid(row=1,column=3,padx=5,pady=10)




mainloop()