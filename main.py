import tkinter as tk


def move_by_keys(event):
    info_coords = canvas.coords(oval)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + " " + str(y))
    if event.keysym == 'Up':
        canvas.move(oval, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(oval, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 20, 0)


win = tk.Tk()
label = tk.Label(win, text='INGINIRIUM')
label.pack()
canvas = tk.Canvas(win, bg='#fff', width=700, height=700)
oval = canvas.create_oval((300, 300), (400, 400), fill='#8171a3')
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()