import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.geometry("300x200")

# Open and resize the image
image = Image.open("btn_nohover.png")
image = image.resize((200, 50))  # Use Image.ANTIALIAS directly

# Convert the image to a format that Tkinter can use
photo = ImageTk.PhotoImage(image)

# Create a label with the image
label = tk.Label(root, image=photo)
label.image = photo  # To prevent image from being garbage collected
label.pack(padx=20, pady=20)

# Run the main event loop
root.mainloop()
