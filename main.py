import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width=400, height=400)
for i in range(0, 400, 50):
    canvas.create_line((0, i), (700, i), fill="black")
    canvas.create_line((i, 0), (i, 700), fill="black")
canvas.pack()
win.mainloop()