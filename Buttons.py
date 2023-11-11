import tkinter as tk
from PIL import Image, ImageTk


class HoverButton(tk.Button):
    def __init__(self, master, **kwargs):
        tk.Button.__init__(self, master=master, **kwargs)

        # Set button images
        img_hover = Image.open("btn_hover2.png")
        img_default = Image.open("btn_default.png")
        on_hover = ImageTk.PhotoImage(img_hover)
        on_default = ImageTk.PhotoImage(img_default)

        self.default_fg = kwargs.get('default_fg', 'white')  # Default text color
        self.hover_fg = kwargs.get('hover_fg', '#649B7A')  # Hover text color

        self.default_img = on_default
        self.hover_img = on_hover
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

        if self.default_img:
            self.config(image=self.default_img)

    def on_enter(self, e):
        if self.hover_img:
            self.config(image=self.hover_img)
        self.config(fg=self.hover_fg)  # Change text color on hover

    def on_leave(self, e):
        if self.default_img:
            self.config(image=self.default_img)
        self.config(fg=self.default_fg)  # Change text color on hover

    def on_click(self, e):
        self.config(fg='white')
