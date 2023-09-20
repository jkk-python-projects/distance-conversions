
from tkinter import *

window = Tk()
window.title("Mi, Nm, Km - converter")
window.minsize(width=350, height=120)

global coefficient


#radiobutton
def radio_used():
    global coefficient
    if radio_state.get() == 1:
        coefficient = 1.6093
        label_upper["text"] = "Km"
        label_lower["text"] = "mi"
        button_clicked()
    if radio_state.get() == 2:
        coefficient = 0.6214
        label_upper["text"] = "mi"
        label_lower["text"] = "Km"
        button_clicked()
    if radio_state.get() == 3:
        coefficient = 0.5399568
        label_upper["text"] = "Km"
        label_lower["text"] = "Nm"
        button_clicked()
    if radio_state.get() == 4:
        coefficient = 1.852
        label_upper["text"] = "Nm"
        label_lower["text"] = "Km"
        button_clicked()


radio_state = IntVar()
radio1 = Radiobutton(text="Km to mi", value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text="mi to Km", value=2, variable=radio_state, command=radio_used)
radio3 = Radiobutton(text="Km to Nm", value=3, variable=radio_state, command=radio_used)
radio4 = Radiobutton(text="Nm to Km", value=4, variable=radio_state, command=radio_used)
radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=0, row=1)
radio4.grid(column=1, row=1)


def button_clicked():
    text_input = input1.get()
    conversion_calc_answer["text"] = round(float(text_input) * coefficient, 2)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input1 = Entry(width=10)
input1.grid(column=2, row=2)

label_upper = Label(text="Miles", font=("Arial", 12, "normal"))
label_upper.grid(column=3, row=2)

label_lower = Label(text="Km", font=("Arial", 12, "normal"))
label_lower.grid(column=3, row=3)

conversion_calc_label = Label(text="Is equal to: ", font=("Arial", 12, "normal"))
conversion_calc_label.grid(column=1, row=3)

conversion_calc_answer = Label(text="0", font=("Arial", 12, "normal"))
conversion_calc_answer.grid(column=2, row=3)

window.mainloop()
