from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

#text label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)


#text box
data_input = Entry(width=10)
data_input.grid(column=1, row=0)


#miles text label
miles_text_lable = Label(text="Miles")
miles_text_lable.grid(column=2, row=0)

output_text = Label(text="data")
output_text.grid(column=1,row=1)

#km label
km_text = Label(text="Km")
km_text.grid(column=2, row=1)

#calculate button
button = Button(text="Calculate")
button.grid(column=1, row=3)


















window.mainloop()