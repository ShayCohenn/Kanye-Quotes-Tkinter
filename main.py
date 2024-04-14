import requests
from typing import Final 
from tkinter import Tk, Canvas, PhotoImage, Button

URL: Final[str] = "https://api.kanye.rest/"

def get_quote() -> str:
    quote: str
    try:
        quote = requests.get(URL).json()['quote']
    except Exception as e:
        print(e)
        quote = "Kanye Quote Goes HERE"
    finally:
        return quote

def change_quote_text() -> None:
    canvas.itemconfig(quote_text, text="Waiting for Kanye...")
    canvas.update()
    quote: str = get_quote()
    canvas.itemconfig(quote_text, text=quote)

# --------------------------------------------- UI Setup --------------------------------

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas: Canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 26, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img: PhotoImage = PhotoImage(file="kanye.png")
kanye_button: Button = Button(image=kanye_img, highlightthickness=0, border=0, command=change_quote_text)
kanye_button.grid(row=1, column=0)

window.mainloop()