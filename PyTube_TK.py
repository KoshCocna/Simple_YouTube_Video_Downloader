from tkinter import *
from pytube import YouTube
from time import sleep

root = Tk()
root.geometry("500x600")
root.configure(bg='#0070E8')
root.title("YouTube Video Downloader")
root.resizable(False, False)

image_icon = PhotoImage(file="youtube.ico")
root.iconphoto(False, image_icon)

Label(root, text="Now YouTube is yours!", bg='#0070E8', fg='#F1F1F1', font="arial 24 bold").place(relx=0.5, rely=0.2,
                                                                                                  anchor=CENTER)

link = StringVar()

link_enter = Entry(root, width=36, font="arial 16", textvariable=link, bd=3)
link_enter.place(relx=0.5, rely=0.4, anchor=CENTER)
link_enter.insert(0, "Paste the link of the video!")
link_enter.configure(state=DISABLED)


def on_click(event):
    link_enter.configure(state=NORMAL)
    link_enter.delete(0, END)
    link_enter.unbind('<Button-1>', on_click_id)


on_click_id = link_enter.bind('<Button-1>', on_click)


def downloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        Label(root, text="Enter the correct link!", font="arial 15", fg="#0070E8", bg="#0070E8").place(relx=0.5,
                                                                                                       rely=0.55,
                                                                                                       anchor=CENTER)
        video.download()
        Label(root, text="Done!", font="arial 15", fg="#F1F1F1", bg="#0070E8").place(relx=0.5, rely=0.55, anchor=CENTER)

    except:
        Label(root, text="Done!", font="arial 15", fg="#0070E8", bg="#0070E8").place(relx=0.5, rely=0.55, anchor=CENTER)
        Label(root, text="Enter the correct link!", font="arial 15", fg="#F1F1F1", bg="#0070E8").place(relx=0.5,
                                                                                                       rely=0.55,
                                                                                                       anchor=CENTER)


Button(root, text="Download", font="arial 15 bold", bg="#0B96F7", fg='#F1F1F1', padx=2,
       command=downloader).place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
