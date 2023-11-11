import tkinter as tk
from PIL import Image, ImageTk
from Buttons import HoverButton


class WelcomeFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('welcome frame instantiated successfully')

        btn_font = ("Roboto Bold", 14)

        # Load the image
        img = Image.open("main_logo.png")
        img.resize((200, 200))
        self.img_logo = ImageTk.PhotoImage(img)

        # Create a label with the image
        img_label = tk.Label(self, image=self.img_logo)
        img_label.place(width=500,
                        height=500,
                        relx=0.5,
                        rely=0.5,
                        anchor=tk.CENTER)


class RecipeFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('recipe frame instantiated successfully')

        btn_font = ("Roboto Bold", 14)

        # Set button images
        img_hover = Image.open("btn_hover2.png")
        img_default = Image.open("btn_default.png")
        on_hover = ImageTk.PhotoImage(img_hover)
        on_default = ImageTk.PhotoImage(img_default)

        self.btn_new_recipe = HoverButton(self,
                                          borderwidth=0,
                                          highlightthickness=2,
                                          relief='flat',
                                          foreground='white',
                                          font=btn_font,
                                          text='New Recipe',
                                          compound=tk.CENTER,
                                          padx=5)
        self.btn_new_recipe.grid(row=0, column=0, sticky='ew')

        self.btn_meal_plan = HoverButton(self,
                                         borderwidth=0,
                                         highlightthickness=2,
                                         relief='flat',
                                         foreground='white',
                                         font=btn_font,
                                         text='New Meal Plan',
                                         compound=tk.CENTER,
                                         padx=5)
        self.btn_meal_plan.grid(row=0, column=1, sticky='w')

        self.btn_addto_mealplan = HoverButton(self,
                                              borderwidth=0,
                                              highlightthickness=2,
                                              relief='flat',
                                              foreground='white',
                                              font=btn_font,
                                              text=' >>> ',
                                              compound=tk.CENTER,
                                              padx=5)
        self.btn_addto_mealplan.grid(row=1, column=2, sticky='s')

        self.btn_remove_mealplan = HoverButton(self,
                                               borderwidth=0,
                                               highlightthickness=2,
                                               relief='flat',
                                               foreground='white',
                                               font=btn_font,
                                               text=' <<< ',
                                               compound=tk.CENTER,
                                               padx=5)
        self.btn_remove_mealplan.grid(row=1, column=2)

        self.btn_refresh = HoverButton(self,
                                       borderwidth=0,
                                       highlightthickness=2,
                                       relief='flat',
                                       foreground='white',
                                       font=btn_font,
                                       text='Refresh',
                                       compound=tk.CENTER,
                                       padx=5)
        self.btn_refresh.grid(row=2, column=0, sticky='s')

        self.btn_save_mealplan = HoverButton(self,
                                             borderwidth=0,
                                             highlightthickness=2,
                                             relief='flat',
                                             foreground='white',
                                             font=btn_font,
                                             text='Save Plan',
                                             compound=tk.CENTER,
                                             padx=5)
        self.btn_save_mealplan.grid(row=0, column=3, sticky='e', columnspan=2)

        # Recipe List
        self.list_recipes = tk.Listbox(self, font=("Roboto", 12), width=22, height=40)
        self.list_recipes.grid(row=1, column=0, padx=5, sticky='ns', rowspan=1)

        self.view_recipe = tk.Text(self, font=btn_font, height=40)
        self.view_recipe.grid(row=1, column=1, padx=5, rowspan=2, sticky='ns')

        self.view_meal_plans = tk.Listbox(self, font=btn_font, height=35, width=32)
        self.view_meal_plans.grid(row=1, column=3, padx=5, rowspan=2, columnspan=2, sticky='ns')

        self.list_recipes.insert(tk.END, "Recipe 1")


class GroceryFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('grocery frame instantiated successfully')


class PantryFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('pantry frame instantiated successfully')


class CharlesFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('chef frame instantiated successfully')
