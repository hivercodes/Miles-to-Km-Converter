from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)


def calculate_miles():
    return_data = float(data_input.get()) * 1.60934
    output_text.config(text=round(return_data, 2))


#centering attempt

#text label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)


#text box
data_input = Entry(width=10)
print(data_input)
data_input.grid(column=1, row=0)


#miles text label
miles_text_lable = Label(text="Miles")
miles_text_lable.grid(column=2, row=0)


#output text
output_text = Label(text="0")
output_text.grid(column=1,row=1)

#km label
km_text = Label(text="Km")
km_text.grid(column=2, row=1)

#calculate button
button = Button(text="Calculate", command=calculate_miles)
button.grid(column=1, row=3)


















window.mainloop()