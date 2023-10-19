import sqlite3


class ErrorSql:
    @staticmethod
    def catch(func):
        def inner(self, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)
                return result
            except sqlite3.Error as error:
                print("SQLite error: ", error)
        return inner


class Data(ErrorSql):
    def __init__(self):
        self.con = sqlite3.connect("db/default.db")
        self.cursor = self.con.cursor()

    @ErrorSql.catch
    def create(self):
        self.cursor.execute('''CREATE TABLE spanish_words (
            id INTEGER PRIMARY KEY,
            word_es TEXT NOT NULL,
            word_en TEXT NOT NULL,
            is_learned BOOLEAN NOT NULL,
            category TEXT NOT NULL
            )''')
        self.con.commit()

    @ErrorSql.catch
    def add_item(self, word_es, word_en, is_learned, category):
        self.cursor.execute(f'''INSERT INTO spanish_words (word_es, word_en, is_learned, category) 
            VALUES ("{word_es}", "{word_en}", {is_learned}, "{category}")''')
        self.con.commit()

    @ErrorSql.catch
    def add_many_items(self, lst, category):
        self.cursor.executemany(f'''INSERT INTO spanish_words (word_es, word_en, is_learned, category)
            VALUES (?, ?, False, "{category}")''', lst)
        self.con.commit()

    @ErrorSql.catch
    def fetch_all_items(self):
        self.cursor.execute('SELECT * FROM spanish_words')
        return self.cursor.fetchall()

    @ErrorSql.catch
    def fetch_data(self, key, value):
        self.cursor.execute(f'SELECT * FROM spanish_words WHERE {key} = ? AND is_learned = 0', (value, ))
        return self.cursor.fetchall()

    @ErrorSql.catch
    def mark_word_as_learned(self, key, value):
        self.cursor.execute(f'UPDATE spanish_words SET is_learned = 1 WHERE {key} = ?', (value, ))
        self.con.commit()

    @ErrorSql.catch
    def reset_learned_value(self, key, value):
        self.cursor.execute(f'UPDATE spanish_words SET is_learned = 0 WHERE {key} = ?', (value, ))
        self.con.commit()

    @ErrorSql.catch
    def get_count_of_not_learned_words_by_category(self):
        self.cursor.execute('SELECT DISTINCT category FROM spanish_words')
        all_unique_categories = self.cursor.fetchall()
        # A category gets omitted if all words are learned in this category
        self.cursor.execute('SELECT category, COUNT(*) FROM spanish_words WHERE is_learned = 0 GROUP BY category')
        group_by_categories = self.cursor.fetchall()
        # Adding missing categories with not learned words count equal to 0
        for category in all_unique_categories:
            if any(category[0] in element for element in group_by_categories):
                continue
            else:
                group_by_categories.append((category[0], 0))
        return sorted(group_by_categories, key=lambda element: element[0])

    def close_db(self):
        self.con.close()
