from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    """Pulls up random remaining card"""
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(card_bg, image=front_card)
    flip_time = window.after(3000, func=flip)


def flip():
    """shows 'reverse' side of card"""
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
    canvas.itemconfig(card_bg, image=back_card)


def known():
    """Removes data from cards"""
    to_learn.remove(current_card)
    print(len(to_learn))
    unknown_words = pandas.DataFrame(to_learn)
    unknown_words.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------- UI -------#


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_time = window.after(3000, func=flip)

# canvas
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 253, image=front_card)
card_title = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons:

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
