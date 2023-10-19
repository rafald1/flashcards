import tkinter as tk

COLOR = ["#222831", "#393E46", "#00ADB5", "#EEEEEE"]
TIMER = 1000


class App(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Spanish Flashcards")
        self.config(padx=40, pady=35, bg=COLOR[0])
        self.geometry("1200x1000")
        self.minsize(width=1200, height=1000)
        container = tk.Frame(self, bg=COLOR[0])
        container.pack(fill="none", expand=True)
        self.frames = {
            "Select": SelectPage(container, self),
            "Main": MainPage(container, self)
        }
        self.show_frame("Select")
        self.selected_category = None

    def show_frame(self, frame_name):
        self.frames[frame_name].tkraise()
        if frame_name == "Select":
            self.frames[frame_name].update_listbox()  # refreshing the count of words to learn
        elif frame_name == "Main":
            self.frames[frame_name].reset_card()  # ensuring the front of card is shown


class SelectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        tk.Button(self, text="Continue", highlightbackground=COLOR[2], pady=20, font="Helvetica 24",
                  command=self.proceed).pack(fill=tk.X)
        tk.Button(self, text="Reset progress", highlightbackground=COLOR[2], pady=20, font="Helvetica 24",
                  command=self.reset_progress).pack(fill=tk.X)
        self.listbox = tk.Listbox(self, bg=COLOR[1], font="Helvetica 24", fg=COLOR[3], height=4, width=74)
        self.listbox.pack(side="left", fill="y")
        scrollbar = tk.Scrollbar(self, orient='vertical', command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    def update_listbox(self):
        self.listbox.delete(0, "end")
        categories = self.controller.game.build_list_of_categories()
        for category in categories:
            self.listbox.insert("end", f"{category[0]} ({category[1]})")
        self.listbox.select_set(0)

    def proceed(self):
        selected_category = self.listbox.get(self.listbox.curselection())
        self.controller.selected_category = selected_category.split(" ")[0]
        self.controller.show_frame("Main")

    def reset_progress(self):
        selected_category = self.listbox.get(self.listbox.curselection())
        self.controller.game.reset_progress(selected_category.split(" ")[0])
        self.update_listbox()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.current_word = None
        self.timer = None
        self.grid(row=0, column=0, sticky="nsew")
        tk.Button(self, text="Go to the Select Screen", highlightbackground=COLOR[2], pady=20, font="Helvetica 24",
                  command=self.back_to_select_screen).pack(side="top", fill=tk.X)
        self.card_back = tk.PhotoImage(file="image/card_back.png")
        self.card_front = tk.PhotoImage(file="image/card_front.png")
        self.lbl = tk.Label(self, compound=tk.CENTER, image=self.card_front, wraplength=600,
                            text="Press ❌ or ✅︎ button to start",
                            font="Helvetica 50 bold", fg=COLOR[2])
        self.lbl.pack()
        self.btn_not_learned = tk.Button(self, text="❌", highlightbackground=COLOR[2], pady=20, font="Helvetica 24",
                                         width=35, command=lambda: self.draw_next_card(False))
        self.btn_not_learned.pack(side="left", fill=tk.X)
        self.btn_learned = tk.Button(self, text="✅︎", highlightbackground=COLOR[2], pady=20, font="Helvetica 24",
                                     width=35, command=lambda: self.draw_next_card(True))
        self.btn_learned.pack(side="right", fill=tk.X)

    def change_state_of_learned_and_not_learned_buttons(self, state):
        if state == "disabled" or state == "normal":
            self.btn_learned.config(state=state)
            self.btn_not_learned.config(state=state)

    def show_card_back(self):
        self.change_state_of_learned_and_not_learned_buttons("disabled")
        self.lbl.config(image=self.card_back, text=self.current_word[2], fg=COLOR[3])
        self.lbl.update()
        self.controller.game.pronounce_word(self.current_word[2], "en")
        self.change_state_of_learned_and_not_learned_buttons("normal")

    def draw_next_card(self, mark_as_learned):
        self.change_state_of_learned_and_not_learned_buttons("disabled")
        if self.timer:
            self.after_cancel(self.timer)  # to cancel showing back of card if button was pressed prior this event
        if mark_as_learned and self.current_word:
            self.controller.game.mark_word_as_learned(id_value=self.current_word[0])
        self.current_word = self.controller.game.get_next_word(self.controller.selected_category)
        if self.current_word:
            self.lbl.config(image=self.card_front, text=self.current_word[1], fg=COLOR[2])
            self.lbl.update()
            self.controller.game.pronounce_word(self.current_word[1], "es")
            self.timer = self.after(TIMER, self.show_card_back)
        else:
            self.lbl.config(image=self.card_front, text="No more words.", fg=COLOR[2])
        self.change_state_of_learned_and_not_learned_buttons("normal")

    def reset_card(self):
        if self.timer:
            self.after_cancel(self.timer)
        self.lbl.config(image=self.card_front, text="Press ❌ or ✅︎ button to start", fg=COLOR[2])

    def back_to_select_screen(self):
        if self.timer:
            self.after_cancel(self.timer)
        self.controller.show_frame("Select")
