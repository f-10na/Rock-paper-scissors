from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Button
import time

window = tk.Tk()

start_time = time.time()
end_time = time.time()
elapsed_time = end_time - start_time
# Dictionary to store PhotoImage objects
image_dict = {}

rock_path = "rock.jpeg"
rock_image = Image.open(rock_path)
rock_image = rock_image.resize((150,150))
rock_photo = ImageTk.PhotoImage(rock_image)
image_dict['rock'] = rock_photo  # Store the PhotoImage object in the dictionary

paper_path = "paper.jpeg"
paper_image = Image.open(paper_path)
paper_image = paper_image.resize((150,150))
paper_photo = ImageTk.PhotoImage(paper_image)
image_dict['paper'] = paper_photo  # Store the PhotoImage object in the dictionary

scissors_path = "scissors.png"
scissors_image = Image.open(scissors_path)
scissors_image = scissors_image.resize((150,150))
scissors_photo = ImageTk.PhotoImage(scissors_image)
image_dict['scissors'] = scissors_photo  # Store the PhotoImage object in the dictionary
   
def display_image(image):
    label.config(image=image)
    label.image = image  # to keep a reference to the image


def button_click(choice):
    image = image_dict.get(choice, None)
    if image:
        display_image(image)

# Create a button with an image
rock_button = Button(window, text="Click me", image=rock_photo, compound="left", command=button_click,width=150, height=150)
rock_button.place(x=0,y=300)

# Create a button with an image
paper_button = Button(window, text="Click me", image=paper_photo, compound="left", command=button_click,width=150, height=150)
paper_button.place(x=200,y=300)

# Create a button with an image
scissors_button = Button(window, text="Click me", image=scissors_photo, compound="left", command=button_click,width=150, height=150)
scissors_button.place(x=400,y=300)

window.mainloop()

