import tkinter
import pyshorteners
import clipboard


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))


root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("900x400")
root.configure(bg="#333333")

frame = tkinter.Frame(bg="#333333")

longurl_label = tkinter.Label(
    frame, text="Enter Long URL", bg="#333333", fg="#ff3399", font=("arial", 30))
longurl_entry = tkinter.Entry(frame, font=("arial", 15), bd=0)
shorturl_label = tkinter.Label(
    frame, text="SHORTENED URL", bg="#333333", fg="#ff3399", font=("arial", 15))
shorturl_entry = tkinter.Entry(frame, font=("arial", 15), bd=0)
shorten_button = tkinter.Button(
    frame, text="SHORTEN URL", command=shorten, bg="#ff3399", fg="#ffffff", font=("arial", 15))


# def copy(root):
#     clipboard.copy(root)
#     copy()


copy_button = tkinter.Button(
    frame, text="COPY", command=lambda: clipboard.copy(shorturl_entry.get()), bg="#ff3399", fg="#ffffff", font=("arial", 15))

longurl_label.grid(row=1, column=3, columnspan=2,
                   sticky="news", pady=30, padx=300)
longurl_entry.grid(row=2, column=3, pady=10, padx=300)
shorturl_label.grid(row=3, column=3, pady=10, padx=300)
shorturl_entry.grid(row=4, column=3, pady=10, padx=300)
shorten_button.grid(row=5, column=3, padx=300, pady=10)
copy_button.grid(row=9, column=3, padx=300, pady=10)
frame.pack()
root.mainloop()
