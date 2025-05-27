import tkinter as tk
import webbrowser

def open_naver():
    webbrowser.open_new("https://www.naver.com")

root = tk.Tk()
root.title("네이버 바로가기")
root.geometry("500x300")

# Create a frame to hold the button and center it
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create the button
naver_button = tk.Button(frame, text="네이버", command=open_naver)
naver_button.pack()

root.mainloop()