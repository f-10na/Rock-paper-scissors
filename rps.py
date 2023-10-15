from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Button
import itertools

window = tk.Tk()

# Dictionary to store PhotoImage objects
image_dict = {}

#the code below gets the image of the rock and then converts it into a photo that can be displayed on tkinter and then stored as a key in a dictionary
rock_path = "rock.jpeg"
rock_image = Image.open(rock_path)
rock_image = rock_image.resize((150,150))
rock_photo = ImageTk.PhotoImage(rock_image)
image_dict['rock'] = rock_photo  # Store the PhotoImage object in the dictionary

#the code below gets the image of the paper and then converts it into a photo that can be displayed on tkinter and then stored as a key in a dictionary
paper_path = "paper.jpeg"
paper_image = Image.open(paper_path)
paper_image = paper_image.resize((150,150))
paper_photo = ImageTk.PhotoImage(paper_image)
image_dict['paper'] = paper_photo  # Store the PhotoImage object in the dictionary

#the code below gets the image of the scissor and then converts it into a photo that can be displayed on tkinter and then stored as a key in a dictionary
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
rock_button = Button(window, text="Click me", image=rock_photo, compound="left", command=button_click(image_dict.get('rock')),width=150, height=150)
rock_button.place(x=0,y=300)

# Create a button with an image
paper_button = Button(window, text="Click me", image=paper_photo, compound="left", command=button_click(image_dict.get('paper')),width=150, height=150)
paper_button.place(x=200,y=300)

# Create a button with an image
scissors_button = Button(window, text="Click me", image=scissors_photo, compound="left", command=button_click(image_dict.get('scissors')),width=150, height=150)
scissors_button.place(x=400,y=300)

# Create a label for displaying the images
label = tk.Label(window, width=150, height=150)
label.place(x=200, y=50)  # Adjust the position as needed

# Create an iterator to cycle through the image keys ('rock', 'paper', 'scissors')
image_cycle = itertools.cycle(image_dict.keys())

def animate():
    # Get the next image key from the cycle
    image_key = next(image_cycle)
    # Get the corresponding image from the image_dict
    image = image_dict.get(image_key)
    # Display the image
    display_image(image)
    # Call animate function again after 2000 milliseconds (2 seconds)
    window.after(1000, animate)

# Start the animation loop
animate()

window.mainloop()

