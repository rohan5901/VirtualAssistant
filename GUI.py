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

def redirector(inputStr):
    textbox.insert(INSERT, inputStr)


sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.







mainloop()