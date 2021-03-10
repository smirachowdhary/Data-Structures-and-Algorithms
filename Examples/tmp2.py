import f1
from tkinter import *
import tkinter as tk


def isPrimeBtn_Handler(event):
    n=int(numTxt.get())
    tmp = resultLbl["text"]
    if f1.is_prime(n):
        resultLbl["text"] += f'{n} is prime \n'
    else:
        resultLbl["text"] += f'{n} is composite \n'


window = tk.Tk(className = "number GUI")
inputFrame=tk.Frame()

numLbl = tk.Label(text = "Number :", master = inputFrame)
numLbl.pack(side=LEFT)

numTxt = tk.Entry(fg="blue",bg="#66FFCC", master = inputFrame)
numTxt.pack(side=LEFT)

inputFrame.pack()

isPrimeBtn = tk.Button(text="Is Prime")
isPrimeBtn.bind("<Button-1>", isPrimeBtn_Handler)
isPrimeBtn.pack()


resultFrame = tk.Frame()

resultTitleLbl = tk.Label(text = "Result", master = resultFrame)
resultTitleLbl.pack()

resultLbl = tk.Label(master = resultFrame)
resultLbl.pack()

resultFrame.pack()

window.mainloop()
print("end")