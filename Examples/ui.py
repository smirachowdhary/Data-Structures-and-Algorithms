import tkinter as tk
import c1

s1 = c1.student("Smira", 10)
s2 = c1.student("Viraj", 8)
# test= s1.GetIntroduction()
window = tk.Tk(className = "My Program")
frame1=tk.Frame()
frame2=tk.Frame()

greeting1 = tk.Label(text = s1.GetIntroduction(), master=frame1)
greeting1.pack()

greeting2 = tk.Label(text = s2.GetIntroduction(), master=frame2)
greeting2.pack()

input1 = tk.Entry(fg="blue",bg="#66FFCC")
button1 = tk.Button(text="Click me")
input1.pack()
button1.pack()

frame2.pack()
frame1.pack()

window.mainloop()

print("end")