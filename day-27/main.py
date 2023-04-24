import tkinter


def calculate():
    miles = float(entry.get())
    result_label.config(text=round(miles * 1.60934, 2))


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

entry = tkinter.Entry(width=5)
entry.focus()

miles_label = tkinter.Label(text="Miles")
is_equal_label = tkinter.Label(text="is equals to")
result_label = tkinter.Label(text="0")
km_label = tkinter.Label(text="Km")
button = tkinter.Button(text="Calculate", command=calculate)

entry.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
