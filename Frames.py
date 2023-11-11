import tkinter as tk
from PIL import Image, ImageTk
from Buttons import HoverButton


class Frame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.font_button = ("Roboto Bold", 14)
        self.font_header1 = ("Roboto Bold", 20)
        self.font_header2 = ("Roboto Bold", 16)
        self.font_body = ("Roboto", 14)


class WelcomeFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('welcome frame instantiated successfully')

        frame_login = tk.Frame(self, pady=20, width=100, height=300)
        frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        entry_login = tk.Entry(frame_login,
                               width=40,
                               font=self.font_header2,
                               fg='#649B7A')
        entry_login.configure(font=self.font_header2)
        entry_login.grid(row=0, column=0, columnspan=2, pady=5)

        entry_password = tk.Entry(frame_login,
                                  width=40,
                                  font=self.font_header2,
                                  show='*',
                                  fg='#649B7A')
        entry_password.grid(row=1, column=0, columnspan=2, pady=5)

        btn_new_user = HoverButton(frame_login,
                                   borderwidth=0,
                                   highlightthickness=2,
                                   relief='flat',
                                   foreground='white',
                                   font=self.font_button,
                                   text='New User',
                                   compound=tk.CENTER,
                                   padx=5)
        btn_new_user.grid(row=2, column=0, sticky='w')

        btn_login = HoverButton(frame_login,
                                borderwidth=0,
                                highlightthickness=2,
                                relief='flat',
                                foreground='white',
                                font=self.font_button,
                                text='Login',
                                compound=tk.CENTER,
                                padx=5)
        btn_login.grid(row=2, column=1, sticky='e')


class RecipeFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('recipe frame instantiated successfully')

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
                                          font=self.font_button,
                                          text='New Recipe',
                                          compound=tk.CENTER,
                                          padx=5)
        self.btn_new_recipe.grid(row=0, column=0, sticky='ew')

        self.btn_meal_plan = HoverButton(self,
                                         borderwidth=0,
                                         highlightthickness=2,
                                         relief='flat',
                                         foreground='white',
                                         font=self.font_button,
                                         text='New Meal Plan',
                                         compound=tk.CENTER,
                                         padx=5)
        self.btn_meal_plan.grid(row=0, column=1, sticky='w')

        self.btn_addto_mealplan = HoverButton(self,
                                              borderwidth=0,
                                              highlightthickness=2,
                                              relief='flat',
                                              foreground='white',
                                              font=self.font_button,
                                              text=' >>> ',
                                              compound=tk.CENTER,
                                              padx=5)
        self.btn_addto_mealplan.grid(row=1, column=2, sticky='s')

        self.btn_remove_mealplan = HoverButton(self,
                                               borderwidth=0,
                                               highlightthickness=2,
                                               relief='flat',
                                               foreground='white',
                                               font=self.font_button,
                                               text=' <<< ',
                                               compound=tk.CENTER,
                                               padx=5)
        self.btn_remove_mealplan.grid(row=1, column=2)

        self.btn_refresh = HoverButton(self,
                                       borderwidth=0,
                                       highlightthickness=2,
                                       relief='flat',
                                       foreground='white',
                                       font=self.font_button,
                                       text='Refresh',
                                       compound=tk.CENTER,
                                       padx=5)
        self.btn_refresh.grid(row=2, column=0, sticky='s')

        self.btn_save_mealplan = HoverButton(self,
                                             borderwidth=0,
                                             highlightthickness=2,
                                             relief='flat',
                                             foreground='white',
                                             font=self.font_button,
                                             text='Save Plan',
                                             compound=tk.CENTER,
                                             padx=5)
        self.btn_save_mealplan.grid(row=0, column=3, sticky='e', columnspan=2)

        # Recipe List
        self.list_recipes = tk.Listbox(self, font=("Roboto", 12), width=22, height=40)
        self.list_recipes.grid(row=1, column=0, padx=5, sticky='ns', rowspan=1)

        self.view_recipe = tk.Text(self, font=self.font_button, height=40)
        self.view_recipe.grid(row=1, column=1, padx=5, rowspan=2, sticky='ns')

        self.view_meal_plans = tk.Listbox(self, font=self.font_button, height=35, width=32)
        self.view_meal_plans.grid(row=1, column=3, padx=5, rowspan=2, columnspan=2, sticky='ns')

        self.list_recipes.insert(tk.END, "Recipe 1")


class GroceryFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('grocery frame instantiated successfully')

        frame_buttons = tk.Frame(self)
        frame_buttons.grid(row=0, column=0)

        btn_new_list = HoverButton(frame_buttons,
                                   borderwidth=0,
                                   highlightthickness=2,
                                   relief='flat',
                                   foreground='white',
                                   font=self.font_button,
                                   text='New List',
                                   compound=tk.CENTER,
                                   padx=5)
        btn_new_list.pack()


class PantryFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('pantry frame instantiated successfully')


class CharlesFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print('chef frame instantiated successfully')
