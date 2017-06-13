import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from io import BytesIO
import webbrowser

import siteparser


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Football")
        self.club = None

        self.main_container = tk.Frame(self, borderwidth=1, relief="sunken", pady=10)
        self.main_container.pack(fill=tk.X, side=tk.TOP)

        self.init_teamname_container()

        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(expand=1, fill="both")

        self.init_emblem_gui()
        self.init_info_gui()
        self.init_team_gui()

    # Init methods:
    def init_teamname_container(self):
        teamname_container = tk.Frame(self.main_container, borderwidth=1, relief="sunken", pady=10)
        teamname_container.pack(fill=tk.X, side=tk.TOP)
        teamnameLabel = tk.Label(teamname_container, text='Название клуба:', padx=10)
        teamnameLabel.grid(row=0, column=0)
        self.teamnameEntry = tk.Entry(teamname_container)
        self.teamnameEntry.grid(row=0, column=1)
        teamname_applyBtn = tk.Button(teamname_container, text='Поиск', padx=10)
        teamname_applyBtn.bind("<Button-1>", self.teamname_apply_click)
        teamname_applyBtn.grid(row=0, column=2, padx=10)

        self.teamnameInfoLabel = tk.Label(teamname_container, text='', padx=10)
        self.teamnameInfoLabel.grid(row=1, columnspan=3)

    def init_emblem_gui(self):
        emblem_page = ttk.Frame(self.notebook)
        self.notebook.add(emblem_page, text='Эмблема')

        self.emblem_image = tk.Label(emblem_page)
        self.emblem_image.pack(padx=10, pady=10)

        goto_club_btn = tk.Button(emblem_page, text='Перейти на страницу клуба', padx=10)
        goto_club_btn.bind("<Button-1>", self.goto_club_click)
        goto_club_btn.pack(padx=10, pady=10)

    def init_info_gui(self):
        self.info_page = ttk.Frame(self.notebook)
        self.notebook.add(self.info_page, text='Ближайшие игры')

    def init_team_gui(self):
        self.team_page = ttk.Frame(self.notebook)
        self.notebook.add(self.team_page, text='Состав команды')

    # Update methods:

    def update_emblem_gui(self):
        if self.club:
            image = self.club.image
        else:
            image = None

        if image:
            imgdata = Image.open(BytesIO(image))
            imgdata.thumbnail((500, 500), Image.ANTIALIAS)
            photoimage = ImageTk.PhotoImage(imgdata)
        else:
            photoimage = None

        self.emblem_image.configure(image=photoimage)
        self.emblem_image.image = photoimage

    def update_info_gui(self):
        for widget in self.info_page.winfo_children():
            widget.destroy()

        row = 0
        for game in self.club.games[-5:]:
            tk.Label(self.info_page, text=game.date, padx=10).grid(row=row, column=0)
            tk.Label(self.info_page, text=game.contestant, padx=10).grid(row=row, column=1)
            tk.Label(self.info_page, text=game.score, padx=10).grid(row=row, column=2)
            row += 1

    def update_team_gui(self):
        for widget in self.team_page.winfo_children():
            widget.destroy()

        row = 0
        for player in self.club.team:
            tk.Label(self.team_page, text=player.name, padx=10).grid(row=row, column=0)
            tk.Label(self.team_page, text=player.role, padx=10).grid(row=row, column=1)
            row += 1

    # Event handlers:

    def teamname_apply_click(self, ev):
        self.teamnameInfoLabel.config(text='Поиск')
        self.update()
        self.club = siteparser.ClubFactory.init_club(self.teamnameEntry.get())
        if self.club:
            self.teamnameInfoLabel.config(text=self.club.name)
        else:
            self.teamnameInfoLabel.config(text='Ничего не найдено')

        self.update_emblem_gui()
        self.update_info_gui()
        self.update_team_gui()

    def goto_club_click(self, ev):
        if self.club and self.club.href != '':
            webbrowser.open_new(self.club.href)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
