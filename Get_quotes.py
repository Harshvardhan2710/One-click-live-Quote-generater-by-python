from tkinter import * 
from requests import *

root = Tk()
root.title("Quote app by harsh sir")
root.geometry("700x600+50+50")
f = ("Arial", 30, "bold")

def gq():
	try:
		wa = "https://zenquotes.io/api/random"
		res = get(wa)
		data = res.json()
		quote = data[0]['q']
		lab_msg.configure(text=quote)
	except Exception as e:
		print("issue ", e)
btn_quote =  Button(root, text="GET QUOTE", font=f, command=gq)
lab_msg = Label(root, font=f, wraplength=400)

btn_quote.pack(pady=10)
lab_msg.pack(pady=10)

root.mainloop()