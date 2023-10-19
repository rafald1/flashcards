from database import Data
from game import Game
from window import App
# from db.spanish_words import animals


if __name__ == '__main__':
    db = Data()
    # db.add_many_items(animals, "ANIMAL")
    game = Game(db)
    app = App(game)
    app.mainloop()
    db.close_db()
