import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Buttons import HoverButton
from Frames import WelcomeFrame, RecipeFrame, GroceryFrame, PantryFrame, CharlesFrame
import sys


# Function to switch between frames
def show_frame(index):
    for i, frame in enumerate(frames):
        if i == index:
            frame.pack(fill="both", expand=True)
        else:
            frame.pack_forget()


# Close Program
def close_program():
    sys.exit()


# Root Frame
root = tk.Tk()
root.geometry("1920x1080")
root.config(bg='white')

# Button Font
btn_font = ("Roboto Bold", 18)

# Navigation Frame
frame_navigation = tk.Frame(root, width=100, height=600, padx=5, pady=10)
frame_navigation.pack(side="left", fill="y")

# Recipe Nav Button
btn_recipes = HoverButton(frame_navigation,
                          borderwidth=0,
                          highlightthickness=2,
                          relief="flat",
                          foreground='white',
                          font=btn_font,
                          text="Recipes",
                          compound=tk.CENTER)
btn_recipes.pack()

# Grocery Lists Button
btn_groceries = HoverButton(frame_navigation,
                            borderwidth=0,
                            highlightthickness=2,
                            relief="flat",
                            foreground='white',
                            font=btn_font,
                            text='Grocery Lists',
                            compound=tk.CENTER)
btn_groceries.pack()

# Pantry Button
btn_pantry = HoverButton(frame_navigation,
                         borderwidth=0,
                         highlightthickness=2,
                         relief="flat",
                         foreground='white',
                         font=btn_font,
                         text='Pantry',
                         compound=tk.CENTER)
btn_pantry.pack()

# ChefAI Button
btn_chef = HoverButton(frame_navigation,
                       borderwidth=0,
                       highlightthickness=2,
                       relief="flat",
                       foreground='white',
                       font=btn_font,
                       text='ChefAI',
                       compound=tk.CENTER)
btn_chef.pack()

# Spacer for nav frame
lbl_spacer = tk.Label(frame_navigation, text='', pady=340)
lbl_spacer.pack()

# Exit Program
btn_exit = HoverButton(frame_navigation,
                       borderwidth=0,
                       highlightthickness=2,
                       relief="flat",
                       foreground='white',
                       font=btn_font,
                       text='Exit',
                       compound=tk.CENTER,
                       command=close_program)
btn_exit.pack()

# Main Widgets
# Create a frame for stacking
stack_frame = tk.Frame(root, width=100, height=100, padx=10, pady=10)
stack_frame.pack(side="right", expand=True, fill="both")

# Create three frames to be stacked
frame0 = WelcomeFrame(stack_frame, width=100, height=100)
frame1 = RecipeFrame(stack_frame, width=100, height=100)
frame2 = GroceryFrame(stack_frame, bg="blue", width=100, height=100)
frame3 = PantryFrame(stack_frame, bg="green", width=100, height=100)
frame4 = CharlesFrame(stack_frame, bg="yellow", width=100, height=100)

frames = [frame0, frame1, frame2, frame3, frame4]

# Create buttons to switch between frames
btn_recipes.config(command=lambda: show_frame(1))
btn_groceries.config(command=lambda: show_frame(2))
btn_pantry.config(command=lambda: show_frame(3))
btn_chef.config(command=lambda: show_frame(4))

# Show the first frame initially
show_frame(0)

# Run loop
root.mainloop()
